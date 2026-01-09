pip install Flask Pillow
import os
from flask import Flask, render_template, request, send_from_directory
from PIL import Image
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            img = Image.open(file)
            rotated_img = img.rotate(180, expand=True)
            filepath = os.path.join(UPLOAD_FOLDER, "rotated_" + file.filename)
            rotated_img.save(filepath)
            return render_template('index.html', filename="rotated_" + file.filename)
    return render_template('index.html')
@app.route('/uploads/<filename>')
def display_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
if __name__ == '__main__':
    app.run(debug=True)