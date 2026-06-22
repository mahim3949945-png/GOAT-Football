# Output Blueprint

Use this structure for the final response after intake is valid.

## 1. 镜头设定解析

Return a concise parsed summary:

- 人物：
- 场景：
- 尺寸：
- 时长：默认 30 秒，或用户指定时长
- 核心镜头逻辑：先口播，后举手机，最后 rack focus 到纯绿手机屏幕

## 2. Step 1 - 纯口播首帧图片

Include:

- File name: `first-frame.png`
- Purpose: pure talking-head first frame for I2V
- Prompt used
- Negative prompt used

Generation requirements:

- No phone.
- Face in focus.
- Clean background.
- No logo, corner bug, sticker, watermark, or extra brand icon.

## 3. Step 2 - 举绿幕手机垫图

Include:

- File name: `phone-reference.png`
- Main reference: `first-frame.png`
- Prompt used
- Negative prompt used

Generation requirements:

- Must preserve the same person, clothing, scene, lighting, and camera distance from `first-frame.png`.
- Only add the phone raise action.
- Phone occupies about 70% of the frame.
- Phone screen is pure chroma key green.
- Phone and screen are sharp.
- Person and background are blurred with rack focus / shallow depth of field.

## 4. Step 3 - I2V 视频 Prompt

Include one production-ready I2V prompt:

- Use both images as references.
- 0-10 seconds: football watching pain point / match-day emotion.
- 10 seconds onward: football app feature introduction.
- End movement: raise phone and rack focus to green screen.
- Natural KOL performance: blinking, breathing, slight nods, moderate speaking pace.
- Preserve identity and scene consistency.

Include one negative prompt focused on:

- Identity drift.
- Changed clothes / scene / lighting.
- Stiff or robotic delivery.
- Dead eyes / frozen face.
- Background clutter or people.
- Phone screen not pure green.
- Blurry phone or distorted hands.
- Logos / UI / watermarks.

## 5. Step 4 - 30 秒足球 App 口播稿

For the default 30-second script, use this rhythm:

- 0-3s: match-day hook.
- 3-10s: pain point: lineups, formations, match status, team/league tracking.
- 10-22s: app features.
- 22-27s: customized score homepage and follow limits.
- 27-30s: phone raise / call to action.

Required feature mentions:

- 首发阵容
- 阵型分析
- `END`
- `Delayed`
- `ABD`
- `CAN`
- 最多关注 5 支球队
- 最多关注 5 项赛事/联赛
- 定制比分首页

If the user specifies a non-30-second duration, keep the same order and compress or expand the sections proportionally.

## 6. 保存路径说明

Always save generated images to:

```text
~/Desktop/ai-kol-greenscreen-director/
```

In cloud workspaces, also save to:

```text
outputs/ai-kol-greenscreen-director/
```

Use fixed file names:

```text
first-frame.png
phone-reference.png
```

## Final Message Requirements

After generation:

- Show both images directly in chat when the environment supports it.
- Tell the user:
  - Cloud desktop path.
  - Workspace output path.
  - Exact file names.
- Keep the final response concise and action-oriented.
