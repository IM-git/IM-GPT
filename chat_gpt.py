import openai
import json
from tools import FileTools

from audio_gpt import AudioTools, ElevenLabsVoice
from settings import TOKEN_GPT, EL_API_KEY, VOICE_ID

openai.api_key = TOKEN_GPT  # API token
file_tools = FileTools()

# The file where the conversation history is stored
data_story_conversation_json = "chat_history.jsonl"
data_story_conversation_jsonl = "chat_history.jsonl"

elv = ElevenLabsVoice(EL_API_KEY, VOICE_ID)
audio_tools = AudioTools()


class ChatGptTools:

    @staticmethod
    def get_response_from_gpt(query: str) -> list:
        messages = [{"role": "user", "content": query}]
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        return chat.choices[0].message.content


def run_chat_gpt(query: str):
    """Receive a request from the user and print a response from gpt.
    Save the conversation messages."""
    reply = ChatGptTools().get_response_from_gpt(query)
    print(f"ChatGPT: {reply}")
    # elv.convert_text_to_voice("output.mp3", reply)
    audio_tools.get_voice_acting(reply)
    # pyttsx3_convert_text_to_voice(reply)
    file_tools.save_conversation_in_jsonl(data_story_conversation_jsonl, query, reply)


if __name__ == '__main__':
    test_text = "Test message. Write a random number from 5 to 666"
    print(f"User: {test_text}")
    run_chat_gpt(test_text)

    while True:
        message = input("User: ")
        if message in ["q", "exit", "quit", "stop"]:
            break
        run_chat_gpt(message)
