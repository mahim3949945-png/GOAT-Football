# I2V 时间轴与焦点控制公式

本公式用于生成标准化 Prompt。生成时应先把用户输入的【人物】和【场景】扩写为具备摄影细节、投放质感、真人口播灵动感、足球 App 推广语境和明确视觉边界的描述，再填入模板。

## 产品语境

默认推广产品是**面向中东地区球迷的足球资讯 App**。

如果用户没有提供 App 名称，口播稿中使用 `[App名称]` 占位。如果用户提供 App 名称，所有口播稿与 Prompt 都替换为真实名称。

## 时长控制

每次任务必须明确视频时长，只允许：

- `15秒`
- `30秒`

如果用户没有提供时长，先追问时长，不要生成口播稿、图片或视频 Prompt。

### 15 秒节奏

- 口播稿：3-4 句，强 Hook，快速讲 2 个核心卖点，结尾 CTA。
- 视频动作：`0-3s` 清晰人脸纯口播 -> `3-5s` 举起绿幕手机 -> `5-15s` rack focus 到手机，手机屏幕清晰，人物和背景虚化。

### 30 秒节奏

- 口播稿：5-7 句，可以加入更多痛点、使用场景、3-4 个卖点和更明确 CTA。
- 视频动作：`0-5s` 清晰人脸 Hook -> `5-15s` 继续口播解释 App 价值，仍不出现手机 -> `15-18s` 举起绿幕手机 -> `18-30s` rack focus 到手机，手机屏幕清晰，人物和背景虚化。

### 默认卖点池

生成口播稿时从以下卖点中选择 2-3 个，不要一次塞满：

- 最新足球新闻和热门话题。
- 比赛赛程提醒。
- 实时比分 / 比分动态。
- 转会消息。
- 中东球迷关心的球队与球星资讯。
- 重要比赛前后的快速更新。
- 打开 App 即可快速了解今天最重要的足球消息。

### 禁止承诺

不要承诺：

- 官方独家版权，除非用户明确提供。
- 免费看全部赛事直播。
- 博彩、中奖、送彩金或 guaranteed winnings。
- 任何无法由普通资讯 App 支撑的功能。

## 扩写原则

### 人物扩写

人物描述应包含：

- 年龄段、地域 / 气质、发型、面部特征。
- 服装材质、颜色、版型。
- 口播状态：confident, energetic, speaking directly to the camera, authentic creator energy。
- 面部表现：lively eyes, clear facial expression, natural mouth movement, warm micro-smile, spontaneous mid-speech expression。
- 姿态表现：slight head tilt, relaxed shoulders, gentle forward lean, subtle asymmetrical posture, natural upper-body movement。
- 真人质感：natural skin texture, imperfect but attractive real-person details, candid social media presenter realism。
- 产品语境：speaking as a football fan creator, enthusiastically recommending a football news app for Middle Eastern fans。

不要扩写为夸张怪异、过度奇幻或遮挡面部的造型。避免墨镜、口罩、大帽檐、夸张手势遮脸。必须排除 stiff pose、frozen expression、mannequin-like、blank stare、over-posed portrait、plastic skin。

### 场景扩写

场景描述应包含：

- 空间类型与质感。
- 干净背景、浅层次布景、少量大色块。
- 柔和环境光、电影感补光。

无论用户输入什么场景，都必须净化为：

```text
clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions
```

## Promo Script: 中东足球资讯 App 推广口播稿公式

用途：生成可配音、可字幕、可给真人 KOL 参考的短口播稿。口播稿应与人物身份和场景气质匹配。

### 结构

```text
Hook: 用足球迷痛点开场，例如“还在到处刷比分和转会消息？”
Value: 介绍 [App名称] 如何帮助中东球迷快速看新闻、比分、赛程或转会动态。
CTA: 引导下载、打开、立即查看。
```

### 推荐长度

- 15 秒标准版：3-4 句。
- 30 秒扩展版：5-7 句。

### 中文口播模板

15 秒：

```text
如果你每天都在追足球新闻、比分和转会消息，一定要试试 [App名称]。这里能快速看到中东球迷关心的热门比赛、赛程动态和最新资讯。现在就打开 [App名称]，别错过今天最重要的足球消息。
```

30 秒：

```text
如果你每天都在追足球新闻、比分、赛程和转会消息，不要再到处切换平台了。打开 [App名称]，中东球迷关心的热门比赛、球队动态、球星新闻和关键赛程都能快速看到。无论是赛前看消息，还是赛后追比分更新，[App名称] 都能帮你更快掌握重点。现在就打开 [App名称]，把今天最重要的足球资讯一次看清楚。
```

### English / MENA-friendly Voiceover Template

15 seconds:

```text
If you follow football every day, you need [App Name]. Get the latest match updates, football news, fixtures, and transfer stories made for fans in the Middle East. Open [App Name] now and stay ahead of the game.
```

30 seconds:

```text
If you follow football every day, stop jumping between different apps for news, scores, fixtures, and transfer stories. With [App Name], fans in the Middle East can quickly catch the biggest football updates, trending matches, team news, and player stories in one place. Whether it is before kickoff or right after the match, [App Name] helps you stay updated faster. Open [App Name] now and stay ahead of the game.
```

### Arabic Placeholder Template

15 seconds:

```text
إذا كنت تتابع كرة القدم كل يوم، جرّب [App Name]. تابع آخر الأخبار، النتائج، المباريات، وانتقالات اللاعبين لعشاق كرة القدم في الشرق الأوسط. افتح [App Name] الآن ولا تفوّت أهم الأخبار.
```

30 seconds:

```text
إذا كنت تتابع كرة القدم يومياً، لا تضيع وقتك بين أكثر من تطبيق لمعرفة الأخبار والنتائج والمباريات والانتقالات. مع [App Name]، يمكن لعشاق كرة القدم في الشرق الأوسط متابعة أهم الأخبار، المباريات الرائجة، أخبار الفرق، وقصص اللاعبين بسرعة ومن مكان واحد. سواء قبل المباراة أو بعدها، يساعدك [App Name] على البقاء على اطلاع دائم. افتح [App Name] الآن ولا تفوّت أهم أخبار كرة القدم.
```

## Step 1: Midjourney 首帧垫图 Prompt 模板

用途：直接生成演员定妆和视频首帧。此阶段必须是纯口播画面，不允许手机提前出现。

```text
Medium shot, [人物高精度扩写描述], speaking directly to the camera like a real football fan creator promoting a football news app for Middle Eastern fans, authentic creator energy, lively eyes, natural mouth movement, subtle micro-expressions, slight head tilt, relaxed shoulders, gentle forward lean, spontaneous mid-speech expression. Focus strictly concentrated on the subject's face, highly detailed facial expressions, sharp eyes, clear facial features, natural skin texture. The presenter looks like they are naturally delivering an app recommendation about football news, match updates, fixtures, and transfer stories. Situated in [场景高精度扩写描述]. Clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions. The subject's hands stay naturally out of the foreground, no smartphone, no phone screen, no green screen, no handheld device visible. Warm ambient lighting, soft cinematic key light, candid high-end UGC football app ad style, photorealistic, 8k, cinematic lighting --ar 9:16 --style raw --v 6.0
```

### Step 1 Negative Prompt 建议

```text
background people, crowd, columns, poles, clutter, messy props, phone, smartphone, green screen, hand holding phone, face obstruction, sunglasses, mask, stiff pose, frozen expression, mannequin-like, blank stare, over-posed portrait, plastic skin, text, watermark, logo, low quality, distorted hands, extra fingers
```

## Step 2: Midjourney 拿手机展示图 Prompt 模板

用途：直接生成一张人物拿着绿幕手机的图片。此图用于终帧参考、展示姿势参考或素材扩展，**不得替代 Step 1 视频首帧**。

```text
Medium close-up, [人物高精度扩写描述], holding a modern smartphone naturally in one hand and presenting it toward the camera while recommending a football news app for Middle Eastern fans, authentic football fan creator energy, lively eyes, spontaneous mid-speech expression, relaxed shoulders, subtle head tilt, natural hand posture. The smartphone is in the foreground with its screen clearly visible, perfectly flat, completely solid, bright chroma key green, evenly lit, no UI, no text, no reflections, no patterns, no cracks, no black borders. The subject still feels like a real person speaking about football news, match updates, fixtures, and transfer stories, not a posed model. Situated in [场景高精度扩写描述]. Clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions. Cinematic rack-focus look, the green phone screen is crisp and prominent while the subject's expressive face remains recognizable with gentle natural softness, warm ambient lighting, soft cinematic key light, candid high-end UGC football app ad style, photorealistic, 8k, cinematic lighting --ar 9:16 --style raw --v 6.0
```

### Step 2 Negative Prompt 建议

```text
background people, crowd, columns, poles, clutter, messy props, stiff pose, frozen expression, mannequin-like, blank stare, over-posed portrait, plastic skin, face obstruction, sunglasses, mask, screen reflections, phone UI, text on phone, patterned screen, dark green screen, uneven green, black phone border dominating the screen, blurry phone screen, warped phone, distorted hands, extra fingers, watermark, logo, low quality
```

## Step 3: 视频大模型直出 Prompt 模板

用途：基于 Step 1 首帧生成动态视频。此阶段必须表现完整时间轴。

### 15 秒版本

```text
[人物高精度扩写描述], situated in [场景高精度扩写描述]. Clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions. 15-second vertical video. From 0-3 seconds, the video starts with a stable clear medium shot of the subject speaking passionately directly to the camera like a real football fan creator promoting a football news app for Middle Eastern fans, focus sharply and strictly concentrated on their face, lively eyes, natural mouth movement, spontaneous micro-expressions, slight head tilt, relaxed shoulders, gentle forward lean, direct eye contact, no smartphone visible at the beginning. From 3-5 seconds, the subject confidently lifts a modern smartphone from below the frame into the foreground toward the camera lens with natural hand motion, as if revealing the app download or app screen area for compositing. The smartphone screen is perfectly flat, completely solid, bright chroma key green, evenly lit, with no UI, no text, no reflections, no patterns, no cracks, and no black borders. From 5-15 seconds, a cinematic rack focus occurs smoothly: the camera focus shifts dynamically from the subject's face to the green smartphone screen. The green screen becomes extremely sharp and fills the viewer's attention, while the subject's expressive face and the clean background smoothly transition into a beautiful shallow-depth-of-field blur and soft bokeh. The subject should feel alive and conversational, not stiff, not mannequin-like, not over-posed. High quality, photorealistic, 8k resolution, cinematic lighting, realistic handheld micro-movement, shot on a 35mm lens, vertical 9:16 football app social media ad.
```

### 30 秒版本

```text
[人物高精度扩写描述], situated in [场景高精度扩写描述]. Clean, completely uncluttered background, no background characters, no extra people, no crowds, no extraneous props, no messy objects, no columns, no poles, no vertical obstructions. 30-second vertical video. From 0-5 seconds, the video starts with a stable clear medium shot of the subject delivering a strong football fan hook directly to the camera, focus sharply and strictly concentrated on their face, lively eyes, natural mouth movement, spontaneous micro-expressions, slight head tilt, relaxed shoulders, gentle forward lean, direct eye contact, no smartphone visible. From 5-15 seconds, the subject continues speaking naturally like a real football fan creator promoting a football news app for Middle Eastern fans, explaining the app value for football news, match updates, fixtures, transfer stories, and trending matches, still no smartphone visible, focus remains on the expressive face. From 15-18 seconds, the subject confidently lifts a modern smartphone from below the frame into the foreground toward the camera lens with natural hand motion, as if revealing the app download or app screen area for compositing. The smartphone screen is perfectly flat, completely solid, bright chroma key green, evenly lit, with no UI, no text, no reflections, no patterns, no cracks, and no black borders. From 18-30 seconds, a cinematic rack focus occurs smoothly: the camera focus shifts dynamically from the subject's face to the green smartphone screen. The green screen becomes extremely sharp and fills the viewer's attention, while the subject's expressive face and the clean background smoothly transition into a beautiful shallow-depth-of-field blur and soft bokeh. The subject should feel alive and conversational, not stiff, not mannequin-like, not over-posed. High quality, photorealistic, 8k resolution, cinematic lighting, realistic handheld micro-movement, shot on a 35mm lens, vertical 9:16 football app social media ad.
```

### Step 3 Negative Prompt 建议

```text
phone visible at start, early phone reveal, stiff pose, frozen expression, mannequin-like, blank stare, over-posed portrait, robotic movement, background characters, crowd, clutter, columns, poles, messy room, extra props, screen reflections, phone UI, text on phone, patterned screen, dark green screen, uneven green, face remains sharper than phone after rack focus, no focus shift, blurry phone, warped phone, extra fingers, distorted hands, watermark, subtitles
```

## 时间轴硬约束

```text
15s: 0-3s clear face-only talking head, no phone visible, focus locked on face -> 3-5s lift chroma green smartphone -> 5-15s rack focus to phone, phone sharp, face and background blurred
30s: 0-5s face-only hook, no phone visible -> 5-15s app value explanation, no phone visible -> 15-18s lift chroma green smartphone -> 18-30s rack focus to phone, phone sharp, face and background blurred
```

## 质量检查

输出前检查：

- 是否生成了围绕中东足球资讯 App 的口播稿。
- 是否先确认了 15 秒或 30 秒时长。
- 口播稿是否包含 Hook、App 价值点和 CTA。
- 口播稿长度是否匹配 15 秒或 30 秒。
- 是否避免了直播版权、博彩、中奖等未经授权承诺。
- Step 1 是否完全无手机。
- Step 1 是否直接生成图片。
- Step 1 是否加入了真人口播灵动感，而不是僵硬证件照。
- Step 2 是否是一张独立的拿手机展示图，且没有被当作视频首帧。
- Step 2 是否直接生成图片。
- Step 2 的手机屏幕是否为纯 chroma key green。
- Step 3 是否使用对应的 15 秒或 30 秒时间轴。
- Step 3 是否明确写出手机出现前无手机。
- 是否出现 rack focus。
- 是否明确手机屏幕为纯 chroma key green。
- 是否排除了 stiff pose、frozen expression、mannequin-like。
- 是否反复排除了背景人物、杂物、立柱。
- 是否保证前段人脸清晰、后段手机清晰。
