#!/usr/bin/env python3
"""
MP3 Voice Translator - 主程序入口
"""

import os
import sys
import argparse
import asyncio
from pathlib import Path

# 添加项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent))

from translator import WhisperSTT, Translator, EdgeTTS, AudioProcessor


def load_config(config_path: str = None):
    """加载配置文件"""
    if config_path and os.path.exists(config_path):
        # 动态导入配置
        import importlib.util
        spec = importlib.util.spec_from_file_location("config", config_path)
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
        return config
    elif os.path.exists("config.py"):
        import config
        return config
    else:
        # 使用默认配置
        class DefaultConfig:
            OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
            WHISPER_MODEL = "base"
            TTS_VOICE = "en-US-AriaNeural"
            TTS_RATE = "+0%"
            TTS_PITCH = "+0%"
            TRANSLATION_SYSTEM_PROMPT = "Translate Chinese to English naturally."
        return DefaultConfig()


async def process_file(input_path: str, output_path: str, config):
    """处理单个文件"""
    print(f"\n📄 处理: {Path(input_path).name}")
    
    try:
        # 1. 语音识别
        print("  🎤 语音识别中...")
        stt = WhisperSTT(config.OPENAI_API_KEY, config.WHISPER_MODEL)
        chinese_text = await stt.transcribe(input_path)
        if not chinese_text:
            print("  ⚠️ 未能识别到语音，跳过")
            return False
        print(f"  📝 识别: {chinese_text[:80]}...")
        
        # 2. 翻译
        print("  🌐 翻译中...")
        translator = Translator(config.OPENAI_API_KEY, config.TRANSLATION_SYSTEM_PROMPT)
        english_text = await translator.translate(chinese_text)
        print(f"  📝 翻译: {english_text[:80]}...")
        
        # 3. TTS
        print("  🔊 生成语音中...")
        tts = EdgeTTS(config.TTS_VOICE, config.TTS_RATE, config.TTS_PITCH)
        temp_tts = output_path.replace(".mp3", "_temp.mp3")
        await tts.speak(english_text, temp_tts)
        
        # 4. 替换音频
        print("  🎬 合成中...")
        processor = AudioProcessor()
        processor.replace_audio(input_path, temp_tts, output_path)
        
        # 清理临时文件
        if os.path.exists(temp_tts):
            os.remove(temp_tts)
        
        print(f"  ✅ 完成!")
        return True
        
    except Exception as e:
        print(f"  ❌ 错误: {e}")
        return False


async def main():
    parser = argparse.ArgumentParser(description="MP3 Voice Translator - 将中文语音转换为英文")
    parser.add_argument("-i", "--input", required=True, help="输入目录或文件")
    parser.add_argument("-o", "--output", required=True, help="输出目录")
    parser.add_argument("-c", "--config", default="config.py", help="配置文件路径")
    parser.add_argument("-m", "--model", default="base", choices=["base", "small", "medium", "large"], help="Whisper模型")
    parser.add_argument("-v", "--voice", default="en-US-AriaNeural", help="TTS声音")
    
    args = parser.parse_args()
    
    # 加载配置
    config = load_config(args.config)
    
    # 检查 API Key
    if not config.OPENAI_API_KEY:
        print("❌ 请在配置文件中设置 OPENAI_API_KEY")
        print("   复制 config.example.py 为 config.py 并填入你的 API Key")
        sys.exit(1)
    
    # 创建输出目录
    os.makedirs(args.output, exist_ok=True)
    
    # 获取输入文件
    input_path = Path(args.input)
    if input_path.is_file():
        files = [input_path]
    else:
        files = list(input_path.glob("*.mp3"))
    
    if not files:
        print("❌ 未找到 MP3 文件")
        sys.exit(1)
    
    print(f"🎵 找到 {len(files)} 个文件")
    print(f"📂 输入: {args.input}")
    print(f"📂 输出: {args.output}")
    print(f"🤖 Whisper: {args.model}")
    print(f"🔊 TTS: {args.voice}")
    
    # 确认
    response = input("\n开始处理? (y/n): ")
    if response.lower() != 'y':
        print("已取消")
        return
    
    # 处理
    success = 0
    failed = 0
    
    for i, f in enumerate(files, 1):
        output_file = os.path.join(args.output, f"{f.stem}_en.mp3")
        if await process_file(str(f), output_file, config):
            success += 1
        else:
            failed += 1
    
    print(f"\n{'='*40}")
    print(f"🎉 处理完成! 成功: {success}, 失败: {failed}")
    print(f"📂 输出目录: {args.output}")


if __name__ == "__main__":
    asyncio.run(main())
