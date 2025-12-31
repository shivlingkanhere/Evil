from flask import Flask, request, jsonify
from gtts import gTTS
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("text")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    answer = response.choices[0].message.content

    tts = gTTS(answer)
    tts.save("response.mp3")

    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run()
