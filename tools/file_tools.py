import json


class FileTools:

    @staticmethod
    def read_file(file_path: str) -> list | dict | tuple:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    @staticmethod
    def save_conversation_in_jsonl(file_path: str, query: str, reply: str) -> None:
        """Saving the message to a JSONL file"""
        messages = [{"role": "user", "content": query}, {"role": "assistant", "content": reply}]
        with open(file_path, "a") as file_name:
            for line in messages:
                json.dump(line, file_name)

