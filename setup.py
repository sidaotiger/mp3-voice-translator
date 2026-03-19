from setuptools import setup, find_packages
import os

this_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(this_dir, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()

requirements = ["openai>=1.0.0", "whisper", "edge-tts", "ffmpeg-python", "tqdm"]

setup(
    name="mp3-voice-translator",
    version="0.1.1",
    author="sidaotiger",
    author_email="",
    description="将中文MP3语音翻译并转换为英文语音的工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidaotiger/mp3-voice-translator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "mp3-translator=main:main",
        ],
    },
)
