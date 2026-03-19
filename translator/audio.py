#!/usr/bin/env python3
"""
音频处理 - 使用 ffmpeg
"""

import subprocess
import os


class AudioProcessor:
    """音频处理工具"""
    
    @staticmethod
    def replace_audio(original_audio: str, new_audio: str, output_path: str) -> bool:
        """
        用新音频替换原音频
        """
        # 检查 ffmpeg
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise Exception("ffmpeg 未安装，请先安装 ffmpeg 并加入 PATH")
        
        # 使用 ffmpeg 替换音频
        cmd = [
            "ffmpeg", "-y",
            "-i", original_audio,
            "-i", new_audio,
            "-map", "0:v",       # 保留原视频轨道
            "-map", "1:a",       # 使用新音频
            "-c:v", "copy",      # 视频直接复制
            "-c:a", "aac",       # 音频转 AAC
            "-shortest",         # 取较短者
            output_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            # 如果失败，尝试简单复制
            import shutil
            shutil.copy(new_audio, output_path)
        
        return os.path.exists(output_path)
    
    @staticmethod
    def get_duration(audio_path: str) -> float:
        """获取音频时长（秒）"""
        cmd = [
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
            audio_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        try:
            return float(result.stdout.strip())
        except:
            return 0.0
