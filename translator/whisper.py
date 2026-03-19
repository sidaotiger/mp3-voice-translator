#!/usr/bin/env python3
"""
语音识别 - 硅基流动 API (直接调用)
"""

import requests
import asyncio
import base64


class WhisperSTT:
    """Whisper 语音识别"""
    
    def __init__(self, api_key: str, model: str = "FunAudioLLM/SenseVoiceLarge", api_base: str = None):
        self.api_key = api_key
        self.model = model
        self.api_base = api_base or "https://api.siliconflow.cn/v1"
    
    async def transcribe(self, audio_path: str) -> str:
        """转录音频文件"""
        try:
            # 读取音频文件
            with open(audio_path, "rb") as f:
                audio_data = f.read()
            
            # 硅基流动的 Whisper API
            url = f"{self.api_base}/audio/transcriptions"
            
            files = {
                'file': ('audio.mp3', audio_data, 'audio/mpeg'),
                'model': (None, self.model),
                'language': (None, 'zh')
            }
            
            headers = {
                'Authorization': f'Bearer {self.api_key}'
            }
            
            response = requests.post(url, files=files, headers=headers, timeout=120)
            
            if response.status_code == 200:
                result = response.json()
                return result.get("text", "")
            else:
                raise Exception(f"API错误: {response.status_code} - {response.text}")
                
        except Exception as e:
            raise Exception(f"语音识别失败: {e}")
