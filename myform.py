from bottle import post, request
import re
from datetime import datetime

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    date_time = datetime.now().strftime("%Y-%m-%d")
    if quest == "" or mail == "" or username == "":
        return "Not all fields filled"
    elif not re.fullmatch(regex, mail):
        return "Invalid mail"
    else:
        return f'''Thanks, {username}! The answer will be sent to the mail {mail}
            Access Date: {date_time}'''