import openai
import json
import time

from settings import TOKEN_GPT, EL_API_KEY, VOICE_ID
from audio_gpt import google_voice_acting, ElevenLabsVoice
from eleven_labs import convert_text_to_voice

openai.api_key = TOKEN_GPT  # API token

# The file where the conversation history is stored
data_story_conversation_json = "chat_history.jsonl"
data_story_conversation_jsonl = "chat_history.jsonl"

elv = ElevenLabsVoice(EL_API_KEY, VOICE_ID)


def run_chat_gpt(query: str):
    """Receive a request from the user and print a response from gpt.
    Save the conversation messages."""
    reply = get_response_from_gpt(query)
    print(f"ChatGPT: {reply}")
    # elv.convert_text_to_voice("output.mp3", reply)
    google_voice_acting(reply)
    # pyttsx3_voice_acting(reply)
    save_conversation_in_jsonl(data_story_conversation_jsonl, query, reply)


def get_response_from_gpt(query: str) -> list:
    messages = [{"role": "user", "content": query}]
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return chat.choices[0].message.content


def read_file(file_path: str) -> list | dict | tuple:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_conversation_in_jsonl(file_path: str, query: str, reply: str) -> None:
    """Saving the message to a JSONL file"""
    messages = [{"role": "user", "content": query}, {"role": "assistant", "content": reply}]
    with open(file_path, "a") as file_name:
        for line in messages:
            json.dump(line, file_name)


if __name__ == '__main__':
    test_text = "Test message. Write a random number from 5 to 666"
    print(f"User: {test_text}")
    run_chat_gpt(test_text)

    while True:
        message = input("User: ")
        if message in ["q", "exit", "quit", "stop"]:
            break
        run_chat_gpt(message)
