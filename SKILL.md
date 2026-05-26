---
name: ava-ppt-automation
description: "艾娃·自动化演示技能包。用于从业务文档,视频,图像,文本素材自动化生成声画同步的 HTML PPT 演示系统。包含素材分析、需求确认、大纲规划、讲稿优化、TTS 语音合成（阿里云百炼）、资产管理及自动播放引擎配置。适用于路演、产品发布、内部培训等自动化展示场景。"
author: "chenbaolin"
version: "1.0.0"
date: "2026-04-29"
email: "scaling_agent@126.com"
domain: "business"
license: "MIT"
----

# 艾娃 · 自动化演示技能包 (AVA PPT Automation)

本技能包提供了一套从原始素材到全自动、声画同步 PPT 演示系统的完整闭环工作流。

## 1. 核心生产流程 (Workflow)

### 阶段 0：素材分析与规划 (Material Analysis & Planning)

- **核心任务**：
  - **多模态解析**：分析用户提供的图像（UI 截图、Logo）、视频（演示录屏）和文本素材，识别核心功能点及视觉风格。
  - **大纲与规划**：根据素材内容编写 PPT 大纲及内容制作规划文档，标注视频/图像的精准插入点。
- **使用参考**：[outline\_templates.md](references/outline_templates.md) (选择场景模板)、[requirement\_analysis.md](references/requirement_analysis.md) (需求分析准则)。
- **输出产物**：
  - `outline.md`: PPT 结构大纲，定义各页视觉与内容重点。
  - `presentation_script.md`: 完整路演讲稿，包含视频配合指令。

### 阶段 1：PPT 制作与资产管理 (PPT Creation & Asset Management)

- **核心任务**：
  - **视觉制作**：遵循 Viewport Fitting 规范，集成自动播放引擎 `PresentationEngine`。
  - **资产管理**：将所有引用的图像、视频素材同步至交付目录，并分析时长。
- **使用参考**：[style\_presets.md](references/style_presets.md) (视觉预设)、[animation\_patterns.md](references/animation_patterns.md) (动效参考)、[timing\_logic.md](references/timing_logic.md) (同步逻辑)。
- **调用脚本**：可选工具脚本`analyze_assets.py` (分析时长)、`extract_frames.py` (抽取素材)。
- **输出产物**：
  - `index.html`: PPT 交互原型（内置样式框架与播放逻辑）。
  - `assets/images/` & `assets/videos/`: 归档后的视觉资产库。

### 阶段 2：语音合成与配置 (Audio & API) - **可选阶段**

- **核心任务**：进行文本发音纠偏，调用阿里云百炼 API 合成章节配音，并配置播放计划。
- **使用参考**：[generate\_audio\_template.py](scripts/generate_audio_template.py) (合成模板)。
- **输出产物**：
  - `audio_script.json`: 记录发音纠偏、音色配置及音频映射关系。
  - `assets/audio/`: 生成的章节 MP3 文件库。

### 阶段 2.5：视觉素材生成 (Optional Image Generation)

- **核心任务**：基于页面主题，利用文生图模型生成定制化的背景或插图。
- **使用参考**：[generate\_image\_template.py](scripts/generate_image_template.py) (生图模板)。
- **输出产物**：
  - `assets/images/`: 自动化生成的补充视觉素材。

### 阶段 3：产物交付 (Delivery)

- **核心任务**：整合所有文档与资产，生成独立的交付包，并提供操作指南。
- **使用参考**：[delivery\_guide.md](references/delivery_guide.md) (交付规范)。
- **输出产物**：标准的路演交付文件夹（包含 HTML、大纲、讲稿、音频讲稿及全量资产）。

## 2. 资源指南

### 脚本资源 (`scripts/`)

- `analyze_assets.py`: **跨平台兼容**。使用 `tinytag` 库分析素材时长。
- `extract_frames.py`: **轻量级素材抽取**。从视频中提取帧并分析主色调。
- `generate_audio_template.py`: **音频合成模板**。支持发音纠偏、多章节批量合成。
- `generate_image_template.py`: **视觉生成模板**。支持根据 `IMAGE_PLAN` 自动化生成并下载路演素材。

### 参考资料 (`references/`)

- `outline_templates.md`: 包含商业路演、学术技术、内部评审、培训教程 4 套标准化大纲模板。
- `requirement_analysis.md`: 素材分析、需求确认与大纲规划准则。
- `timing_logic.md`: 声画同步底层逻辑、自动播放引擎实现及 PPT 设计规范。
- `style_presets.md`: 12 套精心设计的视觉预设方案。
- `animation_patterns.md`: 不同氛围下的 CSS 动画模式参考。
- `delivery_guide.md`: **最终产物交付物说明书**。
- `svg_asset_guide.md`: **SVG 素材制作指南**。约定了风格、动效及不同场景下的 SVG 样式。

### 静态资产 (`assets/`)

- `viewport-base.css`: 强制性的基础 CSS 框架。
- `ppt_engine_template.html`: 集成自动播放逻辑的 HTML 演示模板。
- `config.json`: API 密钥配置模板。

## 3. 最终产物交付说明 (Final Deliverables)

一份成功的交付物应包含一个独立的文件夹，结构如下：

- `index.html`: 核心演示文件（内置自动播放引擎及所有样式框架）。
- `outline.md`: PPT 结构大纲，记录了视觉设计思路与内容排版规划。
- `presentation_script.md`: 详细的演讲稿，包含翻页提示与视频配合指令。
- `audio_script.json`: **新增**。专门用于 TTS 合成的讲稿，记录了发音纠偏后的文本、音色配置及音频文件映射关系。
- `assets/`:
  - `audio/`: 所有合成的讲稿音频。
  - `images/`: PPT 使用到的所有图片。
  - `videos/`: PPT 嵌入的所有视频。
- `README.md`: 简要的使用说明（如何启动、快捷键等）。

