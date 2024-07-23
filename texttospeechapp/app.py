from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def tts():
    text = request.form['text']
    lang = request.form['lang']
    slow = request.form.get('slow') == 'true'
    
    tts = gTTS(text=text, lang=lang, slow=slow)
    output_file = "output.mp3"
    tts.save(output_file)
    
    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
