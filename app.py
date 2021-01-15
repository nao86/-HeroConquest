from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return "Hello!!"


@app.route('/index')
def index():
    return render_template('index.html')

#スキルチェックページ
@app.route('/check')
def check():
    return render_template('check.html')



if __name__ == '__main__':
    app.run()
