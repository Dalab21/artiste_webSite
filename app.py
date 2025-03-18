from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biography')
def biography():
    return render_template('biography.html')

@app.route('/photos')
def photos():
    return render_template('gallery.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
