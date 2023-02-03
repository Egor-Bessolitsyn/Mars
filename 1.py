from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.gif')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <p><b>Человечество вырастает из детства.</b></p>
                    <p><b>Человечеству мала одна планета.</b></p>
                    <p><b>Мы сделаем обитаемыми безжизненные пока планеты.</b></p>
                    <p><b>И начнем с Марса!</b></p>
                    <p><b>Присоединяйся!</b></p>
                  </body>
                </html>"""


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
