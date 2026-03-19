#!/usr/bin/env python3
"""
翻译 - MiniMax GPT API
"""

import requests


class Translator:
    """使用 MiniMax 翻译文本"""
    
    def __init__(self, api_key: str, model: str = "abab6.5s-chat", api_base: str = "https://api.minimax.chat/v1"):
        self.api_key = api_key
        self.model = model
        self.api_base = api_base
    
    async def translate(self, text: str) -> str:
        """翻译文本"""
        try:
            url = f"{self.api_base}/text/chatcompletion_v2"
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": "You are a professional translator. Translate ALL text to English. Remove any Chinese characters. Output ONLY English translation."},
                    {"role": "user", "content": text}
                ]
            }
            
            response = requests.post(url, json=data, headers=headers, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                raise Exception(f"API错误: {response.status_code} - {response.text}")
                
        except Exception as e:
            raise Exception(f"翻译失败: {e}")
