# 绿幕 KOL 视频口播自动化导演 (V2.5)

ID: `ai-kol-greenscreen-director`
Version: `2.5.0`

## 核心定位

把用户的 KOL 指令快速整理成中东足球资讯 App 广告素材方案，并默认直接生成两张垫图图片：纯口播首帧、举绿幕手机垫图。同时输出 I2V 视频 Prompt 和 15 秒或 30 秒口播稿。

## 输入要求

标准格式：

```text
生成KOL：[人物外观与穿着] + [背景环境] + [尺寸/比例] + [15秒/30秒]
```

- 必须带 App logo 附件；没有则询问是否补传或不使用。
- 缺尺寸时询问：`1:1`、`9:16`、`16:9` 或自定义。
- 缺时长时询问：`15秒` 还是 `30秒`。

## 输出内容

1. 镜头设定解析
2. Step 1：直接生成纯口播首帧图片，并保留 Prompt
3. Step 2：直接生成举绿幕手机垫图图片，并保留 Prompt
4. Step 3：I2V 视频 Prompt，清晰口播 -> 举手机 -> rack focus 到绿屏手机
5. Step 4：足球 App 口播稿
6. 保存路径说明

## 必保留规则

- 背景干净：无背景人物、无杂物、无立柱。
- 人物自然：眨眼、呼吸、轻微点头、语速适中，避免僵硬。
- App 卖点：首发阵容、阵型分析、`END`、`Delayed`、`ABD`、`CAN`、最多关注 5 支球队和 5 项赛事/联赛、定制比分首页。
- 默认保存到 `~/Desktop/ai-kol-greenscreen-director/`；无法访问桌面时保存到 `outputs/ai-kol-greenscreen-director/`。
- 图片文件命名：`first-frame.png`、`phone-reference.png`。

## 参考文件

- 触发规则：`references/intake-rules.md`
- 视频生成与口播控制公式：`references/prompt-formula.md`
- 输出标准框架：`references/output-blueprint.md`
- Agent 配置：`agents/openai.yaml`
