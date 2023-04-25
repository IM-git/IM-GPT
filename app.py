from flask import Flask, render_template, request, jsonify

from chat_gpt import get_response_from_gpt, save_conversation_in_jsonl

app = Flask(__name__, template_folder='./templates')
data_story_conversation_jsonl = "chat_history.jsonl"


@app.route('/', methods=["GET", "POST"])
def index():
    # if request.method == "POST":
    #     query = request.form.get("user-message")
    #     messages = [{"role": "user", "content": query}]
    #     if len(query) <= 2048:
    #         reply = get_response_from_gpt(messages)
    #         messages.append({"role": "assistant", "content": reply})
    #         save_conversation_in_jsonl(data_story_conversation_jsonl, messages)
    # # return render_template('index.html', messages=messages)

    return render_template('index.html')


# @app.route("/get-text", methods=["POST"])
# def get_text():
#     # get text input from user
#     input_text = request.form["input_text"]
#
#     # get response from GPT-3
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=input_text,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#
#     # get text from response
#     gpt_response = response.choices[0].text.strip()
#
#     # return GPT-3 text response
#     return gpt_response
#
#
# @app.route("/get-audio", methods=["POST"])
# def get_audio():
#     # get text input from user
#     input_text = request.form["input_text"]
#
#     # get response from GPT-3
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=input_text,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#
#     # get text from response
#     gpt_response = response.choices[0].text.strip()
#
#     # generate audio from text
#     tts = gTTS(gpt_response)
#     audio_file = "gpt_audio.mp3"
#     tts.save(audio_file)
#
#     # return generated audio file
#     return send_file(audio_file, mimetype="audio/mpeg")


if __name__ == "__main__":
    app.run(debug=True)
