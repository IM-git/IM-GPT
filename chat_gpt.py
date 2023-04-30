import openai

from settings import TOKEN_GPT


class ChatGptTools:
    openai.api_key = TOKEN_GPT  # API token

    @staticmethod
    def get_response_from_gpt(query: str) -> list:
        messages = [{"role": "user", "content": query}]
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        return chat.choices[0].message.content


if __name__ == '__main__':

    # Test of the GPT API response
    def __test_response(question: str):
        try:
            chat_gpt_tools = ChatGptTools()
            print(f"User: {question}")
            print(chat_gpt_tools.get_response_from_gpt(question))
        except Exception as e:
            print(f"An error occurred: {e}")

    # free version allow to send response only 3 time within 1 minute
    __test_response("Test message. Write a random number from 5 to 666")
    __test_response("Write hello")
    __test_response("Write the name of all the oceans.")
