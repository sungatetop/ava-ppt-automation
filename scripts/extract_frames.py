import os
import json
import imageio
from PIL import Image
import numpy as np

def extract_frame(video_path, timestamp, output_path):
    """
    从视频中提取指定时间点（秒）的帧并保存
    """
    try:
        reader = imageio.get_reader(video_path)
        # 获取视频的 fps
        fps = reader.get_meta_data().get('fps', 25)
        # 计算帧索引
        frame_index = int(timestamp * fps)
        
        # 读取指定帧
        frame = reader.get_data(frame_index)
        
        # 转换为 Pillow 图像对象
        img = Image.fromarray(frame)
        
        # 简单分析：获取尺寸和主导颜色
        width, height = img.size
        # 缩小图片以快速计算主导颜色
        small_img = img.resize((1, 1), resample=Image.Resampling.BILINEAR)
        dominant_color = small_img.getpixel((0, 0))
        
        # 保存图片
        img.save(output_path)
        
        return {
            "success": True,
            "path": output_path,
            "dimensions": f"{width}x{height}",
            "dominant_color": f"rgb{dominant_color}",
            "timestamp": f"{timestamp}s"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def main():
    print("=== 艾娃视频帧提取工具 (AVA Video Frame Extractor) ===")
    
    # 配置文件路径或直接输入
    video_dir = "assets/videos"
    output_dir = "assets/images"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 示例任务：分析 assets/videos 下的第一个 mp4 文件，提取第 1 秒和第 5 秒
    videos = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
    
    if not videos:
        print(f"在 {video_dir} 下未发现视频文件。")
        return

    print(f"发现视频: {videos}")
    
    results = []
    for video in videos:
        video_path = os.path.join(video_dir, video)
        # 默认提取 1s, 5s, 10s 位置的图片
        timestamps = [1, 5, 10] 
        
        for ts in timestamps:
            output_name = f"{os.path.splitext(video)[0]}_frame_{ts}s.png"
            output_path = os.path.join(output_dir, output_name)
            
            print(f"正在提取 {video} @ {ts}s ...")
            res = extract_frame(video_path, ts, output_path)
            
            if res["success"]:
                print(f"  成功: {output_name} ({res['dimensions']}, {res['dominant_color']})")
                results.append(res)
            else:
                print(f"  失败: {res['error']}")

    # 保存分析报告
    with open("frame_analysis_report.json", "w", encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(f"\n分析报告已生成: frame_analysis_report.json")

if __name__ == "__main__":
    main()
