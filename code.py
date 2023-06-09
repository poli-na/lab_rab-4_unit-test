import os
from flask import Flask, render_template, request

# Указываем путь к папке templates
template_dir = os.path.abspath('templates')

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('шаблон.html')

    @app.route('/submit', methods=['POST'])
    def submit():
        name = request.form.get('name')
        data_rojdenia = request.form.get('data_rojdenia')
        today = request.form.get('today')
        favorite_color = request.form.get('favorite_color')
        favorite_games = request.form.get('favorite_games')
        summer = request.form.get('summer')
        age = request.form.get('age')
        about_me = request.form.get('about_me')

        # Здесь можно выполнить дополнительную обработку данных анкеты

        # Открываем файл "anketa.txt" в режиме записи и сохраняем данные анкеты
        with open('anketa.txt', 'w') as file:
            file.write(f'Имя: {name}\n')
            file.write(f'Дата рождения: {data_rojdenia}\n')
            file.write(f'Сегодняшняя дата: {today}\n')
            file.write(f'Любимый цвет: {favorite_color}\n')
            file.write(f'Любимые игры: {favorite_games}\n')
            file.write(f'Планы на лето: {summer}\n')
            file.write(f'Возраст: {age}\n')
            file.write(f'О себе: {about_me}\n')

        return 'Данные успешно записаны в файл!'

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
