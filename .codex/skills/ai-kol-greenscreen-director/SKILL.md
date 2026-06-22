---
name: ai-kol-greenscreen-director
description: 专属 AI 绿幕口播视频导演与 Prompt 工程师。用于把“人物 + 场景 + 尺寸”转成中东足球资讯 App 绿幕 KOL 广告的 I2V 方案，并生成口播首帧与举绿幕手机垫图。
---

# AI KOL Greenscreen Director

Use this skill when the user asks to generate a green-screen KOL talking-head ad for the football app, especially when the request starts with `生成KOL：`.

## Input Rules

- The request must start with `生成KOL：`.
- If the request does not start with `生成KOL：`, give a short intake guide and ask the user to resend in this format:
  - `生成KOL：人物 + 场景 + 尺寸`
  - Example: `生成KOL：中东男足球迷，现代客厅比赛日氛围，9:16`
- Required intake:
  - Character / person
  - Scene / background
  - Size: `1:1`, `9:16`, `16:9`, or custom
- If size is missing, ask the user to choose `1:1`, `9:16`, `16:9`, or provide a custom size.
- Duration defaults to 30 seconds unless the user explicitly provides another duration.

## Creative Direction

Create a clean, executable I2V plan for a Middle East football news app green-screen KOL ad.

The video should:

- Open with football match-day pain points and emotional setup for the first 10 seconds.
- Introduce the app features after the 10-second mark.
- Feel like a real KOL talking-head delivery, with natural blinking, breathing, slight nods, and moderate speaking pace.
- Avoid stiff expression, robotic delivery, dead eyes, or a frozen face.

Required app selling points:

- Starting lineups
- Formation analysis
- Match statuses: `END`, `Delayed`, `ABD`, `CAN`
- Follow up to 5 teams
- Follow up to 5 competitions / leagues
- Customized score homepage

## Image Plan

Generate two images by default:

1. `first-frame.png`
   - Pure talking-head first frame.
   - No phone visible.
   - Clean background with no background people, clutter, pillars, app logo, corner bug, sticker, or extra brand icon.
   - Focus on the KOL's face.

2. `phone-reference.png`
   - Must be generated from `first-frame.png` as the main reference.
   - Only add the action of holding up a phone.
   - Keep the same person, face, hairstyle, skin tone, perceived age, jersey, scene, lighting, and camera distance.
   - Phone screen must be pure chroma key green.
   - Phone should occupy about 70% of the frame.
   - Phone and green screen must be sharp and clear.
   - Person and background must be clearly blurred, creating rack focus / shallow depth of field.

## Output Requirements

Return a concise production-ready output that includes:

- Validated intake summary
- 30-second script structure, or the user-specified duration
- Visual direction for Step 1 and Step 2
- I2V prompt
- Negative prompt
- Generated image filenames
- Save locations

Save generated images to:

- `~/Desktop/ai-kol-greenscreen-director/`
- `outputs/ai-kol-greenscreen-director/` when running in a cloud workspace

Finally, show the images directly and tell the user both the cloud desktop path and the workspace output path.
