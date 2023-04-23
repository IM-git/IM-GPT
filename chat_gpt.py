import openai
import json
import time
import os

from settings import TOKEN_GPT

openai.api_key = TOKEN_GPT
data_story_conversation = "chat_history.json"

# time.strftime('%Y-%m-%dT%H:%M:%S')


def main(message: str):
    data = read_file()
    messages = []
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    # data = {
    #     time.strftime('%Y-%m-%dT%H:%M:%S'): messages
    # }
    data[time.strftime('%Y-%m-%dT%H:%M:%S')] = messages
    save_conversation(data_story_conversation, data)


def save_conversation_in_jsonl():
    messages = []
    while True:
        message = input("User: ")  # message
        if message == "q": break

        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
        with open(data_story_conversation, "a") as file_name:
            json.dump(messages, file_name)
            messages = []


def read_file():
    with open(data_story_conversation, "r") as file:
        data = json.load(file)
    return data


def save_conversation(file_path: str, data: str):
    with open(file_path, "w") as file_name:
        json.dump(data, file_name)


def chat_gpt():
    while True:
        message = input("User: ")
        if message == "q":
            break
        main(message)
    # print(messages)
    # save_conversation(data_story_conversation, messages)


if __name__ == '__main__':
    chat_gpt()
