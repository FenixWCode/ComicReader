from flask import Flask, render_template, send_from_directory, abort
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
base_dir = os.getenv("BASE_PATH")


# Übersicht
@app.route('/')
def home():
    dirs = os.listdir(base_dir)
    return render_template("home.html", dirs=dirs)


# Inhalt
@app.route('/<cur_dir>')
def index(cur_dir):
    full_path = os.path.join(base_dir, cur_dir)
    if os.path.isdir(full_path):
        images = os.listdir(full_path)
        sorted_images = sorted(images, key=lambda x: int(x.split('.')[0]))
    else:
        print(f"Pfad {full_path} nicht gefunden")
        abort(404)

    return render_template("index.html", images=sorted_images, cur_dir=cur_dir)


@app.route('/serve-image/<folder>/<filename>', methods=['GET'])
def get_image(folder, filename):
    full_path = os.path.join(base_dir, folder)
    if not os.path.isdir(full_path):
        print(f"Pfad {full_path} nicht gefunden")
        abort(404)

    return send_from_directory(full_path, filename)


# GUI for webscraper
@app.route('/download')
def download():
    return render_template("download.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0') # 0.0.0.0 = Im lokalen Netz für alle Geräte verfügbar
