from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello world!</h1><h3>It is nice to meet you man</h3>'

if __name__ == '__main__':
    app.run()