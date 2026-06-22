# I2V 视频生成与口播控制公式

The I2V Timeline, Focus & Voiceover Formula

## 全局变量

- `[人物高精度扩写描述]`：包含外观、年龄感、肤色/发型、穿着、气质、镜头表达、自然口播状态。
- `[场景高精度扩写描述]`：包含背景类型、光线氛围、材质感、品牌广告语境，但必须极简干净。
- `[画幅参数]`：根据用户尺寸转写，例如 `--ar 9:16`、`--ar 1:1`、`--ar 16:9`。
- `[视频画幅描述]`：例如 `vertical 9:16 composition`、`square 1:1 composition`、`horizontal 16:9 composition`。
- `[时长]`：仅支持 `15 seconds` 或 `30 seconds`。
- `[App logo 图像参考]`：用户随指令上传的足球 App logo。生成前两张垫图时必须作为 image reference 使用。
- `[Logo 露出描述]`：把 App logo 以自然、干净、不喧宾夺主的方式植入画面，例如 small branded corner badge、subtle logo sticker on the shirt、minimal desk card、small clean wall display。不得放在纯绿手机屏幕上。

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

## 足球 App 固定卖点

所有口播稿必须围绕推广中东地区足球资讯 App 展开，并覆盖：

- 赛前：查看首发阵容、阵型分析。
- 赛中/赛后：实时事件与比赛状态，包括完赛 `END`、推迟 `Delayed`、腰斩 `ABD`、取消 `CAN`。
- 个性化关注：自由搜索并一键关注球队，最多 5 支；关注赛事/联赛，最多 5 项。
- 定制首页：根据关注项定制个人比分首页，快速看到自己关心的比赛。

## Logo 使用规则

- Step 1 与 Step 2 两张 Midjourney 垫图必须连带用户上传的 App logo 一起生成。
- Logo 应作为品牌元素出现在画面里，例如角标、衣服小贴标、桌面小立牌、干净背景屏幕上的小 logo。
- Logo 不能覆盖人物面部，不能制造背景杂乱。
- Step 2 的手机屏幕必须保持纯绿色 chroma key green，不能出现 logo、文字、图标或反光。

## Step 1: Midjourney 纯口播首帧垫图 Prompt 模板

用途：生成演员定妆首帧。此图只负责前 3 秒纯口播状态，绝对不能出现手机。

```text
[App logo 图像参考] Medium shot, [人物高精度扩写描述], speaking directly to the camera in a lively mid-sentence expression for a Middle East football app advertisement. Natural KOL speaking energy, expressive eyes, subtle blinking impression, relaxed shoulders, gentle breathing posture, slight head movement feeling, responsive eyebrows, varied mouth shapes, confident but authentic delivery. Focus strictly concentrated on the subject's face, highly detailed facial expressions. Situated in [场景高精度扩写描述]. [Logo 露出描述], clean and subtle, visible as football app branding but not distracting. Clean, completely uncluttered background without any background characters, extraneous props, or columns. No smartphone, no object in hands, no raised hand blocking the face. Warm ambient lighting, photorealistic, 8k, cinematic lighting, shot on 35mm lens [画幅参数] --style raw --v 6.0
```

## Step 2: Midjourney 举绿幕手机垫图 Prompt 模板

用途：新增一张人物拿着绿幕手机的过渡垫图，方便后续视频模型锁定手机出现后的构图和纯绿屏区域。

```text
[App logo 图像参考] Medium close-up shot, [人物高精度扩写描述], naturally and confidently holding a modern smartphone up toward the camera in the foreground, as if presenting it during a live KOL ad read for a Middle East football app. The smartphone screen is completely solid bright chroma key green, flat and evenly lit, with no icons, no reflections, no text, no patterns, and no logo on the green screen. The phone is clearly visible but does not fully cover the subject's face; the subject's eyes and facial expression remain visible, lively, and engaging. [Logo 露出描述], visible outside the phone screen as subtle football app branding. Natural KOL speaking energy, expressive eyes, subtle blinking impression, relaxed shoulders, gentle breathing posture, slight head movement feeling, responsive eyebrows, varied mouth shapes, confident but authentic delivery. Situated in [场景高精度扩写描述]. Clean, completely uncluttered background without any background characters, extraneous props, or columns. Balanced focus between the subject's expressive face and the green smartphone screen, clean advertising composition. Warm ambient lighting, photorealistic, 8k, cinematic lighting, shot on 35mm lens [画幅参数] --style raw --v 6.0
```

## Step 3: 视频大模型直出 Prompt 模板

用途：用 Step 1 或 Step 2 垫图生成完整动态视频，强化动作演进、表情灵动和焦点转移。

```text
[人物高精度扩写描述], situated in [场景高精度扩写描述]. [视频画幅描述], [时长]. This is a Middle East football app advertisement. Clean, completely uncluttered background without any background characters, extraneous props, or columns. The video starts with a clear medium shot of the subject speaking passionately and naturally directly to the camera for the first few seconds, focus sharply and strictly concentrated on their face. Natural KOL speaking energy, expressive eyes, subtle blinking, gentle breathing, relaxed shoulders, slight head movements, responsive eyebrows, varied mouth shapes, and confident authentic delivery. The speaking pace is moderate, with tiny natural pauses and emphasis, not robotic, not stiff, not frozen.

The subject's mouth movements should match a concise football app promotion script: check pre-match starting lineups, analyze formations, follow live match events and statuses like END, Delayed, ABD, and CAN, search and follow up to five favorite teams and up to five leagues or competitions, and customize a personal live scores homepage.

After the first few seconds, the subject confidently lifts a modern smartphone from below the frame into the foreground toward the camera lens in one smooth natural motion. The movement feels human, coordinated with the speech rhythm, with a small shift of posture and hand energy. The smartphone screen is completely solid, bright chroma key green, evenly lit, with no icons, no text, no reflections, no logo, and no patterns.

As the phone enters the frame, a cinematic rack focus seamlessly occurs: the camera focus shifts dynamically from the subject's expressive face to the green smartphone screen. The chroma green screen becomes incredibly sharp and stable, while the subject's face and the background smoothly transition into a beautifully blurred shallow depth of field (bokeh). High quality, photorealistic, 8k resolution, cinematic lighting, realistic motion, shot on 35mm lens.
```

## Step 4: 足球 App 口播稿模板

### 15 秒版本

```text
If you follow football in the Middle East, this app keeps everything clear before kickoff and during the match. Check starting lineups, formation analysis, and live statuses like END, Delayed, ABD, or CAN. Follow up to five favorite teams and five competitions, then build your own live scores homepage.
```

### 30 秒版本

```text
For football fans in the Middle East, this app makes match day easier. Before kickoff, you can check confirmed starting lineups and understand the formation analysis at a glance. During the match, follow real-time events and clear status labels, including END for full time, Delayed for postponed matches, ABD for abandoned games, and CAN for cancelled fixtures. Search your favorite clubs and competitions, follow up to five teams and five leagues or tournaments, and customize a personal scores homepage focused only on the matches you care about.
```

## 视频 Negative Prompt 建议

```text
stiff expression, robotic delivery, dead eyes, frozen face, frozen body, awkward hand motion, jittery phone, phone covering entire face, text on green screen, icons on screen, reflections on screen, background characters, extra people, columns, cluttered props, messy background, distorted hands, extra fingers, warped phone, low quality, overexposed green screen
```
