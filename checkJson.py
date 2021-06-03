import json

lst = ['messages_20210202120106252.json', 'messages_20210202120311182.json', 'messages_20210304111841659.json',
       'messages_20210304112453094.json', 'messages_20210304112453172.json', 'messages_20210304112656850.json',
       'messages_20210304112901395.json', 'messages_20210304113106118.json', 'messages_20210304113309367.json',
       'messages_20210304113509616.json', 'messages_20210304113713174.json', 'messages_20210304113918354.json']

with open(lst[10]) as file:
    data = json.load(file)

    for decode in data:
        try:
            print('ID:', decode['ID'])
        except:
            print("Not ID")
        try:
            print('Parametro:', decode['MessageSegments'][0]['Parameters'])
            checkPar = decode['MessageSegments'][0]['Parameters']
            if not checkPar == {}:
                print('>>>>>>>>>>>>>>>>>>> Hay datos')
            else:
                print('Parametro vacio')
        except:
            print("No hay segmento de mensaje")
