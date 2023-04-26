# https://beta.elevenlabs.io/sign-up
import requests
from playsound import playsound
from settings import EL_API_KEY

# streaming chunk size
chunk_size = 1024
stability = 0.75
similarity_boost = 0.75

# https://docs.elevenlabs.io/api-reference/voices-gets
voice_id = "EXAVITQu4vr4xnSDxMaL"
voice_name = "Bella"
tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

data = {
  "text": "Hello world!",
  "voice_settings": {
    "stability": stability,
    "similarity_boost": similarity_boost
  }
}

headers = {
    "Accept": "application/json",
    "xi-api-key": EL_API_KEY,
    "Content-Type": "application/json"
}


def convert_text_to_voice(mp3_file_name: str, message="Hello fworld!"):
    data["text"] = message
    response = requests.post(tts_url, json=data, headers=headers, stream=True)

    with open(mp3_file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)


if __name__ == '__main__':
    # Test 1
    file_name_1 = "output.mp3"
    convert_text_to_voice(file_name_1)
    playsound(file_name_1)

    # Test 2
    mes = "Your API key. This is required by most endpoints to access our API programatically." \
          "You can view your xi-api-key using the 'Profile' tab on the website."
    file_name_2 = "output2.mp3"
    convert_text_to_voice(file_name_2, message=mes)
    playsound(file_name_2)



