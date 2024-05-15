from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse
from telepot import Bot


def send_message(message):
    bot = Bot(token='7020375331:AAF6EenHlh2UdL0OYrPMfR5ynJs0Jw2gRmE')
    bot.sendMessage(476874543, message)

@csrf_exempt
def tg_send(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        number = request.POST.get('number')
        message_template = f'''Ім'я {name}
        email {email},
        Номер телефону {number}
        Повідомлення {message}
        '''
        if message:
            send_message(message_template)
        return HttpResponse('...')
    else:
        return HttpResponseBadRequest('ONLY POST REQUESTS')

