import os
import openai
import pyttsx3
import requests
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

from settings import TOKEN_GPT, EL_API_KEY, voice_assistance

# If the size of the audio file is more than 25 MB:
# https://platform.openai.com/docs/guides/speech-to-text/longer-inputs


class AudioTools:

    openai.api_key = TOKEN_GPT

    @staticmethod
    def convert_audio_to_text(path_to_audio_file="audio/Recording.m4a"):
        """Transcribes audio into the input language."""
        audio_file = open(path_to_audio_file, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)  # json, text, srt, verbose_json, or vtt
        print(transcript)
        return transcript

    @staticmethod
    def translate_to_english_language(path_to_audio_file="audio/Recording.m4a"):
        """Translates audio into English"""
        audio_file = open(path_to_audio_file, "rb")
        transcript = openai.Audio.translate("whisper-1", audio_file)
        print(transcript)
        return transcript

    # google, pyttsx3
    @staticmethod
    def get_voice_acting(text: str):
        if voice_assistance == "google":
            AudioTools._google_convert_text_to_voice(text)
        elif voice_assistance == "pyttsx3":
            AudioTools._pyttsx3_convert_text_to_voice(text)

    @staticmethod
    def convert_voice_to_text():
        """Creating a Recognizer object that will be used for voice recording and conversion"""
        with sr.Microphone() as source:    # Performing voice recording
            recognizer = sr.Recognizer()
            source.pause_threshold = 1
            print("Speak now!")
            recognizer.adjust_for_ambient_noise(source)  # removing background noises
            audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
            try:    # Performing conversion a voice to text
                text = recognizer.recognize_google(audio, language="ru-RU")    # en-US, ru-RU
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Error sending the request: {e}")

    @staticmethod
    def _google_convert_text_to_voice(text: str):
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

    @staticmethod
    def _pyttsx3_convert_text_to_voice(text: str):
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

    @staticmethod
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


class ElevenLabsVoice:
    CHUNK_SIZE = 1024
    STABILITY = 0.75
    SIMILARITY_BOOST = 0.75

    def __init__(self, api_key, voice_id):
        self.api_key = api_key
        self.voice_id = voice_id
        self.tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    def convert_text_to_voice(self, mp3_file_name, message):
        data = {
            "text": message,
            "voice_settings": {
                "stability": self.STABILITY,
                "similarity_boost": self.SIMILARITY_BOOST
            }
        }

        headers = {
            "Accept": "application/json",
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        response = requests.post(self.tts_url, json=data, headers=headers, stream=True)
        try:
            with open(mp3_file_name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
            playsound(mp3_file_name)
        except:
            print("Something went wrong. Please try again later.")


if __name__ == '__main__':

    # ------ Test ElevenLabs ------ #
    elv = ElevenLabsVoice(EL_API_KEY, "EXAVITQu4vr4xnSDxMaL")
    # Test 1
    file_name_1 = "output.mp3"
    elv.convert_text_to_voice(file_name_1, "Hello fworld!")

    # Test 2
    message = "Your API key. This is required by most endpoints to access our API programatically." \
              "You can view your xi-api-key using the 'Profile' tab on the website."
    file_name_2 = "output2.mp3"
    elv.convert_text_to_voice(file_name_2, message=message)

    # Test 3
    message2 = "I've become so numb, I can't feel you there" \
               "Become so tired, so much more aware" \
               "I'm becoming this, all I want to do" \
               "Is be more like me and be less like you"
    file_name_3 = "output3.mp3"
    elv.convert_text_to_voice(file_name_3, message=message2)
