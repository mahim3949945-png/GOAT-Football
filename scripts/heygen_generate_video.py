#!/usr/bin/env python3
"""Submit a HeyGen video job and optionally poll/download the result.

Required environment variables:
  HEYGEN_API_KEY

For avatar mode:
  HEYGEN_AVATAR_ID
  HEYGEN_VOICE_ID

For image mode:
  HEYGEN_VOICE_ID
  pass --image-url https://...

The script intentionally reads secrets from environment variables instead of
hardcoding them in source files or command history.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


API_BASE = "https://api.heygen.com"
DEFAULT_SCRIPT_FILE = Path("outputs/ai-kol-greenscreen-director/heygen-script.txt")
DEFAULT_RESULT_FILE = Path("outputs/ai-kol-greenscreen-director/heygen-result.json")
DEFAULT_VIDEO_FILE = Path("outputs/ai-kol-greenscreen-director/heygen-video.mp4")


class HeyGenError(RuntimeError):
    """Raised when HeyGen returns an error response."""


def env_required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise HeyGenError(f"Missing required environment variable: {name}")
    return value


def read_script(args: argparse.Namespace) -> str:
    if args.text:
        return args.text.strip()

    script_file = Path(args.script_file)
    if not script_file.exists():
        raise HeyGenError(
            f"Script file not found: {script_file}. "
            "Pass --text or create the script file first."
        )

    text = script_file.read_text(encoding="utf-8").strip()
    if not text:
        raise HeyGenError(f"Script file is empty: {script_file}")
    return text


def request_json(method: str, url: str, api_key: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None
    headers = {"X-Api-Key": api_key}
    if payload is not None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            response_body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise HeyGenError(f"HeyGen HTTP {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise HeyGenError(f"HeyGen request failed: {exc}") from exc

    try:
        data = json.loads(response_body)
    except json.JSONDecodeError as exc:
        raise HeyGenError(f"HeyGen returned non-JSON response: {response_body}") from exc

    if data.get("error"):
        raise HeyGenError(f"HeyGen error: {data['error']}")
    return data


def submit_avatar_video(args: argparse.Namespace, api_key: str, script: str) -> str:
    avatar_id = args.avatar_id or env_required("HEYGEN_AVATAR_ID")
    voice_id = args.voice_id or env_required("HEYGEN_VOICE_ID")

    payload: dict[str, Any] = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": avatar_id,
                    "avatar_style": args.avatar_style,
                },
                "voice": {
                    "type": "text",
                    "input_text": script,
                    "voice_id": voice_id,
                },
            }
        ]
    }

    if args.width and args.height:
        payload["dimension"] = {"width": args.width, "height": args.height}
    if args.title:
        payload["title"] = args.title

    data = request_json("POST", f"{API_BASE}/v2/video/generate", api_key, payload)
    try:
        return data["data"]["video_id"]
    except KeyError as exc:
        raise HeyGenError(f"Could not find video_id in response: {data}") from exc


def submit_image_video(args: argparse.Namespace, api_key: str, script: str) -> str:
    if not args.image_url:
        raise HeyGenError("Image mode requires --image-url with a public HTTPS image URL.")

    voice_id = args.voice_id or env_required("HEYGEN_VOICE_ID")
    payload = {
        "type": "image",
        "image": {
            "type": "url",
            "url": args.image_url,
        },
        "script": script,
        "voice_id": voice_id,
        "title": args.title or "AI KOL Greenscreen Director",
        "resolution": args.resolution,
        "aspect_ratio": args.aspect_ratio,
    }

    data = request_json("POST", f"{API_BASE}/v3/videos", api_key, payload)
    try:
        return data["data"]["video_id"]
    except KeyError as exc:
        raise HeyGenError(f"Could not find video_id in response: {data}") from exc


def get_video_status(video_id: str, api_key: str) -> dict[str, Any]:
    data = request_json("GET", f"{API_BASE}/v3/videos/{video_id}", api_key)
    try:
        return data["data"]
    except KeyError as exc:
        raise HeyGenError(f"Could not find video data in response: {data}") from exc


def poll_until_done(video_id: str, api_key: str, interval: int, timeout: int) -> dict[str, Any]:
    deadline = time.monotonic() + timeout
    while True:
        status_data = get_video_status(video_id, api_key)
        status = status_data.get("status")
        print(f"HeyGen status for {video_id}: {status}", flush=True)

        if status == "completed":
            return status_data
        if status == "failed":
            message = status_data.get("failure_message") or status_data.get("failure_code") or status_data
            raise HeyGenError(f"HeyGen video failed: {message}")
        if time.monotonic() >= deadline:
            raise HeyGenError(f"Timed out waiting for HeyGen video: {video_id}")

        time.sleep(interval)


def download_video(video_url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(video_url, timeout=120) as response:
        output_path.write_bytes(response.read())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a HeyGen video from an avatar or public image URL.")
    parser.add_argument("--mode", choices=["avatar", "image"], default="avatar")
    parser.add_argument("--script-file", default=str(DEFAULT_SCRIPT_FILE))
    parser.add_argument("--text", help="Voiceover text. Overrides --script-file.")
    parser.add_argument("--title", default="AI KOL Greenscreen Director")
    parser.add_argument("--result-file", default=str(DEFAULT_RESULT_FILE))

    parser.add_argument("--avatar-id", help="Overrides HEYGEN_AVATAR_ID for avatar mode.")
    parser.add_argument("--avatar-style", default="normal")
    parser.add_argument("--voice-id", help="Overrides HEYGEN_VOICE_ID.")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)

    parser.add_argument("--image-url", help="Public HTTPS image URL for image mode.")
    parser.add_argument("--resolution", default="1080p")
    parser.add_argument("--aspect-ratio", default="9:16")

    parser.add_argument("--wait", action="store_true", help="Poll until the video is completed or failed.")
    parser.add_argument("--poll-interval", type=int, default=10)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--download", action="store_true", help="Download completed video_url after --wait.")
    parser.add_argument("--video-file", default=str(DEFAULT_VIDEO_FILE))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        api_key = env_required("HEYGEN_API_KEY")
        script = read_script(args)

        if args.mode == "avatar":
            video_id = submit_avatar_video(args, api_key, script)
        else:
            video_id = submit_image_video(args, api_key, script)

        result: dict[str, Any] = {"video_id": video_id, "status": "submitted"}
        print(json.dumps(result, ensure_ascii=False, indent=2))

        if args.wait:
            video_data = poll_until_done(video_id, api_key, args.poll_interval, args.timeout)
            result.update(video_data)

            video_url = video_data.get("video_url")
            if args.download and video_url:
                download_video(video_url, Path(args.video_file))
                result["downloaded_to"] = args.video_file

        result_file = Path(args.result_file)
        result_file.parent.mkdir(parents=True, exist_ok=True)
        result_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return 0
    except HeyGenError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
