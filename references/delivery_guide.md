# 最终产物交付物说明 (Delivery Guide)

本技能包生成的最终产物是一个高度集成的演示文件夹。

## 1. 文件夹结构规范

交付给用户的文件夹应严格遵循以下结构，确保所有路径均为相对路径：

```
delivery-folder/
├── index.html              # 演示主入口 (内置样式与逻辑)
├── outline.md              # PPT 结构大纲
├── presentation_script.md  # 演讲稿
├── audio_script.json       # 音频合成讲稿
├── README.md               # 快速入门指南
├── config.json             # API 配置
└── assets/                 # 静态资源中心
    ├── audio/              # TTS 音频
    ├── images/             # 图片素材
    └── videos/             # 视频素材
```

## 2. 核心产物详解

### index.html
- **全集成设计**：包含所有幻灯片内容、CSS 样式框架（Viewport-base）、视觉主题样式及 `PresentationEngine` 播放类。
- **自动播放**：内置 `playPlan`（章节音频映射）和 `videoTimings`（视频时长锁定）。
    - *提示*：可通过运行 `scripts/analyze_assets.py` 自动化获取素材时长。
- **零外部依赖**：除 Web Fonts 外，所有逻辑和资源均在本地处理。

### 资产自动化迁移 (Asset Migration)

- 在制作阶段，技能包必须自动检测 PPT 中引用到的外部素材。
- **操作**：将这些原始素材复制到交付文件夹的相应子目录下，并在 HTML 中更新引用路径（如 `assets/videos/demo.mp4`）。

## 4. 典型交付示例 (Typical Delivery Example)

以“艾娃 AI 助手路演”项目为例，您的交付文件夹应如下所示：

### 目录结构预览

```text
ava-pitch-deck-bundle/
├── index.html              (已集成所有幻灯片内容与自动播放逻辑)
├── outline.md              (PPT 结构大纲，含视觉重点与内容规划)
├── presentation_script.md  (完整演讲稿，含视频配合指令)
├── audio_script.json       (音频制作讲稿：包含 TTS 合成文本、发音纠偏及章节映射)
├── README.md               (包含：空格键启动、E键编辑等说明)
├── config.json             (已填入 API_KEY，支持二次开发)
└── assets/
    ├── audio/              (含音频文件)
    ├── images/             (含图片素材)
    └── videos/             (含演示视频)
```

### 交付物验证清单 (Checklist)
- [ ] **文档完整**：文件夹内包含 `outline.md`、`presentation_script.md` 及 `audio_script.json`。
- [ ] **发音对齐**：`audio_script.json` 中的文本已完成发音纠偏（如使用“艾娃”）。
- [ ] **独立运行**：将文件夹移动到桌面其他位置，双击 `index.html` 依然能正常播放视频和音频。
- [ ] **声画同步**：视频页会自动停留，期间配音独立播放。
- [ ] **资产完整**：`assets/` 目录下不存在 0 字节的文件，所有用户素材均已成功迁移。
- [ ] **发音自然**：点击演示后，播报员应说“艾娃”而非英文单词。

