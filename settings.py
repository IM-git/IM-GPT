import os
import dotenv


dotenv.load_dotenv('.env')
LOGIN = ''
PASSWORD = ''
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
EL_API_KEY = os.environ['EL_API_KEY']
TOKEN_GPT = os.environ['TOKEN_GPT']

voice_assistance = "google"   # google, pyttsx3
