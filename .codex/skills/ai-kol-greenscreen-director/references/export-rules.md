# 本地桌面归档规则

Local Desktop Export Rules

## 默认保存位置

每次生成完整导演方案后，默认保存到：

```text
~/Desktop/ai-kol-greenscreen-director/
```

如果当前系统的桌面目录不存在，按顺序处理：

1. 尝试创建 `~/Desktop/ai-kol-greenscreen-director/`。
2. 如果无法创建或当前运行环境无法访问用户本地桌面，则明确告知用户，并询问可用保存路径。
3. 在云端或沙盒环境中，先保存到当前工作区的 `outputs/ai-kol-greenscreen-director/`，并提示用户下载或同步到本地桌面。

## 文件夹命名

每条 KOL 指令创建一个独立子文件夹：

```text
YYYYMMDD_HHMM_[人物关键词]_[画幅]_[时长]
```

示例：

```text
20260622_1540_middle-east-football-fan_9x16_15s/
```

## 必须保存的文件

每次至少保存以下文本文件：

```text
director-plan.md
```

内容必须包含：

- 镜头设定解析
- 画幅与时长
- Logo 使用说明
- 足球 App 卖点
- Step 1 Midjourney 纯口播首帧垫图 Prompt
- Step 2 Midjourney 举绿幕手机垫图 Prompt
- Step 3 Kling / Runway 视频动作 Prompt
- Step 4 足球 App 口播稿
- Negative Prompt

如果工具链实际生成了图片或视频，也保存到同一子文件夹，并使用以下命名：

```text
01-first-frame-prompt.md
02-phone-reference-prompt.md
03-i2v-motion-prompt.md
04-voiceover-script.md
first-frame.png
phone-reference.png
final-video.mp4
app-logo.[ext]
```

## 输出结束提示

如果已成功保存，最后必须告诉用户保存路径：

```text
已保存到本地桌面：~/Desktop/ai-kol-greenscreen-director/[本次子文件夹]/
```

如果只能保存到云端工作区，最后必须告诉用户：

```text
当前环境无法直接访问你的本地桌面，已先保存到工作区：[路径]。请下载或同步到本地桌面。
```
