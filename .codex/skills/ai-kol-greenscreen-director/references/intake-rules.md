# Intake Rules

Use these rules before creating prompts or images.

## Trigger

The user request must start with:

```text
生成KOL：
```

If the request does not start with `生成KOL：`, do not generate images yet. Reply with this short guide:

```text
请按这个格式发送：
生成KOL：[人物外观与穿着] + [背景环境] + [尺寸/比例]

示例：
生成KOL：中东男足球迷，穿白色主场球衣 + 现代客厅比赛日氛围 + 9:16
```

## Required Fields

Extract three fields from the request:

1. Person
   - Appearance
   - Clothing
   - Age impression / gender / regional style when provided
2. Scene
   - Background environment
   - Lighting mood
   - Match-day atmosphere when provided
3. Size
   - `1:1`
   - `9:16`
   - `16:9`
   - Custom size or ratio

## Missing Size

If size is missing, ask only one concise clarification:

```text
请选择尺寸：1:1、9:16、16:9，或告诉我自定义比例。
```

Do not ask for duration unless the user mentions timing.

## Duration

- Default duration: 30 seconds.
- If the user specifies a different duration, use that duration.
- Keep the required rhythm:
  - First segment: football watching pain point / match-day emotion.
  - Later segment: app feature introduction.

For the default 30-second script:

- 0-10 seconds: football topic setup.
- 10-30 seconds: app benefits, phone raise, and green-screen phone handoff.

## Safety and Clean Frame Checks

Before generating prompts, enforce:

- No background people.
- No clutter.
- No pillars.
- No app logo, corner bug, sticker, watermark, or extra brand icon.
- Step 1 must not include a phone.
- Step 2 must include a pure chroma key green phone screen.
