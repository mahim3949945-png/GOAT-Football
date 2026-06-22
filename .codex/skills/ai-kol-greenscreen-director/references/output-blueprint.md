# 核心输出蓝图

当用户输入标准口令后，先检查是否包含 `15秒` 或 `30秒`。

如果没有时长，只输出：

```text
请问这条视频要做 15 秒还是 30 秒？也可以直接补充：生成KOL：[人物] + [场景]，时长：15秒
```

不要生成口播稿、图片或视频 Prompt。

如果包含时长，必须严格按以下结构输出。不要省略任一部分。当前环境支持图片生成工具时，Step 1 和 Step 2 必须先直接生成图片，再输出复用 Prompt。两张图片最终交付都必须是 9:16 竖图。

---

## 🎬 镜头设定解析 (Scene Configuration)

**人物与构图 (Character & Composition)：**  
[用中文扩写人物外观、服装、年龄气质、面部表现和画面构图。必须强调：中景、直视镜头、面部是唯一视觉中心、前 3 秒不出现手机、背景无人物、无杂物、无立柱。]

**真人口播表现 (Performance)：**  
[用中文说明人物要像真实 KOL 口播：眼神灵动、有自然微表情、轻微头部倾斜、肩颈放松、身体轻微前倾、嘴型处在真实说话中，避免僵硬摆拍、蜡像感、证件照感。]

**推广产品 (Product)：**  
[固定围绕“面向中东地区球迷的足球资讯 App”展开。如用户提供 App 名称，用真实名称；否则使用 `[App名称]` 占位。说明本条视频是在推荐 App 的足球新闻、比分动态、赛程、转会消息和热门比赛资讯。]

**视频时长 (Duration)：**  
[只能是 `15秒` 或 `30秒`。说明该时长对应的节奏分配：15 秒为快速 Hook + 举手机 + 转焦；30 秒为 Hook + 价值解释 + 举手机 + 转焦。]

**场景与光影 (Atmosphere)：**  
[用中文扩写场景布置与灯光。必须把用户场景净化为干净、可控、低干扰的背景，强调柔和环境光、电影感补光、背景不抢焦。]

**时间轴动作流 (Timeline)：**  
[根据时长选择输出：  
15秒：`0-3s：人脸清晰纯口播，手机不出现` -> `3-5s：人物从画面下方举起纯绿幕手机` -> `5-15s：rack focus 到手机屏幕，手机清晰，人脸与背景虚化`  
30秒：`0-5s：人脸清晰 Hook，手机不出现` -> `5-15s：继续介绍 App 价值，手机仍不出现` -> `15-18s：举起纯绿幕手机` -> `18-30s：rack focus 到手机屏幕，手机清晰，人脸与背景虚化`]

---

## 🗣️ 推广口播稿 (App Promo Script)

> 此口播稿用于后期配音、字幕或真人 KOL 参考。文案必须围绕中东足球资讯 App，不要跑成泛足球闲聊。

**中文版本：**

```text
[根据时长生成中文口播稿。15秒为3-4句；30秒为5-7句。结构：足球迷痛点 Hook -> [App名称] 的价值点 -> 下载 / 打开 CTA。]
```

**English / MENA-friendly Version：**

```text
[Generate an English voiceover for Middle Eastern football fans based on the selected duration. 15 seconds: 3-4 sentences. 30 seconds: 5-7 sentences. Structure: hook -> app value -> CTA.]
```

**Arabic Placeholder Version：**

```text
[Generate an Arabic voiceover draft for Middle Eastern football fans based on the selected duration. Keep it natural and app-focused.]
```

---

## 🖼️ 第一步：直接生成纯口播首帧图 (Step 1: Generate First Frame)

> 直接生成演员定妆图 / 视频首帧。此图必须只有人物口播状态，不允许提前举起手机。生成后保留以下 Prompt 作为复用记录。

**Image Generation：**  
[直接生成 9:16 竖图。文件名建议：`kol-first-frame-[人物关键词]-[时长]-9x16.png`。如果生成工具返回非 9:16，先裁切或补边成 9:16 再交付。]

**Reusable Prompt：**

```text
[套用 references/prompt-formula.md 的 Step 1 模板，填入扩写后的人物与场景]
```

**Negative Prompt：**

```text
[套用 references/prompt-formula.md 的 Step 1 Negative Prompt 建议]
```

---

## 📱 第二步：直接生成拿手机展示图 (Step 2: Generate Phone Holding Still)

> 直接生成一张人物拿着纯绿幕手机的图片。此图用于终帧参考、展示姿势参考或素材扩展，不能替代第一步视频首帧。生成后保留以下 Prompt 作为复用记录。

**Image Generation：**  
[直接生成 9:16 竖图。文件名建议：`kol-phone-holding-[人物关键词]-[时长]-9x16.png`。如果生成工具返回非 9:16，先裁切或补边成 9:16 再交付。]

**Reusable Prompt：**

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
[根据时长套用 references/prompt-formula.md 的 Step 3 15秒或30秒模板，填入扩写后的人物与场景]
```

**Negative Prompt：**

```text
[套用 references/prompt-formula.md 的 Step 3 Negative Prompt 建议]
```

---

## ✅ 抽卡注意事项 (Execution Notes)

- 如果手机在开头就出现：重抽或加强 `no smartphone visible at the beginning`。
- 如果用户没给时长：不要继续生成，先问 15 秒还是 30 秒。
- 如果生成图片不是 9:16：不要直接交付，先处理成 9:16 竖图。
- 如果 30 秒视频太早举手机：加强 `from 5-15 seconds, still no smartphone visible`。
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
- Step 1 和 Step 2 是直接图片生成任务；不要只输出 Prompt 而不生成图片，除非当前环境没有图片生成能力。
- Step 1 和 Step 2 的最终图片必须是 9:16 竖图；非 9:16 原图只能作为中间产物，不能作为最终交付图。
- 不要输出与本工作流无关的营销文案或投放策略，除非用户额外要求。
