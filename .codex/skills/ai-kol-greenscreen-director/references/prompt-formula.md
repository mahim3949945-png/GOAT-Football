# I2V Prompt 公式

通用要求：背景干净、无背景人物、无杂物、无立柱；人物自然口播，有眨眼、呼吸和轻微点头；logo 只做轻量品牌露出，不放在绿幕手机屏幕上。

## Step 1: Midjourney 纯口播首帧垫图 Prompt 模板

```text
[App logo image reference] Medium shot, [人物扩写], speaking directly to camera for a Middle East football app ad. Natural KOL energy, expressive eyes, subtle blinking, relaxed breathing, slight head movement. Face in sharp focus. [场景扩写], clean uncluttered background, no background characters, no props, no columns. Subtle app logo branding outside the face area. No smartphone, no object in hands. Photorealistic, cinematic lighting, 8k [画幅参数] --style raw --v 6.0
```

## Step 2: Midjourney 举绿幕手机垫图 Prompt 模板

```text
[App logo image reference] Medium close-up shot, [人物扩写], naturally holding a modern smartphone toward the camera. The phone screen is solid bright chroma key green, no icons, no text, no reflections, no logo. Phone does not fully cover the face; eyes and expression remain visible. Subtle app logo branding outside the phone screen. [场景扩写], clean uncluttered background, no background characters, no props, no columns. Photorealistic, cinematic lighting, 8k [画幅参数] --style raw --v 6.0
```

## Step 3: 视频大模型直出 Prompt 模板

```text
[人物扩写] in [场景扩写], [视频画幅描述], [时长]. Middle East football app ad. Clean background, no background characters, no props, no columns. First seconds: clear face-focused KOL speaking, natural blinking, breathing, slight head movement, moderate pace. Then the subject smoothly lifts a smartphone from below frame. Phone screen is solid bright chroma key green. Rack focus shifts from face to green phone screen; face and background become soft bokeh. Photorealistic, cinematic, realistic motion.
```

## Step 4: 足球 App 口播稿模板

### 15 秒

```text
Follow football in the Middle East with one app. Check starting lineups, formation analysis, and live statuses like END, Delayed, ABD, or CAN. Follow up to five teams and five competitions, then build your own live scores homepage.
```

### 30 秒

```text
For football fans in the Middle East, this app makes match day simple. Before kickoff, check starting lineups and formation analysis. During the match, follow real-time events and clear status labels: END, Delayed, ABD, and CAN. Search and follow up to five favorite teams plus five leagues or competitions, then customize a live scores homepage focused only on what you care about.
```

## 视频 Negative Prompt 建议

```text
stiff expression, robotic delivery, dead eyes, frozen face, awkward hand motion, phone covering face, text/icons/logo on green screen, reflections on green screen, background characters, columns, cluttered props, distorted hands, warped phone, low quality
```
