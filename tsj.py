#-*- coding:utf-8 -*-

import requests

for i in range(1, 41):
    baseUrl = 'http://cdn.aixifan.com/dotnet/20130418/umeditor/dialogs/emotion/images/tsj/{index}.gif'
    fileName = ''
    if i < 10:
        fileName = '0' + str(i)
    else:
        fileName = str(i)
    r = requests.get(baseUrl.format(index=fileName))
    contentType = r.headers['Content-Type']
    suffix = contentType[contentType.index('/') + 1:]
    with open('/tsj/' + fileName + '.' + suffix, 'wb') as file:
        file.write(r.content)