from flask import Flask, render_template
from api import app

app = Flask(__name__)


@app.route('/')
def Home():
    return "Hello!!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

#スキルチェックページ
@app.route('/check')
def check():
    return render_template('check.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080',debug=True)
