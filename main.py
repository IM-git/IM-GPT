from chat_gpt import run_chat_gpt
from audio_gpt import convert_voice_to_text, start_after_key_word

import speech_recognition as sr


def _test_voice_assistant():
    while True:
        try:
            message = convert_voice_to_text()
            if message in ["q", "exit", "quit", "stop", "стоп", "выход"]:
                break
            print(f"User: {message}")
            run_chat_gpt(message)
        except Exception as e:
            print("An error occurred: {}".format(e))


if __name__ == '__main__':

    # _test_chat_assistant()
    _test_voice_assistant()
