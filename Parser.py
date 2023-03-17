from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://auto.drom.ru/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allCars = soup.findAll('div', class_='css-13ocj84 e1icyw250')
    description = ""
    for cars in allCars:
        if cars.find('div'):
            description += cars.text + '\n'
    print(description)
    save_result_in_file(description)


def save_result_in_file(cars):
    file = open("cars.txt", "w")
    file.write(cars)
    file.close()
