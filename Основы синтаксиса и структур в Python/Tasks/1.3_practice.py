import requests as req
from bs4 import BeautifulSoup
import json
import time


# 1. Парсинг данных о вакансиях python разработчиков с сайта hh.ru
def parsing():
    data = {
        "data": []
    }

    url = 'https://api.hh.ru/vacancies'
    for page in range(10):
        par = {'text': ["python developer"], 'area': '113', 'per_page': '10', 'page': page}
        r = req.get(url, params=par)
        id_vac = [i['id'] for i in r.json()['items']]
        for i in id_vac:
            url_vac = f'https://api.hh.ru/vacancies/{i}'
            vac = req.get(url_vac)
            vac = vac.json()
            try:
                tmp = []
                if vac['salary']['from'] is not None:
                    tmp.append(f"От {vac['salary']['from']}")
                else:
                    tmp.append("")
                if vac['salary']['to'] is not None:
                    tmp.append(f"до {vac['salary']['to']}")
                else:
                    tmp.append("")
            except:
                tmp = ["", ""]

            data['data'].append({"Title": vac['name'],
                                 "Work experience": vac['experience']['name'],
                                 "Salary": f"{tmp[0]} {tmp[1]}",
                                 "Region": vac['area']['name']})

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)


parsing()


# 2. Палиндром строки
def palindrom(string: str) -> bool:
    string = string.replace(" ", "")
    if string == string[::-1]:
        return True

    return False


print("Тест задания 2.")
for itr in ["taco cat", "rotator", "black cat"]:
    print(palindrom(itr))


# 3. Перевод арабского числа в римское
def arab_to_rom(num: int) -> str:
    result = ""
    for arab, rom in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                         'M CM D CD C XC L XL X IX V IV I'.split()):
        result += (num // arab) * rom
        num %= arab

    return result


print("\nТест задания 3.")
for itr in [3, 10, 13, 20, 40, 90, 588, 1964]:
    print(itr, arab_to_rom(itr))


# 4. Валидность скобок
def bracets(string: str) -> bool:
    br_dict = {"]": "[", ")": "(", "}": "{"}
    br_stack_list = []

    for i in string:
        if i in "[({":
            br_stack_list.append(i)
        else:
            if br_stack_list.pop() != br_dict[i]:
                return False
    return not br_stack_list


print("\nТест задания 4.")
for itr in ("[{}({})]", "{]", "{", "[()]{}", "{{{}"):
    print(itr, bracets(itr))


# 5. Умножить два бинарных числа в формате строк
def bin_mul(x1: str, x2: str) -> str:
    multiplication = int(x1, 2) * int(x2, 2)
    binary_mul = bin(multiplication)

    return str(binary_mul)[2:]


print("\nТест задания 5.")
for itr in (("111", "101"), ("000", "11101")):
    print(bin_mul(itr[0], itr[1]))
