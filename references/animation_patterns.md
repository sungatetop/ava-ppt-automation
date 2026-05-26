# 动画模式参考 (Animation Patterns)

本参考文档提供了不同氛围下的动画建议及核心 CSS 代码片段。

## 氛围与动画匹配

| 氛围 | 动画特点 | 视觉提示 |
| :--- | :--- | :--- |
| **戏剧化 / 电影感** | 慢速淡入 (1-1.5s), 大比例缩放 | 暗色背景, 聚光灯效果, 全屏图像 |
| **科技感 / 未来感** | 霓虹发光, 故障效果 (Glitch), 网格显现 | 粒子系统, 网格背景, 等宽字体 |
| **活泼 / 友好** | 弹性动画 (Bouncy), 漂浮感 | 圆角, 明亮色彩, 手绘元素 |
| **专业 / 企业** | 快速简洁 (200-300ms), 平滑切换 | 深蓝/炭黑, 精准间距, 数据可视化 |
| **极简 / 宁静** | 极慢微动, 柔和淡出 | 大量留白, 衬线体, 优雅间距 |

## 核心进入动画 (Entrance Animations)

```css
/* 1. 淡入 + 向上平移 (最通用) */
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1),
                transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
.slide.visible .reveal {
    opacity: 1;
    transform: translateY(0);
}

/* 2. 缩放进入 */
.reveal-scale {
    opacity: 0;
    transform: scale(0.9);
    transition: opacity 0.6s, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 3. 模糊进入 */
.reveal-blur {
    opacity: 0;
    filter: blur(10px);
    transition: opacity 0.8s, filter 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
```

## 背景特效 (Background Effects)

```css
/* 网格背景 */
.grid-bg {
    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 50px 50px;
}

/* 渐变迷雾背景 */
.gradient-bg {
    background:
        radial-gradient(ellipse at 20% 80%, rgba(120, 0, 255, 0.15) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 255, 200, 0.1) 0%, transparent 50%),
        var(--bg-primary);
}
```

## 动画性能优化
- 优先使用 `transform` 和 `opacity` 进行动画，避免触发重排 (Reflow)。
- 为动画元素添加 `will-change: transform, opacity`（慎用）。
- 尊重用户系统设置：使用 `prefers-reduced-motion` 媒体查询禁用复杂动画。
