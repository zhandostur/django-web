import requests
from .models import TeleSettings




def send_telegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=2)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    part_1 = text[0:text.find('{')]
    part_2 = text[text.find('}')+1:text.rfind('{')]
    part_3 = text[text.rfind('}'):-1]
    text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slise,
    })

