import json
import requests


for i in range(1, 2):
    url = f'https://cricketapi-icc.pulselive.com/fixtures?matchTypes=OTHER,T20I,T20,TEST,ODI,FIRST_CLASS,' \
          f'LIST_A&tournamentTypes=I&teamTypes=b,m&matchStates=C&page={i}&pageSize=10'
    response = requests.get(url)
    print(type(response.text))
    context = json.loads(response.text)
    print(type(context['content']))

    for data in context['content']:
        for key, value in data.items():
            print(f"{key}- {value}")
            if value is dict():
                print("__________True_____________")