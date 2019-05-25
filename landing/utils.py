import urllib3
import json

token = 'access_token=bce13776bce13776bce137760dbc8b8811bbce1bce13776e006e030b1e98ac6acea6d39'
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
