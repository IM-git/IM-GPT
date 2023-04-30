from typing import Callable

from chat_gpt import run_chat_gpt
from audio_gpt import AudioTools

audio_tools = AudioTools()


def _test_assistant(message: str, voice_func: Callable):
    while True:
        try:
            if message in ["q", "exit", "quit", "stop", "стоп", "выход"]:
                break
            print(f"User: {message}")
            voice_func(message)
        except Exception as e:
            print("An error occurred: {}".format(e))


def _test_voice_assistant_google():
    # message = ""
    # _test_assistant(message, google_voice_acting())
    pass


def _test_voice_assistant_pyttsx3():
    # _test_assistant()
    pass


def _test_voice_assistant_elevenlabs():
    # _test_assistant()
    pass


def _test_voice_assistant():
    while True:
        try:
            message = audio_tools.convert_voice_to_text()
            if message in ["q", "exit", "quit", "stop", "стоп", "выход", "404"]:
                break
            print(f"User: {message}")
            run_chat_gpt(message)
        except Exception as e:
            print("An error occurred: {}".format(e))


if __name__ == '__main__':

    _test_voice_assistant()
