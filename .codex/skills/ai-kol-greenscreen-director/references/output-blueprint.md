# 输出蓝图

当用户输入符合 `生成KOL：[人物] + [场景] + [尺寸]` 后，直接生成两张垫图图片。第二张必须基于第一张生成，保证人物和场景一致。视频默认约 30 秒。

## 标准输出结构

```text
🎬 镜头设定解析 (Scene Configuration)

人物与构图：[中文扩写。强调脸部清晰、自然口播、背景干净。]
场景与光影：[中文扩写。简洁、有广告质感。]
画幅与时长：[尺寸 -> --ar 参数；默认 30 秒。]
足球 App 卖点：[首发阵容、阵型分析、END / Delayed / ABD / CAN、最多关注 5 支球队和 5 项赛事/联赛、定制比分首页。]
时间轴：[0-10s 足球话题/痛点铺垫] -> [10s 后转入资讯 App] -> [举起绿幕手机] -> [rack focus 到绿屏手机]。

🖼️ 第一步：Midjourney 纯口播首帧垫图 (Step 1: First Frame)
[套用 Step 1 模板，并直接生成图片：first-frame.png。]

📱 第二步：Midjourney 举绿幕手机垫图 (Step 2: Phone Reference Frame)
[以 first-frame.png 为主参考图，套用 Step 2 模板生成 phone-reference.png。必须保持同一人物、同一球衣、同一场景和同一光影。手机必须占画面约 70%，绿屏手机清晰锐利，人物和背景明显虚化。]

🎥 第三步：Kling / Runway 视频动作 Prompt (Step 3: I2V Motion Prompt)
[套用 Step 3 模板。]

🗣️ 第四步：足球 App 口播稿 (Step 4: Voiceover Script)
[输出约 30 秒口播稿。前 10 秒先讲足球观赛痛点/比赛日情绪；10 秒后再转入资讯 App 功能介绍，不删核心卖点。]

🚫 Negative Prompt / 避免项
[输出精简 Negative Prompt。]

💾 本地保存 (Local Save)
[保存 director-plan.md、first-frame.png、phone-reference.png。优先保存到 ~/Desktop/ai-kol-greenscreen-director/[本次子文件夹]/；云端环境同时保存到 outputs/ai-kol-greenscreen-director/[本次子文件夹]/，并在聊天里直接展示图片。]
```

## 输出要求

- 四步都要输出。
- 默认直接生成两张垫图图片，不只给 Prompt。
- 第二张图必须基于第一张图生成，保证人物和场景一致。
- 第二张图手机必须占画面约 70%，人物和背景必须虚化。
- 绿幕手机屏幕只允许纯绿色。
- 不要添加 app logo、角标、贴标或额外品牌图标。
- 口播默认 30 秒，前 10 秒铺垫，10 秒后介绍 App。
- 保留足球 App 核心卖点。
- 最后必须给出保存路径。
