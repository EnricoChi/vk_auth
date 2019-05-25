import urllib3
import json

from webim.settings import VK_OAUTH2_TOKEN

token = f'access_token={VK_OAUTH2_TOKEN}'
method = 'friends.get'
http = urllib3.PoolManager()
url = 'https://api.vk.com/method'


def get_vk_friends(vk_id):
    fields = 'fields=photo_100,first_name'
    parameter = f'user_id={vk_id}'
    order = 'order=random'
    count = 'count=5'
    lang = 'lang=ru'
    path = f'{url}/{method}?{parameter}&{order}&{count}&{fields}&{lang}&{token}&v=V'
    request = http.request('GET', path)
    return json.loads(request.data.decode('utf-8'))
