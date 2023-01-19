from flask import Flask, render_template, send_from_directory
import random
import os

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    # list all the png images from the images folder
    images = [img for img in os.listdir('static') if img.endswith('.png')]
    # choose a random image
    random_image = random.choice(images)
    return render_template('index.html', image=random_image)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
