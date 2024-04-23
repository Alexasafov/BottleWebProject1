from bottle import post, request
import re
from datetime import datetime
import json
import os

REGEX = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
WRITEPATH = 'questions.json'

def add_if_not_exist(list, el):
     if el not in list:
        return list + [el]
     return list

questions = {}

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    date_time = datetime.now().strftime("%Y-%m-%d")

    if quest == "" or mail == "" or username == "":
        return "Not all fields filled"
    if not re.fullmatch(REGEX, mail):
        return "Invalid mail"
    # длина вопроса не может быть меньше 4 символов
    # вопрос не может состоять только из цифр
    if len(quest) <= 3 or quest.isdigit():
        return "Error: Invalid question."
    
    # создаем файл если его нет
    if not os.path.exists(WRITEPATH):
        with open(WRITEPATH, 'a+') as json_file:
            json.dump({}, json_file) 
    with open(WRITEPATH, 'r+') as json_file:
        questions = json.load(json_file)
        # добавляем вопрос если его нет в списке
        questions[mail] = add_if_not_exist(questions.get(mail, []), quest)
        # перезаписываем файл с новыми файлами
        json_file.seek(0)
        json.dump(questions, json_file)

    return f'''Thanks, {username}! The answer will be sent to the mail {mail}
            Access Date: {date_time}'''
