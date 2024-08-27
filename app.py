from flask import Flask, request

app = Flask(__name__)

@app.route('/transcription', methods=['POST'])
def transcription():
    transcription_text = request.form['TranscriptionText']
    print("Transcription:", transcription_text)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
