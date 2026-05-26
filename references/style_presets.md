# Style Presets Reference

本参考文档提供了 12 套精心设计的视觉预设，灵感来源于真实的设计案例，旨在告别平庸的“AI 感”设计。

## 暗色主题 (Dark Themes)

### 1. Bold Signal (强力信号)
- **氛围**：自信、大胆、现代、高冲击力。
- **布局**：暗色渐变背景上的彩色卡片。左上角显示页码，右上角导航，左下角标题。
- **排版**：标题 `Archivo Black` (900)，正文 `Space Grotesk` (400/500)。
- **色彩**：
  ```css
  --bg-primary: #1a1a1a;
  --bg-gradient: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
  --card-bg: #FF5722;
  --text-primary: #ffffff;
  ```

### 2. Electric Studio (电子工作室)
- **氛围**：干净、专业、高对比度。
- **布局**：上下分割面板。
- **排版**：标题与正文均使用 `Manrope`。
- **色彩**：深黑 (#0a0a0a)、纯白、亮蓝 (#4361ee)。

### 3. Creative Voltage (创意电压)
- **氛围**：活力、复古现代、创意十足。
- **布局**：左右分割面板，电蓝色左侧，暗色右侧。
- **排版**：标题 `Syne`，等宽字体 `Space Mono`。

### 4. Dark Botanical (暗夜植物)
- **氛围**：优雅、高级、艺术感。
- **布局**：内容居中，角落有柔和的抽象形状。
- **排版**：优雅衬线体 `Cormorant`，无衬线正文 `IBM Plex Sans`。

## 亮色主题 (Light Themes)

### 5. Notebook Tabs (笔记本标签)
- **氛围**：社论感、井然有序、触感真实。
- **布局**：暗色背景上的米色纸张卡片，右侧边缘有彩色标签。
- **排版**：经典社论体 `Bodoni Moda`，正文 `DM Sans`。

### 6. Swiss Modern (瑞士现代)
- **氛围**：精准、包豪斯风格、极简。
- **布局**：可见网格，非对称布局。
- **排版**：`Archivo` (800) + `Nunito` (400)。
- **色彩**：纯黑、纯白、红色点缀 (#ff3300)。

## 特色主题 (Specialty Themes)

### 7. Neon Cyber (霓虹赛博)
- **氛围**：未来感、科技感。
- **排版**：`Clash Display` + `Satoshi`。
- **背景**：粒子背景、霓虹发光、网格图案。

### 8. Terminal Green (终端绿)
- **氛围**：开发者风格、黑客美学。
- **排版**：全等宽字体 `JetBrains Mono`。
- **色彩**：GitHub 深色 (#0d1117)，终端绿 (#39d353)。

### 9. Academic Innovation (学术创新路演风)
- **氛围**：专业、严谨、高科技、医疗/学术路演感。
- **布局**：
    - **顶部导航**：带有渐变背景的水平页签导航（如：项目背景、产品介绍...）。
    - **内容容器**：圆角卡片，使用微透明的玻璃拟态效果。
    - **视觉焦点**：使用高对比度的气泡标注（Callout）突出图像细节。
- **排版**：标题使用粗体无衬线体（如 `Noto Sans SC Bold`），数字使用 `Oswald`。
- **色彩**：
  ```css
  --bg-primary: #12005e; /* 深邃蓝 */
  --accent-yellow: #ccff00; /* 荧光黄（用于核心重点） */
  --accent-cyan: #00ffff; /* 电力青（用于次要重点） */
  --text-primary: #ffffff;
  --header-gradient: linear-gradient(90deg, #12005e, #6200ea);
  ```

---

## 字体配对指南 (Font Pairing)

| 预设 | 标题字体 | 正文字体 | 来源 |
| :--- | :--- | :--- | :--- |
| Bold Signal | Archivo Black | Space Grotesk | Google |
| Electric Studio | Manrope | Manrope | Google |
| Dark Botanical | Cormorant | IBM Plex Sans | Google |
| Swiss Modern | Archivo | Nunito | Google |
| Neon Cyber | Clash Display | Satoshi | Fontshare |
| Terminal Green | JetBrains Mono | JetBrains Mono | JetBrains |

---

## 禁用设计项 (禁止使用)
- **字体**：Inter, Roboto, Arial 等系统默认字体作为标题。
- **颜色**：通用的靛蓝色 (#6366f1) 或简单的紫色渐变。
- **布局**：全部居中的平庸布局、无目的的阴影。
