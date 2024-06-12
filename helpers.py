# Prevents writing of pycache file
import sys

sys.dont_write_bytecode = True

# Standard imports
import yaml
import csv
import random
from datetime import datetime
from typing import List, Dict, Any


def write_csv(header: List[str], rows: List[List[Any]], file_name: str) -> None:
    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)


def get_address_list(filename: str, locale: str) -> List[Dict[str, Any]]:
    with open(filename, encoding="utf8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data[locale]


def get_product_list(filename: str) -> List[Dict[str, Any]]:
    with open(filename, encoding="utf8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def get_user_input(question: str, default: str) -> str:
    return input(question) or default


def get_single_product(product_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    return product_list[random.randint(0, len(product_list) - 1)]


def get_product(product_list: List[Dict[str, Any]], num: int) -> Dict[str, Any]:
    return product_list[num]


def get_single_address(address_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    return address_list[random.randint(0, len(address_list) - 1)]


def get_gift_message() -> str:
    gift_list = ("Gift Message 1", "Gift Message 2", "Gift Message 3", "Gift Message 4")
    return random.choice(gift_list)


def get_notes(text: str = 'short') -> str:
    good = (
        "Thanks for explaining the word 'many' to me, it means a lot.",
        "I can’t believe I got fired from the calendar factory. All I did was take a day off!",
        "Did you hear about the guy whose whole left side got amputated? He’s all right now.",
        "I find it ironic that the colors red, white, and blue stand for freedom until they are flashing behind you.",
        "Don’t spell part backward. It’s a trap."
    )
    short = (
        'ad', 'adipiscing', 'aliqua', 'aliquip', 'amet', 'anim', 'aute', 'cillum', 'commodo',
        'consectetur', 'consequat', 'culpa', 'cupidatat', 'deserunt', 'do', 'dolor', 'dolore',
        'duis', 'ea', 'eiusmod', 'elit', 'enim', 'esse', 'est', 'et', 'eu', 'ex', 'excepteur',
        'exercitation', 'fugiat', 'id', 'in', 'incididunt', 'ipsum', 'irure', 'labore', 'laboris',
        'laborum', 'lorem', 'magna', 'minim', 'mollit', 'nisi', 'non', 'nostrud', 'nulla',
        'occaecat', 'officia', 'pariatur', 'proident', 'qui', 'quis', 'reprehenderit', 'sed',
        'sint', 'sit', 'sunt', 'tempor', 'ullamco', 'ut', 'velit', 'veniam', 'voluptate'
    )
    bork = ("Testing «ταБЬℓσ»: 1<2 & 4+1>3, now 20%% off!")

    if text == 'good':
        return random.choice(good)
    elif text == 'short':
        return random.choice(short)
    else:
        return random.choice(bork)


def get_formatted_date() -> str:
    date = datetime.now()
    return date.strftime("%m-%d-%y")
