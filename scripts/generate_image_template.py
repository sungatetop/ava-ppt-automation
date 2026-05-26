import os
import requests
import json
import time

"""
================================================================================
AVA 视觉生成脚本模板 (AVA Image Generation Template)
================================================================================
说明：
1. 本脚本为通用模板，用于从业务需求自动化生成 PPT 视觉素材。
2. 使用前请确保已配置 API_KEY（通过环境变量、直接输入 API_KEY）。
3. 请在下方的 `IMAGE_PLAN` 中定义您的素材需求。
================================================================================
"""

# === 1. 核心配置区 (Core Configuration) ===
# 建议在运行前根据实际项目结构调整路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_IMAGE_DIR = os.path.join(BASE_DIR, "assets", "images")

# 默认生成模型
DEFAULT_MODEL = "qwen-image-2.0-pro-2026-04-22"

# === 2. 视觉生成规划表 (Image Generation Plan) ===
# [模板说明]：请在此处填入您需要生成的图片列表
# 格式: {"id": "标识符", "prompt": "提示词", "filename": "保存文件名"}
IMAGE_PLAN = [
    {
        "id": "cover_placeholder",
        "prompt": "A professional and clean background for a technology presentation, abstract geometric shapes, corporate blue theme, 4k.",
        "filename": "cover_bg.png"
    },
    # 在此处继续添加您的需求...
]

# === 3. 核心逻辑区 (Core Logic - 通常无需修改) ===

def get_api_key():
    """多级 API KEY 获取逻辑"""
    # 1. 环境变量
    api_key = os.getenv('DASHSCOPE_API_KEY')
    if api_key: return api_key
    # 2. 直接输入 API_KEY
    api_key = "YOUR_API_KEY_HERE"
    return api_key


def download_image(url, save_path):
    """下载并持久化图片"""
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"  [下载失败] {save_path}: {e}")
        return False

def run_generation_task(plan=None, model=DEFAULT_MODEL, output_dir=DEFAULT_IMAGE_DIR):
    """执行批量生成任务"""
    if not plan:
        plan = IMAGE_PLAN
        
    api_key = get_api_key()
    if not api_key:
        print("❌ 错误: 未检测到有效的 API Key。请检查环境变量或 config.json。")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print(f"🚀 启动 AVA 视觉生产线 | 模型: {model}")
    print(f"📂 输出目录: {output_dir}\n")

    for task in plan:
        print(f"正在生产 [{task['id']}] ...")
        payload = {
            "model": model,
            "input": {
                "messages": [{"role": "user", "content": [{"text": task['prompt']}]}]
            },
            "parameters": {
                "size": "2048*2048", 
                "n": 1, 
                "prompt_extend": True,
                "watermark": False
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                img_url = data.get("output", {}).get("choices", [{}])[0].get("message", {}).get("content", [{}])[0].get("image")
                
                if img_url:
                    save_path = os.path.join(output_dir, task['filename'])
                    if download_image(img_url, save_path):
                        print(f"  ✅ [成功] 产物已归档: {task['filename']}")
                else:
                    print(f"  ⚠️ [告警] 接口未返回有效 URL")
            else:
                print(f"  ❌ [失败] API 返回错误 {response.status_code}: {response.text}")
        except Exception as e:
            print(f"  💥 [异常] {e}")

if __name__ == "__main__":
    # 您可以直接运行此脚本，或在其他模块中调用 run_generation_task()
    run_generation_task()
