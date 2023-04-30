import os
import dotenv


dotenv.load_dotenv('.env')
LOGIN = ''
PASSWORD = ''
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
EL_API_KEY = os.environ['EL_API_KEY']
TOKEN_GPT = os.environ['TOKEN_GPT']

voice_assistance = "google"   # google, pyttsx3
# https://platform.openai.com/docs/models/models

# gpt-3.5-turbo, gpt-3.5-turbo-0301, text-davinci-003
gpt_model = "gpt-3.5-turbo"  # get models list [print(_["id"]) for _ in openai.Model.list()["data"]]
