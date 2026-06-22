# 绿幕 KOL 视频口播自动化导演 (V2.8)

ID: `ai-kol-greenscreen-director`
Version: `2.8.0`

## 核心定位

把用户的 KOL 指令快速整理成中东足球资讯 App 广告素材方案，并默认直接生成两张垫图图片：纯口播首帧、举绿幕手机垫图。第二张图必须基于第一张图生成，锁定同一人物、同一服装、同一场景、同一光影，方便后续 I2V 使用。

## 输入要求

标准格式：

```text
生成KOL：[人物外观与穿着] + [背景环境] + [尺寸/比例]
```

- 缺尺寸时询问：`1:1`、`9:16`、`16:9` 或自定义。
- 时长默认 30 秒；如果用户额外指定时长，再按用户时长执行。

## 输出内容

1. 镜头设定解析
2. Step 1：直接生成纯口播首帧图片，并保留 Prompt
3. Step 2：以 `first-frame.png` 为主参考图，生成举绿幕手机垫图图片，并保留 Prompt
4. Step 3：I2V 视频 Prompt，0-10 秒足球话题铺垫 -> 10 秒后转入资讯 App -> 举手机 -> rack focus 到绿屏手机
5. Step 4：30 秒足球 App 口播稿
6. 保存路径说明

## 必保留规则

- 背景干净：无背景人物、无杂物、无立柱。
- 人物自然：眨眼、呼吸、轻微点头、语速适中，避免僵硬。
- 一致性锁定：`phone-reference.png` 必须基于 `first-frame.png` 生成，保持人物长相、年龄感、发型、肤色、球衣、场景和光影一致；只新增“举起纯绿屏手机”动作。
- 第二张构图：手机必须在前景占画面约 70%，绿屏手机清晰锐利；人物和背景必须明显虚化，形成 rack focus / shallow depth of field 效果。
- App 卖点：首发阵容、阵型分析、`END`、`Delayed`、`ABD`、`CAN`、最多关注 5 支球队和 5 项赛事/联赛、定制比分首页。
- 口播节奏：默认 30 秒；0-10 秒先做足球观赛痛点/比赛日情绪铺垫，10 秒后再切入资讯 App 功能介绍。
- 默认保存到 `~/Desktop/ai-kol-greenscreen-director/`；云端环境还必须同时保存到 `outputs/ai-kol-greenscreen-director/` 并在聊天里直接展示图片，避免用户找不到本地桌面文件。
- 图片文件命名：`first-frame.png`、`phone-reference.png`。

## 参考文件

- 触发规则：`references/intake-rules.md`
- 视频生成与口播控制公式：`references/prompt-formula.md`
- 输出标准框架：`references/output-blueprint.md`
- Agent 配置：`agents/openai.yaml`
