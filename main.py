import powerp
import uuploader
import apiapi
from pprint import pprint

if __name__ == '__main__':
    # Задания 1
    
    search_hero = ['Hulk', 'Captain America', 'Thanos']
    power = 'intelligence'
    results = powerp.search_power_get(search_hero, power)
    pprint(results)
    max_power = {'id': 0, 'name': 'none', power: 0}
    for hero in results:
        if max_power[power] < hero[power]:
            max_power = hero
    print(f'\nГерой {max_power["name"]} с максимальным уровнем {power} = {max_power[power]}.')

    print()
    # Задания 2

    path_to_file = "download"
    token = uuploader.token
    uploader = uuploader.YaUploader(token)
    uploader.create_folder(path_to_file)
    uploader.upload(path_to_file)

    print()
    # Задания 3

    apiapi.search_tag(2, 'python')
