import os
import openai
from settings import TOKEN_GPT

openai.api_key = TOKEN_GPT

# If the size of the audio file is more than 25 MB:
# https://platform.openai.com/docs/guides/speech-to-text/longer-inputs


def convert_audio_to_text():
    """Transcribes audio into the input language."""
    audio_file = open("audio/Recording.m4a", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)   # json, text, srt, verbose_json, or vtt
    print(transcript)


def translate_to_english_language():
    """Translates audio into English"""
    audio_file = open("audio/Recording.m4a", "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)
    print(transcript)
