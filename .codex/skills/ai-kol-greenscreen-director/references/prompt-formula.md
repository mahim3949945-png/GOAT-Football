# I2V 三步走时间轴与焦点控制公式

The Three-Step Timeline & Focus Formula

## 全局变量

- `[人物高精度扩写描述]`：包含外观、年龄感、肤色/发型、穿着、气质、镜头表达、自然口播状态。
- `[场景高精度扩写描述]`：包含背景类型、光线氛围、材质感、品牌广告语境，但必须极简干净。
- `[画幅参数]`：根据用户尺寸转写，例如 `--ar 9:16`、`--ar 1:1`、`--ar 16:9`。
- `[视频画幅描述]`：例如 `vertical 9:16 composition`、`square 1:1 composition`、`horizontal 16:9 composition`。

## 构图净化固定句

所有 Prompt 必须包含：

```text
Clean, completely uncluttered background without any background characters, extraneous props, or columns.
```

所有口播阶段必须包含：

```text
Focus strictly concentrated on the subject's face.
```

## 动态表情固定句

所有人物与视频 Prompt 必须按语境加入：

```text
Natural KOL speaking energy, expressive eyes, subtle blinking, relaxed shoulders, gentle breathing, slight head movements, responsive eyebrows, varied mouth shapes, confident but authentic delivery.
```

视频 Prompt 必须额外加入：

```text
Moderate speaking pace with tiny natural pauses and emphasis, not robotic, not stiff, not frozen.
```

## Step 1: Midjourney 纯口播首帧垫图 Prompt 模板

用途：生成演员定妆首帧。此图只负责前 3 秒纯口播状态，绝对不能出现手机。

```text
Medium shot, [人物高精度扩写描述], speaking directly to the camera in a lively mid-sentence expression. Natural KOL speaking energy, expressive eyes, subtle blinking impression, relaxed shoulders, gentle breathing posture, slight head movement feeling, responsive eyebrows, varied mouth shapes, confident but authentic delivery. Focus strictly concentrated on the subject's face, highly detailed facial expressions. Situated in [场景高精度扩写描述]. Clean, completely uncluttered background without any background characters, extraneous props, or columns. No smartphone, no object in hands, no raised hand blocking the face. Warm ambient lighting, photorealistic, 8k, cinematic lighting, shot on 35mm lens [画幅参数] --style raw --v 6.0
```

## Step 2: Midjourney 举绿幕手机垫图 Prompt 模板

用途：新增一张人物拿着绿幕手机的过渡垫图，方便后续视频模型锁定手机出现后的构图和纯绿屏区域。

```text
Medium close-up shot, [人物高精度扩写描述], naturally and confidently holding a modern smartphone up toward the camera in the foreground, as if presenting it during a live KOL ad read. The smartphone screen is completely solid bright chroma key green, flat and evenly lit, with no icons, no reflections, no text, no patterns. The phone is clearly visible but does not fully cover the subject's face; the subject's eyes and facial expression remain visible, lively, and engaging. Natural KOL speaking energy, expressive eyes, subtle blinking impression, relaxed shoulders, gentle breathing posture, slight head movement feeling, responsive eyebrows, varied mouth shapes, confident but authentic delivery. Situated in [场景高精度扩写描述]. Clean, completely uncluttered background without any background characters, extraneous props, or columns. Balanced focus between the subject's expressive face and the green smartphone screen, clean advertising composition. Warm ambient lighting, photorealistic, 8k, cinematic lighting, shot on 35mm lens [画幅参数] --style raw --v 6.0
```

## Step 3: 视频大模型直出 Prompt 模板

用途：用 Step 1 或 Step 2 垫图生成完整动态视频，强化动作演进、表情灵动和焦点转移。

```text
[人物高精度扩写描述], situated in [场景高精度扩写描述]. [视频画幅描述]. Clean, completely uncluttered background without any background characters, extraneous props, or columns. The video starts with a clear medium shot of the subject speaking passionately and naturally directly to the camera for the first few seconds, focus sharply and strictly concentrated on their face. Natural KOL speaking energy, expressive eyes, subtle blinking, gentle breathing, relaxed shoulders, slight head movements, responsive eyebrows, varied mouth shapes, and confident authentic delivery. The speaking pace is moderate, with tiny natural pauses and emphasis, not robotic, not stiff, not frozen.

After the first few seconds, the subject confidently lifts a modern smartphone from below the frame into the foreground toward the camera lens in one smooth natural motion. The movement feels human, coordinated with the speech rhythm, with a small shift of posture and hand energy. The smartphone screen is completely solid, bright chroma key green, evenly lit, with no icons, no text, no reflections, and no patterns.

As the phone enters the frame, a cinematic rack focus seamlessly occurs: the camera focus shifts dynamically from the subject's expressive face to the green smartphone screen. The chroma green screen becomes incredibly sharp and stable, while the subject's face and the background smoothly transition into a beautifully blurred shallow depth of field (bokeh). High quality, photorealistic, 8k resolution, cinematic lighting, realistic motion, shot on 35mm lens.
```

## 视频 Negative Prompt 建议

```text
stiff expression, robotic delivery, dead eyes, frozen face, frozen body, awkward hand motion, jittery phone, phone covering entire face, text on green screen, icons on screen, reflections on screen, background characters, extra people, columns, cluttered props, messy background, distorted hands, extra fingers, warped phone, low quality, overexposed green screen
```
