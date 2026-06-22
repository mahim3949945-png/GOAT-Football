# 核心输出蓝图 (Blueprint)

当用户输入符合 `生成KOL：[人物] + [场景] + [尺寸] + [15秒/30秒]`，并提供足球 App logo 后，严格按以下结构输出。

## 缺少尺寸时

如果没有检测到尺寸或比例，只输出：

```text
请补充本次图片/视频画幅尺寸：1:1、9:16、16:9，或告诉我其他自定义比例。
```

## 缺少时长时

如果没有检测到视频时长，只输出：

```text
请问本次视频要生成 15 秒还是 30 秒？
```

## 缺少 Logo 时

如果没有检测到足球 App logo 附件，只输出：

```text
请上传足球 App logo，或确认本次不使用 logo。
```

## 多个关键信息缺失时

如果尺寸、时长或 logo 中有多个同时缺失，只输出：

```text
为了生成完整的两张垫图和视频 Prompt，请补充：画幅尺寸（1:1、9:16、16:9 或自定义）、视频时长（15秒或30秒），并上传足球 App logo（或确认不使用 logo）。
```

## 标准输出结构

```text
🎬 镜头设定解析 (Scene Configuration)

人物与构图 (Character & Composition)：
[扩写中文描述。必须强调：人物面部是绝对视觉中心；口播阶段面部清晰；人物表情自然灵动，有眨眼、轻微点头、眉眼反应、自然嘴型变化和呼吸感；背景无杂物、无人物、无立柱。]

场景与光影 (Atmosphere)：
[扩写中文场景布置、材质、光线氛围。必须保持干净、极简、有广告质感，不能出现背景人物、杂乱道具或立柱。]

画幅设置 (Aspect Ratio)：
[输出用户指定尺寸，并说明对应 Midjourney 参数，例如：9:16 -> --ar 9:16。]

视频时长 (Duration)：
[输出用户指定时长：15秒或30秒，并说明口播稿将按该时长控制信息密度和语速。]

Logo 使用 (Logo Integration)：
[说明已将用户上传的足球 App logo 作为前两张 Midjourney 垫图的图像参考。Logo 只能作为角标、胸前小贴标、桌面小立牌或背景小屏幕等干净品牌元素出现，不能放在纯绿手机屏幕上，不能遮挡人物面部。]

足球 App 卖点 (Football App Selling Points)：
[用中文概括本次广告必须口播介绍：中东足球资讯 App；赛前首发阵容；阵型分析；实时比赛事件和状态 END、Delayed、ABD、CAN；自由搜索并关注最多 5 支球队和 5 项赛事/联赛；定制个人比分首页。]

时间轴动作流 (Timeline)：
[0-3s：面部清晰纯口播，语速适中，有自然停顿和重音，开始介绍足球 App 核心价值] -> [3s+：人物顺滑举起纯绿屏手机，动作配合口播节奏] -> [结尾：Rack focus 转移到手机绿屏，人物和背景进入柔和虚化，口播完成 15秒或30秒卖点闭环]。

🖼️ 第一步：Midjourney 纯口播首帧垫图 (Step 1: First Frame)
(先用此 Prompt 生成演员定妆图。要求绝对干净的背景，不能举起手机，不能让手或道具抢焦点，焦点全部集中在脸上；同时把用户上传的 App logo 作为干净品牌元素带入画面。)

[严格套用 references/prompt-formula.md 中 Step 1 模板生成，替换人物、场景、画幅参数、App logo 图像参考和 Logo 露出描述。]

📱 第二步：Midjourney 举绿幕手机垫图 (Step 2: Phone Reference Frame)
(新增此 Prompt 生成“人物已经举起绿幕手机”的垫图。手机屏幕必须是纯净明亮的 chroma key green，方便后期抠像或 I2V 模型锁定手机区域；手机不能完全遮挡脸，人物仍然要有灵动表情；App logo 只能出现在手机屏幕以外的位置。)

[严格套用 references/prompt-formula.md 中 Step 2 模板生成，替换人物、场景、画幅参数、App logo 图像参考和 Logo 露出描述。]

🎥 第三步：Kling / Runway 视频动作 Prompt (Step 3: I2V Motion Prompt)
(用此 Prompt 生成动态视频。重点控制前几秒纯口播、中途举手机、最后焦点转移，并按用户选择控制 15秒或30秒节奏。)

[严格套用 references/prompt-formula.md 中 Step 3 模板生成，替换人物、场景、视频画幅描述和时长。]

🗣️ 第四步：足球 App 口播稿 (Step 4: Voiceover Script)
(根据用户选择输出 15秒或30秒版本。脚本必须围绕中东足球资讯 App，包含赛前首发阵容、阵型分析、END / Delayed / ABD / CAN 状态、最多关注 5 支球队和 5 项赛事/联赛、定制个人比分首页。)

[严格套用 references/prompt-formula.md 中 Step 4 模板，并可根据人物气质轻微调整语气，但不得删除核心卖点。]

🚫 Negative Prompt / 避免项

[输出 references/prompt-formula.md 中的视频 Negative Prompt，并可根据具体人物或场景补充。]
```

## 输出要求

- 不要省略第二步“举绿幕手机垫图”。
- 不要省略第四步“足球 App 口播稿”。
- 第一步必须明确 `No smartphone`。
- 第二步必须明确手机屏幕为 `completely solid bright chroma key green`。
- Step 1 和 Step 2 必须连带用户上传的 App logo 一起生成，但 Step 2 的纯绿手机屏幕上不能出现 logo。
- 第三步必须明确 `rack focus`，并说明焦点从人脸转移到手机绿屏。
- 如果用户没有指定时长，必须先问 15秒还是30秒。
- 口播稿必须包含：首发阵容、阵型分析、END、Delayed、ABD、CAN、最多关注 5 支球队、最多关注 5 项赛事/联赛、定制个人比分首页。
- 所有步骤都必须保持背景干净：无背景人物、无杂乱道具、无立柱。
- 所有视频动作描述都必须避免僵硬感，加入自然口播表情、呼吸、眨眼、轻微头部动作和适中语速。
