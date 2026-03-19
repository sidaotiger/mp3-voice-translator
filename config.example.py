#!/usr/bin/env python3
"""
配置示例文件
复制此文件为 config.py 并填入你的 API Key
"""

# ============== 必需配置 ==============

# OpenAI API Key (从 https://platform.openai.com/api-keys 获取)
OPENAI_API_KEY = "sk-your-key-here"

# ============== 可选配置 ==============

# Whisper 模型选择: base, small, medium, large
# 越大越准确，但越慢、越贵
WHISPER_MODEL = "base"

# Whisper API 模式: "api" (在线) 或 "local" (本地，需要安装 whisper)
WHISPER_MODE = "api"

# TTS 声音
# 常用: en-US-AriaNeural, en-US-GuyNeural, en-GB-SoniaNeural
TTS_VOICE = "en-US-AriaNeural"

# TTS 语速 (0.1 - 2.0, 1.0 为正常速度)
TTS_RATE = "+0%"

# TTS 音调 (-50% - +50%)
TTS_PITCH = "+0%"

# ============== 目录配置 ==============

# 输入输出目录（可选，也可以在命令行指定）
# INPUT_DIR = r"D:\espwork\music"
# OUTPUT_DIR = r"D:\espwork\music_english"

# ============== 翻译配置 ==============

# 翻译 prompt，可自定义翻译风格
TRANSLATION_SYSTEM_PROMPT = """You are a professional translator. 
Translate the following Chinese text to natural, conversational English.
Keep the tone friendly and easy to understand."""
