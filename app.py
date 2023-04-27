from flask import Flask, request, send_from_directory
import download_video

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "URL não informado.", 400

    result = download_video.baixar_video(url)
    return result

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
