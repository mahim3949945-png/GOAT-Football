# 输出蓝图

当用户输入符合 `生成KOL：[人物] + [场景] + [尺寸] + [15秒/30秒]`，并提供足球 App logo 后，直接生成两张垫图图片。第二张必须基于第一张生成，保证人物和场景一致。

## 标准输出结构

```text
🎬 镜头设定解析 (Scene Configuration)

人物与构图：[中文扩写。强调脸部清晰、自然口播、背景干净。]
场景与光影：[中文扩写。简洁、有广告质感。]
画幅与时长：[尺寸 -> --ar 参数；15秒或30秒。]
Logo 使用：[说明 logo 出现在画面品牌位，不放在绿幕手机屏幕上。]
足球 App 卖点：[首发阵容、阵型分析、END / Delayed / ABD / CAN、最多关注 5 支球队和 5 项赛事/联赛、定制比分首页。]
时间轴：[0-3s 纯口播] -> [举起绿幕手机] -> [rack focus 到绿屏手机]。

🖼️ 第一步：Midjourney 纯口播首帧垫图 (Step 1: First Frame)
[套用 Step 1 模板，并直接生成图片：first-frame.png。]

📱 第二步：Midjourney 举绿幕手机垫图 (Step 2: Phone Reference Frame)
[以 first-frame.png 为主参考图，套用 Step 2 模板生成 phone-reference.png。必须保持同一人物、同一球衣、同一场景、同一光影和同一左上角 logo 位置。手机必须占画面约 70%，绿屏手机清晰锐利，人物和背景明显虚化。]

🎥 第三步：Kling / Runway 视频动作 Prompt (Step 3: I2V Motion Prompt)
[套用 Step 3 模板。]

🗣️ 第四步：足球 App 口播稿 (Step 4: Voiceover Script)
[按 15秒或30秒输出，不删核心卖点。]

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
- logo 不能放在绿幕手机屏幕上。
- 保留足球 App 核心卖点。
- 最后必须给出保存路径。
