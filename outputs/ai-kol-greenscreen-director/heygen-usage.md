# HeyGen Usage

Use HeyGen image mode when the digital human should change for every `生成KOL：...` request.

## Recommended Flow

1. Generate the KOL images with the skill:
   - `first-frame.png`
   - `phone-reference.png`
2. Upload `first-frame.png` to a public HTTPS URL.
   - HeyGen cannot read local paths such as `outputs/...` directly.
3. Choose an Arabic HeyGen voice and set its voice ID.
4. Submit the video job in image mode.

## Required Environment Variables

```bash
export HEYGEN_API_KEY="your_rotated_heygen_api_key"
export HEYGEN_VOICE_ID="your_arabic_voice_id"
```

Do not commit API keys or paste them into source files.

## Generate Arabic Video From Dynamic KOL Image

```bash
python3 scripts/heygen_generate_video.py \
  --mode image \
  --image-url "https://example.com/first-frame.png" \
  --script-file outputs/ai-kol-greenscreen-director/heygen-script.txt \
  --aspect-ratio 9:16 \
  --wait \
  --download
```

Outputs:

- Job result: `outputs/ai-kol-greenscreen-director/heygen-result.json`
- Downloaded video: `outputs/ai-kol-greenscreen-director/heygen-video.mp4`

## Fixed Avatar Alternative

Use avatar mode only when you want a fixed HeyGen avatar:

```bash
export HEYGEN_AVATAR_ID="your_avatar_id"
export HEYGEN_VOICE_ID="your_arabic_voice_id"

python3 scripts/heygen_generate_video.py \
  --mode avatar \
  --script-file outputs/ai-kol-greenscreen-director/heygen-script.txt \
  --wait \
  --download
```

For this project, image mode is preferred because the KOL appearance changes with each prompt.
