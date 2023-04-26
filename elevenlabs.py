import requests
from settings import EL_API_KEY


# streaming chunk size
CHUNK_SIZE = 1024

# https://docs.elevenlabs.io/api-reference/voices-gets
data_elevenlabs = {"voice_id": "EXAVITQu4vr4xnSDxMaL",
                   "voice_name": "Bella"}
voice_id = data_elevenlabs["voice_id"]
voice_name = data_elevenlabs["voice_name"]

add_voice_url = f"https://api.elevenlabs.io/v1/voices/{voice_id}?with_settings=false"

headers = {
  "Accept": "application/json",
  "xi-api-key": EL_API_KEY
}

data = {
    'name': voice_name,
    'labels': '{"accent": "American", "gender": "Female"}',
    'description': 'An American female voice with a slight hoarseness in his throat. Perfect for news.'
}

response = requests.post(add_voice_url, headers=headers, data=data)
# print(f"#1# {response.json()}")

# get default voice settings
response = requests.get("https://api.elevenlabs.io/v1/voices/settings/default",
                        headers={"Accept": "application/json"}).json()
# print(f"#2# {response}")
stability = response["stability"]
similarity_boost = response["similarity_boost"]
# print(stability, similarity_boost)

tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

headers["Content-Type"] = "application/json"

data = {
  "text": "Now that you know how to get all the voices,"
          "let’s see how to create a new one. First, you need to get samples for the voice you want to add.",
  "voice_settings": {
    "stability": stability,
    "similarity_boost": similarity_boost
  }
}

response = requests.post(tts_url, json=data, headers=headers, stream=True)
# print(f"#3# {response}")

with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

# Retrieve history. It should contain generated sample.
history_url = "https://api.elevenlabs.io/v1/history"

headers = {
  "Accept": "application/json",
  "xi-api-key": EL_API_KEY
}

response = requests.get(history_url, headers=headers)

# print(response.text)
