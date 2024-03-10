from django.http import HttpResponse
from datetime import datetime
import calendar

def weekdays(request, lang):
    weekdays = {
        'uz': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
        'en': list(calendar.day_name),
        'ru': list(calendar.day_name),
        'all': {'uz': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
                'en': list(calendar.day_name),
                'ru': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']}
    }
    if lang in weekdays:
        if lang == 'all':
            response = "<h1>Weekdays in All Languages:</h1><br>"
            for key, value in weekdays['all'].items():
                response += f"<h2>{key.upper()}:</h2>"
                response += "<ul>"
                for day in value:
                    response += f"<li>{day}</li>"
                response += "</ul>"
        else:
            response = "<h1>Weekdays:</h1><br>"
            response += "<ul>"
            for day in weekdays[lang]:
                response += f"<li>{day}</li>"
            response += "</ul>"
    else:
        response = "<h1>Invalid Language!</h1>"
    return HttpResponse(response)
