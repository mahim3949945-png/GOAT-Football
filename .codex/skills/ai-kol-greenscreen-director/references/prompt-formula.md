# I2V 时间轴与焦点控制公式

本公式用于生成标准化双步 Prompt。生成时应先把用户输入的【人物】和【场景】扩写为具备摄影细节、投放质感和明确视觉边界的描述，再填入模板。

## 扩写原则

### 人物扩写

人物描述应包含：

- 年龄段、地域 / 气质、发型、面部特征。
- 服装材质、颜色、版型。
- 口播状态：confident, energetic, speaking directly to the camera。
- 面部表现：clear facial expression, natural mouth movement, eye contact。

不要扩写为夸张怪异、过度奇幻或遮挡面部的造型。避免墨镜、口罩、大帽檐、夸张手势遮脸。

### 场景扩写

场景描述应包含：

- 空间类型与质感。
- 干净背景、浅层次布景、少量大色块。
- 柔和环境光、电影感补光。

无论用户输入什么场景，都必须净化为：

```text
clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions
```

## Step 1: Midjourney 首帧垫图 Prompt 模板

用途：生成演员定妆和视频首帧。此阶段必须是纯口播画面，不允许手机提前出现。

```text
Medium shot, [人物高精度扩写描述], speaking directly to the camera with natural mouth movement and confident eye contact. Focus strictly concentrated on the subject's face, highly detailed facial expressions, sharp eyes, clear facial features. Situated in [场景高精度扩写描述]. Clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions. The subject's hands stay naturally out of the foreground, no smartphone, no phone screen, no green screen, no handheld device visible. Warm ambient lighting, soft cinematic key light, photorealistic, high-end social media ad style, 8k, cinematic lighting --ar 9:16 --style raw --v 6.0
```

### Step 1 Negative Prompt 建议

```text
background people, crowd, columns, poles, clutter, messy props, phone, smartphone, green screen, hand holding phone, face obstruction, sunglasses, mask, text, watermark, logo, low quality, distorted hands, extra fingers
```

## Step 2: 视频大模型直出 Prompt 模板

用途：基于 Step 1 首帧生成动态视频。此阶段必须表现完整时间轴。

```text
[人物高精度扩写描述], situated in [场景高精度扩写描述]. Clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions. The video starts with a stable clear medium shot of the subject speaking passionately directly to the camera for the first three seconds, focus sharply and strictly concentrated on their face, natural mouth movement, direct eye contact, no smartphone visible at the beginning. After the first few seconds, the subject confidently lifts a modern smartphone from below the frame into the foreground toward the camera lens. The smartphone screen is perfectly flat, completely solid, bright chroma key green, evenly lit, with no UI, no text, no reflections, no patterns, no cracks, and no black borders. As the phone enters the foreground, a cinematic rack focus occurs smoothly: the camera focus shifts dynamically from the subject's face to the green smartphone screen. The green screen becomes extremely sharp and fills the viewer's attention, while the subject's face and the clean background smoothly transition into a beautiful shallow-depth-of-field blur and soft bokeh. High quality, photorealistic, 8k resolution, cinematic lighting, realistic handheld micro-movement, shot on a 35mm lens, vertical 9:16 social media ad.
```

### Step 2 Negative Prompt 建议

```text
phone visible at start, early phone reveal, background characters, crowd, clutter, columns, poles, messy room, extra props, screen reflections, phone UI, text on phone, patterned screen, dark green screen, uneven green, face remains sharper than phone after rack focus, no focus shift, blurry phone, warped phone, extra fingers, distorted hands, watermark, subtitles
```

## 时间轴硬约束

```text
0-3s: clear face-only talking head, no phone visible, focus locked on face
3s+: subject lifts chroma green smartphone into foreground
final: rack focus to phone screen, phone sharp, face and background blurred
```

## 质量检查

输出前检查：

- Step 1 是否完全无手机。
- Step 2 是否明确写出“前几秒无手机”。
- 是否出现 rack focus。
- 是否明确手机屏幕为纯 chroma key green。
- 是否反复排除了背景人物、杂物、立柱。
- 是否保证前段人脸清晰、后段手机清晰。
