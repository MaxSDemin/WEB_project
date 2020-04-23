from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello_page')
def index():
    return render_template('base.html')


@app.route('/history')
def history():
    return render_template('history2.html')


@app.route('/login')
def login(buttons_number, text, pict, n_pict):
    param = {}
    param['buttons_number'] = buttons_number
    param['text'] = text
    param['pict'] = pict
    param['n_pict'] = n_pict
    return render_template('sing_log_in.html', **param)


@app.route('/help_main_page')
def help_main():
    return render_template('help_main_page.html')


@app.route('/help_quiz_page')
def help_quiz():
    return render_template('help_quiz_page.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
