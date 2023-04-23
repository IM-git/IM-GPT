import os
import openai
import speech_recognition as sr

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


def convert_voice_to_text():
    # Creating a Recognizer object that will be used for voice recording and conversion
    r = sr.Recognizer()
    # Determine the sound source (microphone)
    mic = sr.Microphone()
    # Performing voice recording
    with mic as source:
        print("Speak now!")
        r.adjust_for_ambient_noise(source)  # removing background noises
        audio = r.listen(source)
    # Performing conversion a voice to text
    try:
        # text = r.recognize_google(audio, language="ru-RU")
        text = r.recognize_google(audio)
        # print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Error sending the request: {e}")
