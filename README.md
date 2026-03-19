# 🎵 MP3 Voice Translator

将MP3文件中的中文语音批量转换为英文语音的工具。

## 功能特点

- 🎤 语音识别（OpenAI Whisper）
- 🌐 自动翻译（OpenAI GPT）
- 🔊 英文语音合成（Microsoft Edge TTS）
- ⚡ 批量处理

## 环境要求

- Python 3.8+
- ffmpeg（需加入PATH）
- OpenAI API Key

## 安装

```bash
# 克隆项目
git clone https://github.com/yourusername/mp3-voice-translator.git
cd mp3-voice-translator

# 创建虚拟环境（推荐）
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 配置

1. 复制配置文件：
```bash
cp config.example.py config.py
```

2. 编辑 `config.py`，填入你的 API Key：
```python
OPENAI_API_KEY = "sk-your-key-here"
```

## 使用方法

```bash
# 基本用法
python main.py --input D:\espwork\music --output D:\espwork\music_english

# 或指定配置文件
python main.py -c config.py -i input.mp3 -o output.mp3
```

## 参数说明

```
--input, -i        输入目录或文件
--output, -o       输出目录
--config, -c       配置文件路径
--model, -m        Whisper模型 (base/small/medium/large)
--voice, -v        TTS声音 (默认: en-US-AriaNeural)
--help             显示帮助
```

## 支持的 TTS 声音

- `en-US-AriaNeural` (推荐)
- `en-US-GuyNeural`
- `en-GB-SoniaNeural`
- 更多声音请参考 [Microsoft Edge TTS](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/text-to-speech)

## 费用说明

- Whisper API: ~$0.006/分钟
- GPT翻译: ~$0.001/100字符
- Edge TTS: 免费

## 项目结构

```
mp3-voice-translator/
├── main.py              # 主程序入口
├── config.example.py    # 配置示例
├── translator/
│   ├── __init__.py
│   ├── whisper.py       # 语音识别
│   ├── translator.py    # 翻译
│   ├── tts.py          # 语音合成
│   └── audio.py        # 音频处理
├── requirements.txt
└── README.md
```

## 常见问题

### Q: 识别结果不准确
A: 可以尝试使用更大的 Whisper 模型（medium 或 large）

### Q: 翻译结果不够自然
A: 可以修改 `translator.py` 中的 prompt，让翻译更符合你的需求

### Q: ffmpeg 未找到
A: 确保 ffmpeg 已安装并加入系统 PATH

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
