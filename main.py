import openai
import json
import os

from settings import TOKEN_GPT

openai.api_key = TOKEN_GPT
messages = []


def main(message: str):
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})


if __name__ == '__main__':

    # Run GPT BOT
    while True:
        message = input("User: ")
        if message == "q":
            break
        main(message)
