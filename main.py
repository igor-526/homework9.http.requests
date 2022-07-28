import os
import requests

def menu(choise):
    while choise != 'q':
        print('1. Показать самого умного супергероя')
        print('2. Записать файлы на Яндек.Диск')
        print('q. Выход из программы')
        choise = input('Выберите пункт: ')
        if choise == '1':
            print()
            print(f'Имя самого умного супергероя: {most_intelligence_superhero()["name"]}, его интеллект: {most_intelligence_superhero()["intelligence"]}')
            print()
        elif choise == '2':
            print()
            write_to_yandexdisk()
            print()
        else:
            if choise != 'q':
                print('Вы выбрали несуществующий пункт меню! Попробуйте ещё раз!')
                print()
    else:
        print('До свидания!')

def most_intelligence_superhero():
    def getintelligence(hero):
        return (hero['intelligence'])
    superheroes = []
    superheroes_sorted = []
    request = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    for superhero in (request.json()):
        superheroes.append({'name': superhero['name'], 'intelligence': superhero['powerstats']['intelligence']})
    superheroes_sorted = sorted(superheroes, key=getintelligence)
    return (superheroes_sorted[-1])
def new_yandextoken():
    with open('token.txt', 'w') as token:
        token.write(input("Введите Ваш токен: "))
    print('Новый токен успешно записан')
    write_to_yandexdisk()
def write_to_yandexdisk():
    if (os.path.exists('token.txt')) == False:
        print("Нет данных о токене авторизации для Яндекс.Диск")
        new_yandextoken()
    else:
        if input('использовать существующий токен (y) или записать новый (n)? ') == "n":
            new_yandextoken()
        else:
            print("выполняем")



if __name__ == '__main__':
    menu(0)