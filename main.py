import openai

from settings import TOKEN_GPT

openai.api_key = TOKEN_GPT
messages = []


if __name__ == '__main__':
    while True:
        message = input("User: ")
        if message == "q":
            break

        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
