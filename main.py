from typing import Callable

from chat_gpt import ChatGptTools
from audio_gpt import AudioTools
from tools import FileTools

audio_tools = AudioTools()
file_tools = FileTools()
data_story_conversation_jsonl = "chat_history.jsonl"


def _test_assistant(message: str, voice_func: Callable):
    while True:
        try:
            if message in ["q", "exit", "quit", "stop", "стоп", "выход"]:
                break
            print(f"User: {message}")
            voice_func(message)
        except Exception as e:
            print("An error occurred: {}".format(e))


def run_chat_gpt(query: str):
    """Receive a request from the user and print a response from gpt.
    Save the conversation messages."""
    reply = ChatGptTools().get_response_from_gpt(query)
    print(f"ChatGPT: {reply}")
    audio_tools.get_voice_acting(reply)
    file_tools.save_conversation_in_jsonl(data_story_conversation_jsonl, query, reply)


def _test_voice_assistant():
    while True:
        try:
            message = audio_tools.convert_voice_to_text()
            if message in ["q", "exit", "quit", "stop", "стоп", "выход", "404"]:
                break
            print(f"User: {message}")
            run_chat_gpt(message)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':

    _test_voice_assistant()
