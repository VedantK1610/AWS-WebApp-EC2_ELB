from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", hostname=socket.gethostname())

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)