import os
import unittest
from flask import Flask

# Импортируем модуль, который хотим протестировать
import code.py

class YourAppTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр приложения Flask
        self.app = your_module_name.create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def tearDown(self):
        # Удаление созданного файла после каждого теста
        if os.path.exists('anketa.txt'):
            os.remove('anketa.txt')

    def test_index(self):
        # Отправляем GET-запрос на главную страницу
        response = self.client.get('/')
        
        # Проверяем, что ответ имеет код 200 (успех) и содержимое шаблона
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Содержимое шаблона')
       #Преобразует "response.data" в строку Unicode, используя кодировку UTF-8

    def test_submit(self):
        # Отправляем POST-запрос на страницу '/submit' с данными формы
        response = self.client.post('/submit', data={
            'name': 'Иван Иванов',
            'data_rojdenia': '01-01-1990',
            'today': '09-06-2023',
            'favorite_color': 'синий',
            'favorite_games': 'Шахматы',
            'summer': 'Путешествия',
            'age': '33',
            'about_me': 'Я люблю программирование'
        })

        # Проверяем, что ответ имеет код 200 (успех) и возвращает сообщение об успешной записи
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Данные успешно записаны в файл!')

        # Проверяем, что файл "anketa.txt" был создан и содержит ожидаемые данные
        with open('anketa.txt', 'r') as file:
            file_data = file.read()

        expected_data = '''Имя: Иван Иванов
Дата рождения: 01-01-1990
Сегодняшняя дата: 09-06-2023
Любимый цвет: синий
Любимые игры: Шахматы
Планы на лето: Путешествия
Возраст: 33
О себе: Я люблю программирование\n'''

        self.assertEqual(file_data, expected_data)

if _name_ == '_main_':
    unittest.main()
