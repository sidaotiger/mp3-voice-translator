#!/usr/bin/env python3
"""
语音合成 - MiniMax TTS
"""

import requests
import base64
import json
import os
import subprocess


class MiniMaxTTS:
    """MiniMax TTS 语音合成"""
    
    def __init__(self, api_key: str, model: str = "speech-01-turbo", voice: str = "female-yujie", api_base: str = "https://api.minimax.chat/v1"):
        self.api_key = api_key
        self.model = model
        self.voice = voice
        self.api_base = api_base
    
    async def speak(self, text: str, output_path: str):
        """将文本转换为语音并保存"""
        try:
            url = f"{self.api_base}/t2a_v2"
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            # 请求 WAV 格式
            data = {
                "model": self.model,
                "text": text,
                "voice_setting": {
                    "voice_id": self.voice
                },
                "audio_setting": {
                    "sample_rate": 16000,
                    "bitrate": 128000,
                    "format": "wav"
                }
            }
            
            response = requests.post(url, json=data, headers=headers, timeout=120)
            
            if response.status_code == 200:
                result = response.json()
                if "data" in result and "audio" in result["data"]:
                    # 获取实际格式
                    actual_format = result.get("extra_info", {}).get("audio_format", "wav")
                    print(f"      TTS format: {actual_format}")
                    
                    # 解码 base64 音频
                    audio_data = base64.b64decode(result["data"]["audio"])
                    
                    # 生成临时 WAV 文件名
                    dir_name = os.path.dirname(output_path) or "."
                    base_name = os.path.basename(output_path)
                    temp_wav = os.path.join(dir_name, f"_temp_{base_name}.wav")
                    
                    # 保存为 WAV
                    with open(temp_wav, "wb") as f:
                        f.write(audio_data)
                    
                    # 用 ffmpeg 转换为 MP3
                    cmd = ["ffmpeg", "-y", "-i", temp_wav, "-acodec", "mp3", output_path]
                    result_cmd = subprocess.run(cmd, capture_output=True)
                    
                    # 删除临时 WAV
                    if os.path.exists(temp_wav):
                        os.remove(temp_wav)
                    
                    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                        print(f"      Saved: {output_path}")
                    else:
                        raise Exception(f"FFmpeg conversion failed")
                else:
                    raise Exception(f"TTS返回格式错误: {result}")
            else:
                raise Exception(f"API错误: {response.status_code} - {response.text}")
                
        except Exception as e:
            raise Exception(f"TTS 失败: {e}")
    
    @staticmethod
    def get_available_voices():
        """获取可用的声音列表"""
        return [
            "male-qn-qingse",
            "female-shaonv", 
            "female-yujie",
            "male-qn-jingying",
            "male-qn-badao",
            "female-yujie",
            "male-qn-dream",
            "female-shaonv-emo",
            "female-yujie-emo",
            "male-qn-jingying-emo"
        ]
