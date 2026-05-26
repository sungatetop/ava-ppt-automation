# 自动播放与声画同步引擎 (Auto-play & Sync Engine)

本技能包要求生成的 HTML PPT 必须集成一套基于时间维度的自动播放引擎。

## 1. 引擎集成要求
在 HTML 的 `<script>` 标签中，必须包含一个 `PresentationEngine` 类，该类负责：
- **音频加载与播放**：使用 `new Audio()` 加载章节音频。
- **翻页逻辑**：根据音频时长或预设时长自动触发 `goToSlide`。
- **视频页锁定**：通过 `videoTimings` 对象，强制设置特定幻灯片的停留时间。

## 2. PPT 设计规范 (Design Specifications)

在进行 PPT 视觉制作时，必须遵循以下核心设计准则，以确保演示的专业性与兼容性：

### 2.1 视口适配 (Viewport Fitting - 强制要求)
- **无滚动原则**：每一页幻灯片必须精确适配 `100vh` 视口高度。严禁在幻灯片内部出现滚动条。
- **布局约束**：
    - 容器必须设置 `height: 100vh; height: 100dvh; overflow: hidden;`。
    - 所有字体大小和间距必须使用 `clamp(min, preferred, max)` 函数，禁止使用固定像素值。
    - 内容溢出时，必须主动拆分为多页幻灯片。

### 2.2 视觉美学 (Aesthetics)
- **去 AI 化设计**：避免平庸的渐变色和通用布局。追求独特、具有品牌辨识度的设计。
- **排版与字体**：
    - 优先选择具有设计感的 Web Fonts（如 Fontshare 或 Google Fonts），严禁使用系统默认字体（Arial, Inter 等）。
    - 核心标题应具备强烈的视觉冲击力。
- **色彩与氛围**：
    - 建立统一的主色调（CSS 变量管理）。使用对比鲜明的点缀色而非均匀分布的调色板。
    - 增加背景层次感：利用 CSS 渐变叠层、几何纹理或毛玻璃效果（Backdrop-filter）提升高级感。

### 2.3 内容密度限制 (Content Density)
- **标题页**：1 个主标题 + 1 个副标题。
- **内容页**：1 个标题 + 最多 4-6 个要点。
- **卡片页**：1 个标题 + 最多 6 个卡片（2x3 或 3x2 布局）。
- **图片页**：图片最大高度限制为 `min(60vh, 500px)`，确保为文字留足空间。

### 2.4 动效设计 (Motion)
- **有意义的动画**：动画应服务于叙事。优先使用 CSS 动画实现 staggered reveals（交错显现）效果。
- **性能优先**：确保动画平滑且不影响交互性能。

## 3. 自动播放逻辑核心 (Implementation)

```javascript
/* 
   核心同步公式：
   Duration = Math.max(Audio_Duration / Slide_Count_In_Section, Predefined_Video_Time)
*/

async playSection(section) {
    this.audioPlayer.src = this.audioDir + section.audio;
    return new Promise((resolve) => {
        this.audioPlayer.onloadedmetadata = async () => {
            const audioInterval = this.audioPlayer.duration / section.slides.length;
            this.audioPlayer.play();
            
            for (let i = 0; i < section.slides.length; i++) {
                const slideNum = section.slides[i];
                this.goToSlide(slideNum); // 执行翻页
                
                // 确保视频播完，或语音播完
                const duration = Math.max(audioInterval, this.videoTimings[slideNum] || 0);
                await new Promise(r => setTimeout(r, duration * 1000));
            }
            resolve();
        };
    });
}
```

## 4. 交互入口
- 页面必须包含一个显眼的 **“▶ 自动演示”** 按钮。
- 建议放在右下角，使用 `fixed` 定位，并在点击后自动进入第一页开始演示。
