from flask import Flask

app = Flask(__name__)

@app.route('/')
def root_page():
    return "Hello home page"