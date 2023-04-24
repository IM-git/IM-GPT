import openai
import json
import time

from settings import TOKEN_GPT
from audio_gpt import google_voice_acting, pyttsx3_voice_acting

openai.api_key = TOKEN_GPT  # API token

# The file where the conversation history is stored
data_story_conversation_json = "chat_history.jsonl"
data_story_conversation_jsonl = "chat_history.jsonl"


def run_chat_gpt(query: str):
    """Receive a request from the user and print a response from gpt.
    Save the conversation messages."""
    messages = [{"role": "user", "content": query}]
    reply = get_response_from_gpt(messages)
    print(f"ChatGPT: {reply}")
    google_voice_acting(reply)
    # pyttsx3_voice_acting(reply)
    messages.append({"role": "assistant", "content": reply})
    # save_conversation_in_json(data_story_conversation_json, messages)
    save_conversation_in_jsonl(data_story_conversation_jsonl, messages)


def get_response_from_gpt(messages: list) -> list:
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return chat.choices[0].message.content


def read_file(file_path: str) -> list | dict | tuple:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_conversation_in_json(file_path: str, messages: list) -> None:
    """Saving the message to a JSON file"""
    data = read_file(file_path)
    data[time.strftime('%Y-%m-%dT%H:%M:%S')] = messages
    with open(file_path, "w") as file_name:
        json.dump(data, file_name)


def save_conversation_in_jsonl(file_path: str, messages: list) -> None:
    """Saving the message to a JSONL file"""
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
