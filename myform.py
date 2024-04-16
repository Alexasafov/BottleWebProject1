from bottle import post, request
import re
from datetime import datetime
import pdb
import json
import os

REGEX = r'\b[A-Za-z0-9._%+-]+@+[A-Z|a-z]+[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

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
    questions[mail] = [username, quest]
    pdb.set_trace()

    return f'''Thanks, {username}! The answer will be sent to the mail {mail}
            Access Date: {date_time}'''
        