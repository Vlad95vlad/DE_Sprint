import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
import time

data = {
    "data": []
}

for page in range(1, 3):
    url = f"https://www.avito.ru/all/vakansii?cd=1&p={page}&q=python"
    resp = req.get(url)  # Запрос сайта

    #print(resp.text)  # Вывод текста html сайта
    # Обрабатываем html код
    soup = BeautifulSoup(resp.text,  # Текст, из которого будем вычленять
                         "lxml")     # Формат, который будем вычленять

    tags = soup.find_all(attrs={"data-marker":"item-title"})
    for iter in tqdm.tqdm(tags):
        #print(iter.text, iter.attrs["href"])
        time.sleep(2)
        url_object = "https://www.avito.ru" + iter.attrs["href"]

        resp_object = req.get(url_object)  # Запрос сайта
        soup_pbject = BeautifulSoup(resp_object.text, "lxml")
        tag_price = soup_pbject.find_all(attrs={"itemprop": "offers"}).find(attrs={"itemprop": "price"}).text
        #print(iter.text, tag_price)

        tag_region = soup_pbject.find(attrs={"itemtype": "http://schema.org/ListItem"}).find_all(attrs={"itemprop": "name"})[0].text

        data["data"].append({"Title": iter.text, "Salary": tag_price, "Region": tag_region})
        #print(iter.text, tag_price, tag_region)

    with open("data.json", "w") as file:
        json.dump(data, file, ensure_ascii=False)


