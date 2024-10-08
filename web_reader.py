from flask import Flask, render_template, send_from_directory, abort
import os


app = Flask(__name__)
base_dir = "C:\D\BILDER\Iwas\Bilder\Comics\Selenium"


@app.route('/')
def home():
    dirs = os.listdir(base_dir)
    return render_template("home.html", dirs=dirs)


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


if __name__ == "__main__":
    app.run()
