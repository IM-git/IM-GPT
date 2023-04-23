from chat_gpt import run_chat_gpt
from audio_gpt import convert_voice_to_text


def _test_chat_assistant():
    while True:
        message = input("User: ")
        if message in ["q", "exit", "quit", "stop"]:
            break
        run_chat_gpt(message)


def _test_voice_assistant():
    while True:
        message = convert_voice_to_text()
        if message in ["q", "exit", "quit", "stop"]:
            break
        print(f"User: {message}")
        run_chat_gpt(message)


if __name__ == '__main__':

    # _test_chat_assistant()
    _test_voice_assistant()
