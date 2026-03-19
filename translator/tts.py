#!/usr/bin/env python3
"""
语音合成 - Microsoft Edge TTS
"""

import asyncio
import edge_tts


class EdgeTTS:
    """Edge TTS 语音合成"""
    
    def __init__(self, voice: str = "en-US-AriaNeural", rate: str = "+0%", pitch: str = "+0%"):
        self.voice = voice
        self.rate = rate
        self.pitch = pitch
    
    async def speak(self, text: str, output_path: str):
        """将文本转换为语音并保存"""
        try:
            communicate = edge_tts.Communicate(
                text,
                voice=self.voice,
                rate=self.rate,
                pitch=self.pitch
            )
            await communicate.save(output_path)
        except Exception as e:
            raise Exception(f"TTS 失败: {e}")
    
    async def get_available_voices(self):
        """获取可用的声音列表"""
        voices = await edge_tts.list_voices()
        # 过滤英文 voices
        return [v for v in voices if v["ShortName"].startswith("en-")]
