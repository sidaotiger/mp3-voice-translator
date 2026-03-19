# 🎵 MP3 Voice Translator

将MP3文件中的中文语音批量转换为英文语音的工具。

A tool that batch converts Chinese speech in MP3 files to English speech.

## ✨ 功能特点 | Features

- 🎤 语音识别（OpenAI Whisper）| Speech Recognition (OpenAI Whisper)
- 🌐 自动翻译（OpenAI GPT）| Auto Translation (OpenAI GPT)
- 🔊 英文语音合成（Microsoft Edge TTS）| English Voice Synthesis (Microsoft Edge TTS)
- ⚡ 批量处理 | Batch Processing

## 📋 环境要求 | Requirements

- Python 3.8+
- ffmpeg（需加入PATH | need to be in PATH）
- OpenAI API Key

## 🚀 安装 | Installation

```bash
# 克隆项目 | Clone the project
git clone https://github.com/sidaotiger/mp3-voice-translator.git
cd mp3-voice-translator

# 创建虚拟环境（推荐）| Create virtual environment (recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 安装依赖 | Install dependencies
pip install -r requirements.txt
```

## ⚙️ 配置 | Configuration

1. 复制配置文件 | Copy config file:
```bash
cp config.example.py config.py
```

2. 编辑 `config.py`，填入你的 API Key | Edit `config.py`, add your API Key:
```python
OPENAI_API_KEY = "sk-your-key-here"
```

## 📖 使用方法 | Usage

```bash
# 基本用法 | Basic usage
python main.py --input D:\espwork\music --output D:\espwork\music_english

# 或指定配置文件 | Or specify config file
python main.py -c config.py -i input.mp3 -o output.mp3
```

## 📝 参数说明 | Arguments

| 参数 | 参数 | 说明 | Description |
|------|------|------|-------------|
| --input, -i | 输入 | 输入目录或文件 | Input directory or file |
| --output, -o | 输出 | 输出目录 | Output directory |
| --config, -c | 配置 | 配置文件路径 | Config file path |
| --model, -m | 模型 | Whisper模型 (base/small/medium/large) | Whisper model |
| --voice, -v | 声音 | TTS声音 (默认: en-US-AriaNeural) | TTS voice |

## 🎤 支持的 TTS 声音 | Supported TTS Voices

- `en-US-AriaNeural` (推荐 | recommended)
- `en-US-GuyNeural`
- `en-GB-SoniaNeural`
- 更多声音 | More voices: [Microsoft Edge TTS](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/text-to-speech)

## 💰 费用说明 | Cost

- Whisper API: ~$0.006/分钟 | ~$0.006/minute
- GPT翻译 | GPT translation: ~$0.001/100字符 | ~$0.001/100 chars
- Edge TTS: 免费 | Free

## 📁 项目结构 | Project Structure

```
mp3-voice-translator/
├── main.py              # 主程序入口 | Main entry
├── config.example.py    # 配置示例 | Config example
├── translator/
│   ├── __init__.py
│   ├── whisper.py       # 语音识别 | Speech recognition
│   ├── translator.py    # 翻译 | Translation
│   ├── tts.py          # 语音合成 | TTS
│   └── audio.py        # 音频处理 | Audio processing
├── requirements.txt
└── README.md
```

## ❓ 常见问题 | FAQ

### Q: 识别结果不准确 | Recognition result not accurate
A: 可以尝试使用更大的 Whisper 模型（medium 或 large）| Try using a larger Whisper model (medium or large)

### Q: 翻译结果不够自然 | Translation not natural enough
A: 可以修改 `translator.py` 中的 prompt，让翻译更符合你的需求 | Modify the prompt in `translator.py` to suit your needs

### Q: ffmpeg 未找到 | ffmpeg not found
A: 确保 ffmpeg 已安装并加入系统 PATH | Make sure ffmpeg is installed and in system PATH

## 📜 许可证 | License

MIT License

## 🤝 贡献 | Contributing

欢迎提交 Issue 和 Pull Request！| Issues and Pull Requests are welcome!
