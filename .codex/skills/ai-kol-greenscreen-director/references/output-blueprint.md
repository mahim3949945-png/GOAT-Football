# 核心输出蓝图

当用户输入标准口令后，必须严格按以下结构输出。不要省略任一部分。

---

## 🎬 镜头设定解析 (Scene Configuration)

**人物与构图 (Character & Composition)：**  
[用中文扩写人物外观、服装、年龄气质、面部表现和画面构图。必须强调：中景、直视镜头、面部是唯一视觉中心、前 3 秒不出现手机、背景无人物、无杂物、无立柱。]

**真人口播表现 (Performance)：**  
[用中文说明人物要像真实 KOL 口播：眼神灵动、有自然微表情、轻微头部倾斜、肩颈放松、身体轻微前倾、嘴型处在真实说话中，避免僵硬摆拍、蜡像感、证件照感。]

**推广产品 (Product)：**  
[固定围绕“面向中东地区球迷的足球资讯 App”展开。如用户提供 App 名称，用真实名称；否则使用 `[App名称]` 占位。说明本条视频是在推荐 App 的足球新闻、比分动态、赛程、转会消息和热门比赛资讯。]

**场景与光影 (Atmosphere)：**  
[用中文扩写场景布置与灯光。必须把用户场景净化为干净、可控、低干扰的背景，强调柔和环境光、电影感补光、背景不抢焦。]

**时间轴动作流 (Timeline)：**  
`0-3s：人脸清晰，直视镜头纯口播，手机不出现` -> `3s+：人物从画面下方举起纯绿幕手机到镜头前景` -> `结尾：rack focus 从人脸切到手机屏幕，手机清晰，人脸与背景虚化`

---

## 🗣️ 推广口播稿 (App Promo Script)

> 此口播稿用于后期配音、字幕或真人 KOL 参考。文案必须围绕中东足球资讯 App，不要跑成泛足球闲聊。

**中文版本：**

```text
[生成 8-15 秒中文口播稿。结构：足球迷痛点 Hook -> [App名称] 的 2-3 个价值点 -> 下载 / 打开 CTA。]
```

**English / MENA-friendly Version：**

```text
[Generate an 8-15 second English voiceover for Middle Eastern football fans. Structure: hook -> app value -> CTA.]
```

**Arabic Placeholder Version：**

```text
[Generate an Arabic voiceover draft for Middle Eastern football fans. Keep it short, natural, and app-focused.]
```

---

## 🖼️ 第一步：Midjourney 纯口播首帧垫图 (Step 1: First Frame)

> 先用此 Prompt 生成演员定妆图 / 视频首帧。此图必须只有人物口播状态，不允许提前举起手机。

```text
[套用 references/prompt-formula.md 的 Step 1 模板，填入扩写后的人物与场景]
```

**Negative Prompt：**

```text
[套用 references/prompt-formula.md 的 Step 1 Negative Prompt 建议]
```

---

## 📱 第二步：Midjourney 拿手机展示图 (Step 2: Phone Holding Still)

> 额外用此 Prompt 生成一张人物拿着纯绿幕手机的图片。此图用于终帧参考、展示姿势参考或素材扩展，不能替代第一步视频首帧。

```text
[套用 references/prompt-formula.md 的 Step 2 模板，填入扩写后的人物与场景]
```

**Negative Prompt：**

```text
[套用 references/prompt-formula.md 的 Step 2 Negative Prompt 建议]
```

---

## 🎥 第三步：视频动作与焦点转移 Prompt (Step 3: I2V Motion)

> 将第一步生成的首帧图作为视频模型输入，再使用此 Prompt 控制动作与焦点转移。

```text
[套用 references/prompt-formula.md 的 Step 3 模板，填入扩写后的人物与场景]
```

**Negative Prompt：**

```text
[套用 references/prompt-formula.md 的 Step 3 Negative Prompt 建议]
```

---

## ✅ 抽卡注意事项 (Execution Notes)

- 如果手机在开头就出现：重抽或加强 `no smartphone visible at the beginning`。
- 如果人物看起来呆板：加强 `authentic creator energy, lively eyes, subtle micro-expressions, spontaneous mid-speech expression, slight head tilt, relaxed shoulders`。
- 如果口播文案跑题：确保 Hook、价值点和 CTA 都围绕中东足球资讯 App，不要写成泛足球评论。
- 如果人脸在结尾仍比手机清晰：加强 `rack focus shifts from face to green smartphone screen`。
- 如果背景出现人物或立柱：加强 `no background characters, no columns, no poles, no vertical obstructions`。
- 如果绿幕不够纯：加强 `perfectly flat, completely solid, bright chroma key green, evenly lit`。
- 如果手部畸形：增加 `natural hand motion, realistic fingers`，并在 Negative Prompt 保留 `extra fingers, distorted hands`。
- 如果展示图被误当成首帧：明确第一步是 `no smartphone, no handheld device visible`，第二步才是 `holding a modern smartphone`。

---

## 输出注意

- 所有 Prompt 默认使用英文，以提升图像 / 视频模型理解稳定性。
- 中文部分只用于导演解析，不要混入英文 Prompt 模板内部的变量说明。
- 口播稿必须与中东足球资讯 App 推广相关。
- 不要输出与本工作流无关的营销文案或投放策略，除非用户额外要求。
