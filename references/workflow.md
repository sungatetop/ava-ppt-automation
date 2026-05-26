# 艾娃 · 自动化演示操作规程

## 1. 讲稿处理规范
- **中英混合**：英文缩写建议拆分为单词（如 `Scaling Agent Lab`），品牌名建议替换为中文（如 `艾娃`）。
- **章节划分**：视频演示页必须独立为一个 `section`，确保音频时长与视频时长能独立匹配。

## 2. TTS 合成参数 (推荐)
- **模型**：`cosyvoice-v1`
- **音色**：`longshuo` (嘹亮男声，适合路演)
- **环境要求**：macOS 下需配置 `certifi` 解决 SSL 证书问题。

## 3. 自动播放引擎配置 (HTML)
在 `playPlan` 中配置每一页的 `videoTimings`：
- `13`: 36 (Browser-use 完整演示)
- `14`: 43 (报告与文案演示)
- `16`: 42 (多智能体协作演示)

## 4. 目录结构标准
```
project-root/
├── assets/
│   └── audio/          # 存放 MP3 音频
├── scripts/
│   └── generate_audio.py # 音频合成脚本
└── index.html          # 集成自动播放逻辑的 PPT
```
