from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return f'Главная страничка'


@app.route('/profile/<int:user_id>')
def page_profile(user_id):
    return f'Страничка пользователя {user_id}'

app.run()