import os
import json
from tinytag import TinyTag

def get_duration(file_path):
    """使用 pure-python 库 tinytag 获取多媒体文件时长（秒）
    支持: mp3, mp4, m4a, wav, flac, webm 等
    """
    try:
        tag = TinyTag.get(file_path)
        return tag.duration if tag.duration else 0
    except Exception as e:
        print(f"无法分析文件 {file_path}: {e}")
        return 0

def analyze_directory(directory, extensions):
    """分析目录下指定后缀的文件时长"""
    results = {}
    if not os.path.exists(directory):
        return results
    
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in extensions):
            file_path = os.path.join(directory, filename)
            duration = get_duration(file_path)
            results[filename] = round(duration, 2)
    return results

def main():
    print("=== 艾娃资产分析工具 (AVA Asset Analyzer) ===")
    print("状态: 使用 pure-python 跨平台兼容引擎 (tinytag)")
    
    # 分析视频
    video_dir = os.path.abspath("assets/videos")
    video_data = analyze_directory(video_dir, ['.mp4', '.mov', '.avi', '.webm'])
    
    # 分析音频
    audio_dir = os.path.abspath("assets/audio")
    audio_data = analyze_directory(audio_dir, ['.mp3', '.wav', '.m4a'])

    print("\n[视频时长分析结果] - 建议填入 HTML 的 videoTimings 中:")
    if not video_data:
        print("  (未发现视频文件)")
    for name, sec in video_data.items():
        print(f"  - {name}: {sec} 秒")

    print("\n[音频时长分析结果]:")
    if not audio_data:
        print("  (未发现音频文件)")
    for name, sec in audio_data.items():
        print(f"  - {name}: {sec} 秒")

    # 输出为 JSON 方便复制
    output = {
        "engine": "tinytag",
        "video_durations": video_data,
        "audio_durations": audio_data
    }
    
    with open("asset_durations.json", "w") as f:
        json.dump(output, f, indent=4)
    print(f"\n完整结果已保存至: {os.path.abspath('asset_durations.json')}")

if __name__ == "__main__":
    main()
