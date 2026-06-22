# I2V Prompt 公式

通用要求：背景干净、无背景人物、无杂物、无立柱；人物自然口播，有眨眼、呼吸和轻微点头；不要添加 app logo、角标、贴标或额外品牌图标。Step 2 必须基于 Step 1 的 `first-frame.png` 生成，保持人物和场景一致；手机占画面约 70%，手机清晰，人物和背景虚化。

## Step 1: Midjourney 纯口播首帧垫图 Prompt 模板

生成图片文件名：`first-frame.png`

```text
Medium shot, [人物扩写], speaking directly to camera for a Middle East football app ad. Natural KOL energy, expressive eyes, subtle blinking, relaxed breathing, slight head movement. Face in sharp focus. [场景扩写], clean uncluttered background, no background characters, no props, no columns. No app logo, no corner logo, no brand sticker, no smartphone, no object in hands. Photorealistic, cinematic lighting, 8k [画幅参数] --style raw --v 6.0
```

## Step 2: Midjourney 举绿幕手机垫图 Prompt 模板

生成图片文件名：`phone-reference.png`

主参考图：`first-frame.png`

```text
[Use first-frame.png as the primary image reference] Keep the exact same person, face, age, hairstyle, skin tone, outfit, Real Madrid jersey, lighting, futuristic esports room, and clean background from the reference image. Only change the action and focus: the subject holds a modern smartphone very close to the camera in the foreground. The smartphone occupies about 70% of the frame and is the sharpest object. The phone screen is solid bright chroma key green, no icons, no text, no reflections, no logo. The subject remains behind the phone and becomes visibly blurred; the background also becomes blurred bokeh, cinematic rack focus / shallow depth of field. No app logo, no corner logo, no brand sticker, no new background objects, no new people, no columns. Photorealistic, cinematic lighting, 8k [画幅参数] --style raw --v 6.0
```

## Step 3: 视频大模型直出 Prompt 模板

```text
[人物扩写] in [场景扩写], [视频画幅描述], 30 seconds. Middle East football app ad. Clean background, no background characters, no props, no columns, no app logo. 0-10s: clear face-focused KOL speaking naturally about match-day football pain points and excitement, with blinking, breathing, slight head movement, moderate pace. After 10s: the subject transitions into introducing the football information app and smoothly lifts a smartphone from below frame. Phone screen is solid bright chroma key green. Rack focus shifts from face to green phone screen; face and background become soft bokeh. Photorealistic, cinematic, realistic motion.
```

## Step 4: 足球 App 口播稿模板

### 30 秒默认结构

```text
First 10 seconds:
Every match day, the hardest part is keeping up before kickoff. Who is starting? What formation are they using? Is the match live, delayed, cancelled, or already finished? If you follow more than one team, it gets messy fast.

After 10 seconds:
That is why this football app makes it simple. Check starting lineups, formation analysis, and real-time match statuses like END, Delayed, ABD, and CAN. Search and follow up to five favorite teams plus five leagues or competitions, then customize your own live scores homepage around the matches you care about.
```

### 30 秒压缩口播版

```text
Match day moves fast. Before kickoff, you need to know who is starting, what formation they are using, and whether the match is live, delayed, cancelled, abandoned, or already finished. After the first look, this football app keeps everything clear: starting lineups, formation analysis, real-time statuses like END, Delayed, ABD, and CAN, plus your own custom scores homepage. Follow up to five favorite teams and five competitions, and only see the matches you care about.
```

## 视频 Negative Prompt 建议

```text
stiff expression, robotic delivery, dead eyes, frozen face, awkward hand motion, phone covering entire face, text/icons/logo on green screen, reflections on green screen, app logo, corner logo, brand sticker, background characters, columns, cluttered props, distorted hands, warped phone, low quality
```
