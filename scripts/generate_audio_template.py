import os
import dashscope
from dashscope.audio.tts_v2 import SpeechSynthesizer
import ssl
import certifi

# === 通用配置区 ===
# 要求用户输入API密钥，或读取config.json获取API密钥
API_KEY = os.getenv('DASHSCOPE_API_KEY', 'YOUR_API_KEY_HERE')
dashscope.api_key = API_KEY

# 解决 macOS 下的 SSL 证书问题
os.environ['SSL_CERT_FILE'] = certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context

# 音频保存路径
AUDIO_DIR = os.path.abspath("assets/audio")
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

# === 演示规划模板 (Play Plan) ===
# 1. 章节化拆分：将内容按逻辑分组
# 2. 视频页独立：凡是有视频演示的 Slide，建议分配独立的章节 ID
play_plan = [
    { 
        "id": "section_example_1",
        "slides": "1-2", 
        "text": "这里是开场白。艾娃 是您的数字助手。请注意发音纠偏。" 
    },
    { 
        "id": "section_video_demo",
        "slides": "13", 
        "text": "接下来请看一段浏览器操作演示。艾娃 正在自主执行任务。" 
    },
]

def synthesize_all(model='cosyvoice-v1', voice='longshuo'):
    """
    通用预合成函数
    """
    print(f"=== 开始合成音频 | 模型: {model} | 音色: {voice} ===")
    
    for section in play_plan:
        filename = f"{section['id']}.mp3"
        audio_path = os.path.join(AUDIO_DIR, filename)
        
        # 发音预处理逻辑示例
        text = section['text'].replace("Ava", "艾娃").replace("ScalingAgent", "Scaling Agent")
        
        print(f"正在处理 {section['id']}...")
        
        try:
            synthesizer = SpeechSynthesizer(model=model, voice=voice)
            audio_data = synthesizer.call(text)
            if audio_data:
                with open(audio_path, 'wb') as f:
                    f.write(audio_data)
                print(f"  [成功] 已保存: {filename}")
        except Exception as e:
            print(f"  [异常] {filename}: {str(e)}")

if __name__ == "__main__":
    synthesize_all()
