import openai
import json
import os

from settings import TOKEN_GPT

openai.api_key = TOKEN_GPT
# messages = []
data_story_conversation = "chat_history.json"



def main(message: str):
    messages = []
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    save_conversation(data_story_conversation, messages)


def read_file(way):
    with open(way) as text:
        data = json.load(text)
    return data


def save_conversation(file_path: str, data: str):
    with open(file_path, "a") as file_name:
        json.dump(data, file_name)

def chat():
    while True:
        message = input("User: ")
        if message == "q":
            break
        main(message)
    # print(messages)
    # save_conversation(data_story_conversation, messages)


if __name__ == '__main__':

    chat()
