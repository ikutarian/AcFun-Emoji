#-*- coding:utf-8 -*-

import os
import requests


emotions = [
    {'name': 'AC娘',    'path': 'ac',        'count': 55},
    {'name': '新娘',    'path': 'ac2',       'count': 55},
    {'name': '彩娘',    'path': 'ac3',       'count': 50},
    {'name': 'AC先锋',  'path': 'blizzard',  'count': 21},
    {'name': '匿名版',  'path': 'ais',       'count': 40},
    {'name': '兔斯基',  'path': 'tsj',       'count': 40},
    {'name': '皮尔德',  'path': 'brd',       'count': 38},
    {'name': 'TD猫',    'path': 'td',        'count': 35},
    {'name': '犬娘',    'path': 'dog',       'count': 16}
]
baseUrl = 'http://cdn.aixifan.com/dotnet/20130418/umeditor/dialogs/emotion/images/{path}/{index}.gif'

for emotion in emotions:
    dir = os.path.join(os.getcwd(), 'output', emotion['name'])
    if os.path.exists(dir):
        os.rmdir(dir)
    os.makedirs(dir)
    for i in range(1, emotion['count'] + 1):
        filename = ''
        if i < 10:
            filename = '0' + str(i)
        else:
            filename = str(i)
        r = requests.get(baseUrl.format(path=emotion['path'], index=filename))
        contentType = r.headers['Content-Type']
        suffix = contentType[contentType.index('/') + 1:]
        with open(os.path.join(dir, filename + '.' + suffix), 'wb') as file:
            file.write(r.content)