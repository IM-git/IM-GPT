import openai
import json
import time
import os

from settings import TOKEN_GPT

# API key
openai.api_key = TOKEN_GPT

# The file where the conversation history is stored
data_story_conversation = "chat_history.json"


def run_chat_gpt(query: str):
    """Receive a request from the user and print a response from gpt.
    Save the conversation messages."""
    messages = [{"role": "user", "content": query}]
    reply = get_response_from_gpt(messages)
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    save_conversation(data_story_conversation, messages)


def get_response_from_gpt(messages: list) -> list:
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return chat.choices[0].message.content


def read_file(file_path: str) -> list | dict | tuple:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_conversation(file_path: str, messages: list) -> None:
    """Saving the message to a JSON file"""
    data = read_file(file_path)
    data[time.strftime('%Y-%m-%dT%H:%M:%S')] = messages
    with open(file_path, "w") as file_name:
        json.dump(data, file_name)


if __name__ == '__main__':
    test_text = "Test message. Write a random number from 5 to 666"
    print(f"User: {test_text}")
    run_chat_gpt(test_text)

    while True:
        message = input("User: ")
        if message == "q":
            break
        run_chat_gpt(message)
