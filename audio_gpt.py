import os
import openai
import pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

from settings import TOKEN_GPT

openai.api_key = TOKEN_GPT

# If the size of the audio file is more than 25 MB:
# https://platform.openai.com/docs/guides/speech-to-text/longer-inputs


def convert_audio_to_text(audio_file):
    """Transcribes audio into the input language."""
    audio_file = open("audio/Recording.m4a", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)   # json, text, srt, verbose_json, or vtt
    print(transcript)
    return transcript


def translate_to_english_language():
    """Translates audio into English"""
    audio_file = open("audio/Recording.m4a", "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)
    print(transcript)


def convert_voice_to_text():
    """Creating a Recognizer object that will be used for voice recording and conversion"""
    with sr.Microphone() as source:    # Performing voice recording
        recognizer = sr.Recognizer()
        source.pause_threshold = 1
        print("Speak now!")
        recognizer.adjust_for_ambient_noise(source)  # removing background noises
        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
        try:    # Performing conversion a voice to text
            text = recognizer.recognize_google(audio, language="ru-RU")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Error sending the request: {e}")


def google_voice_acting(text: str):
    """Uses gtts library to interface with Google Translates text to speech API.
    It requires an Internet connection. It's pretty easy to use."""
    mp3_file = "mp3_file.mp3"
    if os.path.exists(mp3_file):
        os.remove(mp3_file)
    tts = gTTS(text, lang='ru')    # lang='ru'
    try:
        tts.save(mp3_file)
        playsound(mp3_file)
    except:
        print("Something wrong. Your ad could be here...")


def pyttsx3_voice_acting(text: str):
    """Uses pyttsx3 library to interface text to speech API.
    Offline text to speech."""
    mp3_file = "mp3_file.mp3"
    if os.path.exists(mp3_file):
        os.remove(mp3_file)
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)    # setting up new voice rate
    engine.setProperty('volume', 1.0)   # setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)   # changing index, changes voices. 1 for en, 0 for ru.
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("Something wrong. Your ad could be here...")
    finally:
        engine.stop()


def start_after_key_word(func: object, word="glad"):
    print(f"Say '{word}' to start recording your question…")
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower() == f"{word}":
                func()
        except Exception as e:
            print("An error occurred: {}".format(e))

