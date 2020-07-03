import requests
import json

def get_superhero():
    # получаем данные по суппергероям
    response_Hulk = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Hulk')
    response_Captain_America = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Captain_America')
    response_Thanos = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Thanos')

    # выводим уровень интеллекта каждого супергероя
    Hulk = response_Hulk.json()['results'][0]['powerstats']['intelligence']
    Captain_America = response_Captain_America.json()['results'][0]['powerstats']['intelligence']
    Thanos = response_Thanos.json()['results'][0]['powerstats']['intelligence']
    hero_list = [Hulk, Captain_America, Thanos]
    # print(hero_list)
    return hero_list

def get_max_intelligence():
    hero_list = get_superhero()
    # получаем словарь
    intelligence = {}
    intelligence['Hulk'] = hero_list[0]
    intelligence['Captain_America'] = hero_list[1]
    intelligence['Thanos'] = hero_list[2]

    # выводим максимальное значение
    return print(f'{max(intelligence.items(), key = lambda x: int(x[1]))[0]} - cамый умный супергерой.')

get_max_intelligence()
