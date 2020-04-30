from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
@app.route('/hello_page')
def index():
    return render_template('base.html')


@app.route('/history/<int:buttons_number>')
def history(buttons_number):
    param = {}
    param['buttons_number'] = buttons_number
    #param['text'] = text
    #param['picture'] = picture
    return render_template('history2.html', **param)


@app.route('/login')
def login():
    return render_template('sing_log_in.html')


@app.route('/help_main_page')
def help_main():
    return render_template('help_main_page.html')


@app.route('/help_quiz_page')
def help_quiz():
    return render_template('help_quiz_page.html')

if __name__ == '__main__':
    app.run()
