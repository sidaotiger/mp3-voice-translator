# Translator package
from .whisper import WhisperSTT
from .translator import Translator
from .audio import AudioProcessor

# 根据配置选择 TTS
try:
    from .minimax_tts import MiniMaxTTS
    HAS_MINIMAX_TTS = True
except:
    HAS_MINIMAX_TTS = False

# Edge TTS 作为备选
from .tts import EdgeTTS

__all__ = ['WhisperSTT', 'Translator', 'EdgeTTS', 'AudioProcessor', 'MiniMaxTTS', 'HAS_MINIMAX_TTS']
