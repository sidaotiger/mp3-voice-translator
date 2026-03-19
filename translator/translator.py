#!/usr/bin/env python3
"""
翻译 - OpenAI GPT
"""

import openai


class Translator:
    """使用 GPT 翻译文本"""
    
    def __init__(self, api_key: str, system_prompt: str = None):
        self.api_key = api_key
        self.system_prompt = system_prompt or "Translate the following Chinese text to English."
        openai.api_key = api_key
    
    async def translate(self, text: str) -> str:
        """翻译文本"""
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": text}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"翻译失败: {e}")
