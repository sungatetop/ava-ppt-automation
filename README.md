# AVA PPT Automation

艾娃 · 自动化演示工具包 - 将 PPT 演示转换为可自主播放的交互式展示。

## 背景

AI做ppt已经非常常见了，那么既然都是AI做ppt了，那就让AI自己讲！准备好需要的素材，AI会自动生成ppt。
调用此技能，即可生成一个自动播放的ppt，可以精准控制演讲的时间。

## 使用技巧

- 准备你的产品或想要介绍的素材，建议统一放入`assets/`文件夹下,按文件类型分类

  <image src="./demo/skill-assets.png" width="400" />

- 调用此技能，让AI（例如Trae）编写大纲、讲稿、规划ppt演讲时间安排等，建议使用Markdown格式，示例:`./demo/presentation.md`
-
  <image src="./demo/skill-use.png" width="400" />

#### 快速开始

```bash
# 1. 安装依赖
pip install requests imageio pillow numpy dashscope

# 2. 配置 API Key
export DASHSCOPE_API_KEY="your_api_key_here"

# 3. 运行脚本生成素材
python scripts/generate_image_template.py
python scripts/generate_audio_template.py
```

## 项目结构

```
ava-ppt-automation/
├── assets/
│   ├── audio/          # TTS 生成的音频文件
│   ├── images/         # 生成的图片素材
│   ├── audio_script_template.json
│   ├── config.json     # API 配置
│   └── ppt_engine_template.html
├── scripts/
│   ├── generate_image_template.py   # 图片生成模板
│   ├── generate_audio_template.py   # 音频合成脚本
│   ├── extract_frames.py            # 视频帧提取
│   └── analyze_assets.py            # 素材分析
├── demo/
│   └── demo.mp4        # 演示视频
├── references/
│   ├── workflow.md      # 操作规程
│   ├── style_presets.md # 样式预设
│   └── animation_patterns.md
└── README.md
```

## 脚本使用

### 图片生成

编辑 `scripts/generate_image_template.py` 中的 `IMAGE_PLAN` 定义图片需求：

```python
IMAGE_PLAN = [
    {
        "id": "cover_placeholder",
        "prompt": "A professional background for tech presentation, abstract geometric shapes",
        "filename": "cover_bg.png"
    }
]
```

运行后生成的图片保存至 `assets/images/`。

### 音频合成

编辑 `play_plan` 定义音频章节：

```python
play_plan = [
    {"id": "section_1", "slides": "1-2", "text": "演示内容..."}
]
```

### 视频帧提取

从视频中提取指定时间点的帧：

```bash
python scripts/extract_frames.py
```

## PPT 引擎

`assets/ppt_engine_template.html` 提供自动播放功能：

- 支持键盘空格键启动
- 每页自动计时切换
- 视频页时长可单独配置
- 响应式设计适配各种屏幕

## 配置

在 `assets/config.json` 中配置 API Key，或通过环境变量 `DASHSCOPE_API_KEY` 设置。

## 示例视频

示例录制视频：`demo/demo.mp4`



https://github.com/user-attachments/assets/8ebdfcf0-59c7-40f4-b07d-faf55e5b9b5b







## 许可证

MIT License
