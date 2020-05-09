from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
from flask import request
from random import randint
import sqlite3

app = Flask(__name__)
run_with_ngrok(app)

global n, ger, sov, usa, pressed_button, finish, rar_ivent, flag
n = []
ger = []
sov = []
usa = []
finish = []
rar_ivent = []
pressed_button = 0
flag = []


# коды рарных ивентов
# 1488 - база нацистов в антарктиде
# 1234 - ядерная бомба


@app.route('/')
@app.route('/hello_page')
def index():
    return render_template('base.html')


@app.route('/history_welcome')
def history_one():
    return render_template('history1.html')


@app.route('/history', methods=['GET', 'POST'])
def history():
    pressed_button = request.args.get('answer', default=0,
                                      type=int)  # какая кнопка была нажата последней
    picture_address, buttons_count, text, text_button, flag, final_text = data_base(
        pressed_button)
    if len(flag) == 1:
        param = {}
        param['points_USA'] = len(usa)  # очики Омерики
        param['points_RUSSIA'] = len(sov)  # очки Русских
        param['points_GERMANY'] = len(ger)  # очки Ненцев
        param['final_text'] = finish
        return render_template('final.html', **param)
    else:
        param = {}
        param['buttons_count'] = int(buttons_count)
        param['text'] = str(text)
        param['picture_address'] = picture_address
        param['pressed_button'] = pressed_button
        param['text_button'] = text_button
        param['final_flag'] = flag
        param['final_text'] = finish
        return render_template('history2.html', **param)


def data_base(
        pressed_button):  # должна прочитать базу данных, вернуть ссылку на картинку, кол-во кнопок и текст
    if len(n) == 1:
        print(pressed_button)
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            usa.append(1)
            usa.append(1)
        elif pressed_button == 4:
            ger.append(1)
            ger.append(1)
    elif len(n) < 6:
        print(pressed_button)
        if len(n) == 2:
            if pressed_button == 2:
                finish.append("Самолет не полетел")
        elif pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 6:
        if pressed_button == 1:
            ger.append(1)
            rar_ivent.append(1488)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 7:
        if pressed_button == 1:
            ger.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 8:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 9:
        if pressed_button == 1:
            usa.append(1)
            usa.append(1)
        elif pressed_button == 3:
            ger.append(1)
    elif len(n) == 10:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            finish.append(
                "Первая мировая в вашем мире все равно началась, но под другим предлогом")
    elif len(n) == 11:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            ger.append(1)
            finish.append(
                "Франция в пмв была сокрушена и пошла на перемирие вместе с Великообританией")
            for k in range(3):
                n.append(1)
        elif pressed_button == 3:
            usa.append(1)
            usa.append(1)
            for k in range(3):
                n.append(1)
    elif len(n) == 12:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            usa.append(1)
            usa.append(1)
    elif len(n) == 13:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            sov.append(1)
            sov.append(1)
    elif len(n) == 14:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            ger.append(1)
            ger.append(1)
        elif pressed_button == 3:
            usa.append(1)
            usa.append(1)
    elif len(n) == 15:
        if pressed_button == 1:
            usa.append(1)
            for elem in sov:
                if elem == sov[-1]:
                    del sov[-1]
            finish.append(
                "Россия не вышла из войны и  стала державой-победителем")
        elif pressed_button == 2:
            ger.append(2)
            finish.append("Брестский мир был заключен")
        elif pressed_button == 3:
            usa.append(1)
            usa.append(1)
            for elem in sov:
                if elem == sov[-1]:
                    del sov[-1]
        elif pressed_button == 4:
            usa.append(1)
            usa.append(1)
            sov.clear()
            finish.append(
                "Россия перестала существовать ка централизованное государство")
    elif len(n) == 16:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 17:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
        elif pressed_button == 3:
            sov.append(1)
            sov.append(1)
    elif len(n) == 18:
        if pressed_button == 1:
            ger.append(1)
        elif pressed_button == 2:
            sov.append(1)
    elif len(n) == 19:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            sov.append(1)
        elif pressed_button == 3:
            ger.append(1)
            sov.append(1)
    elif len(n) == 20:
        if pressed_button == 1:
            usa.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            ger.append(1)
            ger.append(1)
    elif len(n) == 21:
        if pressed_button == 2:
            ger.append(1)
            rar_ivent.append(1488)
    elif len(n) == 22:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            sov.append(1)
    elif len(n) == 23:
        if pressed_button == 2:
            ger.append(1)
            rar_ivent.append(1234)
    elif len(n) == 24:
        if pressed_button == 1:
            usa.append(1)
            sov.append(1)
            sov.append(1)
            finish.append(
                "Гитлер был смещен в самом начале своего правления, но это не спасло Европу от грядущей войны")
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            ger.append(1)
    elif len(n) == 25:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
            usa.append(1)
    elif len(n) == 26:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            ger.append(1)
            usa.append(1)
    elif len(n) == 27:
        if pressed_button == 1:
            sov.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 28:
        if pressed_button == 1:
            sov.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 29:
        print(pressed_button, 1488)
        if pressed_button == 1:
            sov.append(1)
            usa.append(1)
            finish.append(
                "Германский рейх уничтожили в зачатке соединенные силы Франции и Великобритании")
            for k in range(34):
                n.append(1)
            print(len(n))
        elif pressed_button == 2:
            finish.append("Германия захватила Австрию")
            ger.append(1)
            ger.append(1)
            ger.append(1)
    elif len(n) == 30:
        if pressed_button == 1:
            sov.append(1)
            usa.append(1)
            finish.append(
                "Франция не рассчитала свои силы - новая война спровоцировала революцию внутри страны")
            finish.append(
                "Третий рейх получил все ресурсы Европы и выгодно заключил мир.Дальнейшая судьба мира не завидна")
            flag.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
    elif len(n) == 31:
        if pressed_button == 1:
            sov.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            ger.append(1)
            ger.append(1)
    elif len(n) == 32:
        if pressed_button == 1:
            usa.append(1)
            ger.append(1)
            finish.append("Пакт Молотова-Риббентропа не был заключен")
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            sov.append(1)
            finish.append("Пакт Молотова-Риббентропа был заключен")
    elif len(n) == 33:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
    elif len(n) == 34:
        if pressed_button == 1:
            sov.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            ger.append(1)
            ger.append(1)
    elif len(n) == 35:
        if pressed_button == 1:
            usa.append(1)
            usa.append(1)
            usa.append(1)
            finish.append(
                "Германский рейх уничтожили в считанные месяцы соединенные силы Франции и Великобритании")
            while len(n) != 62:
                n.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 36:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 37:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
        elif pressed_button == 3:
            ger.append(1)
            ger.append(1)
            ger.append(1)
    elif len(n) == 38:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            finish.append(
                "Скорее всего, за потерей всей английской армии, последовала бы неминуемая"
                " высадка на туманный альбион, которая привела бы к ужаснейшим последствиям для человечества")
            flag.append(1)
        elif pressed_button == 3:
            ger.append(1)
            ger.append(1)
            ger.append(1)
            finish.append(
                "Германия заключила крайне выгодный для себя мир и теперь господствует над всем миром")
            flag.append(1)
    elif len(n) == 39:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            ger.append(1)
    elif len(n) == 40:
        if pressed_button == 1:
            usa.append(1)
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
        elif pressed_button == 3:
            ger.append(1)
    elif len(n) == 41:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            ger.append(1)
            ger.append(1)
    elif len(n) == 42:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
    elif len(n) == 43:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            ger.append(1)
    elif len(n) == 44:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
            ger.append(1)
            ger.append(1)
            ger.append(1)
    elif len(n) == 45:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 46:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)  #
    elif len(n) == 47:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 48:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 3:
            ger.append(1)
            flag.append(1)
            finish.append(
                'Воздух настолько очистился, что в иерусалим вернулись крестоносцы и зхватили полмира')
        elif pressed_button == 3:
            ger.append(1)
            flag.append(1)
            finish.append(
                'Весь мир теперь принадлежит итальянским крестоносцам!!!AVE MARIA')
    elif len(n) == 49:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 50:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 51:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 52:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 53:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 54:
        if pressed_button == 1:
            usa.append(1)
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 55:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 55:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
    elif len(n) == 56:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 57:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
    elif len(n) == 58:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
        elif pressed_button == 2:
            usa.append(1)
            usa.append(1)
    elif len(n) == 59:
        if pressed_button == 1:
            usa.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
            ger.append(1)
    elif len(n) == 60:
        if pressed_button == 1:
            usa.append(1)
            sov.append(1)
            ger.clear()
        elif pressed_button == 2:
            usa.append(1)
            usa.append(1)
            ger.clear()
        elif pressed_button == 3:
            sov.append(1)
            sov.append(1)
            ger.clear()
    elif len(n) == 61:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 62:
        if pressed_button == 1:
            usa.append(1)
    elif len(n) == 64:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
            usa.append(1)
    elif len(n) == 66:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 3:
            usa.append(1)
    elif len(n) == 67:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 68:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 69:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 70:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
        elif pressed_button == 3:
            usa.append(1)
    elif len(n) == 71:
        if pressed_button == 1:
            ger.append(1)
            ger.append(1)
            ger.append(1)
    elif len(n) == 72:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 73:
        if pressed_button == 1:
            sov.append(1)
            sov.append(1)
    elif len(n) == 75:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            sov.append(1)
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 76:
        if pressed_button == 2:
            usa.append(1)
    elif len(n) == 77:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 78:
        if pressed_button == 1:
            usa.append(1)
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 79:
        if pressed_button == 1:
            flag.append(1)
            finish.append('Произошел ядерный апокалипсис!!!!!')
        elif pressed_button == 2:
            flag.append(1)
            finish.append('Произошел ядерный апокалипсис!!!!!')
    elif len(n) == 80:
        if pressed_button == 1:
            sov.append(1)
    elif len(n) == 81:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 82:
        if pressed_button == 1:
            sov.append(1)
    elif len(n) == 83:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            usa.append(1)
        elif pressed_button == 3:
            flag.append(1)
            finish.append(
                'Лунные нацисты принесли на землю террор и танцы из фортанайта!!!!!')
    elif len(n) == 84:
        if pressed_button == 1:
            sov.append(1)
    elif len(n) == 85:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
            usa.append(1)
    elif len(n) == 86:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 87:
        if pressed_button == 1:
            flag.append(1)
            finish.append(
                'CCCР не разваливается и холодная война продолжается вплоть до нащих дней')
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 88:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
    elif len(n) == 91:
        if pressed_button == 1:
            usa.append(1)
            usa.append(1)
        elif pressed_button == 2:
            ger.append(1)
    elif len(n) == 92:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            usa.append(1)
            usa.append(1)
    elif len(n) == 93:
        if pressed_button == 1:
            usa.append(1)
            sov.clear()
        elif pressed_button == 2:
            usa.append(1)
            usa.append(1)
            sov.clear()
    elif len(n) == 94:
        if pressed_button == 2:
            usa.append(1)
            usa.append(1)
    elif len(n) == 95:
        if pressed_button == 2:
            usa.append(1)
    elif len(n) == 96:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 2:
            flag.append(1)
            finish.append(
                'CCCР был возрожден, но зачем и в каком виде - неясно')
    elif len(n) == 97:
        if pressed_button == 1:
            usa.append(1)
    elif len(n) == 98:
        if pressed_button == 1:
            sov.append(1)
        elif pressed_button == 2:
            sov.append(1)
            sov.append(1)
        elif pressed_button == 3:
            flag.append(1)
            finish.append(
                'КОСМОДЕСАНТ ВЫСАДИЛСЯ НА ЗЕМЛЮ И ПРИСОЕДЕНИЛ ЕЕ К ИМПЕРИМУ.ЖГИ ЕРЕСЬ!!!!')
    elif len(n) == 99:
        if pressed_button == 1:
            flag.append(1)
            finish.append(
                'CCCР был возрожден, но зачем и в каком виде - неясно')
        elif pressed_button == 2:
            usa.append(1)
            flag.append(1)
            finish.append(
                'Россия в своем стандартном и историческом варианте выбрала Ельцина в 95')
    elif len(n) == 100:
        if pressed_button == 1:
            usa.append(1)
        elif pressed_button == 3:
            ger.append(1)
            finish.append('Немецкий блицкриг на тарелках не остановим')
        elif pressed_button == 4:
            finish.append(
                'Ваша шапочка из фольги лежит в тумбочке слева от вас')

    bds = sqlite3.connect("main.db")
    ks = bds.cursor()
    n.append(1)
    result = ks.execute("""SELECT * FROM ww2
                    WHERE id""").fetchmany(len(n))
    fg = 0
    count_button = 4
    ss = []
    for elem in result:
        if elem == result[-1]:
            for el in elem:
                if el is None:
                    count_button -= 1
                else:
                    if fg == 0:
                        text = el
                    if fg > 0 and fg < 5:
                        ss.append(el)
                    if fg == 5:
                        im = el
                fg += 1
    picture_address = "/static/img/" + str(im) + '.jpg'  # ссылку на картинку
    buttons_count = count_button  # кол-во кнопок
    text_button = ss  # текст на кнопках

    final_text = 'финальные слова'  # ТЕКСТ ДЛЯ ФИНАЛА

    return picture_address, buttons_count, text, text_button, flag, final_text


@app.route('/login')
def login():
    return render_template('sing_log_in.html')


@app.route('/help_main_page')
def help_main():
    return render_template('help_main_page.html')


@app.route('/help_quiz_page')
def help_quiz():
    return render_template('help_quiz_page.html')


@app.route('/rules')
def rule():
    return render_template('rules.html')


if __name__ == '__main__':
    app.run()
