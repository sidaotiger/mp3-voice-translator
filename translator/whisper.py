#!/usr/bin/env python3
"""
语音识别 - OpenAI Whisper API
"""

import openai


class WhisperSTT:
    """Whisper 语音识别"""
    
    def __init__(self, api_key: str, model: str = "base"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key
    
    async def transcribe(self, audio_path: str) -> str:
        """转录音频文件"""
        try:
            with open(audio_path, "rb") as audio_file:
                response = openai.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language="zh"  # 指定中文
                )
            return response.text
        except Exception as e:
            raise Exception(f"语音识别失败: {e}")
