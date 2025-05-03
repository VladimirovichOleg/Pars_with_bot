import logging

from bs4 import BeautifulSoup
import requests

from env import config_file
from dict_of_path_of_tags import tags_into_a, tags_indiv_page, tags_gen_page_start
from headers_for_requests import create_headers


def check_and_get_info(bs_obj: BeautifulSoup, path):
    try:
        return eval(f"bs_obj{path}")
    except:
        return 0  # Dont use "None"


def get_price(bs_obj: BeautifulSoup, dict_of_tags: dict) -> dict:
    dict_of_price = {'price_now': check_and_get_info(bs_obj, dict_of_tags['price_now'])}
    if check_and_get_info(bs_obj, dict_of_tags['discount']):
        dict_of_price['discount'] = check_and_get_info(bs_obj, dict_of_tags['discount'])
        dict_of_price['old_price'] = check_and_get_info(bs_obj, dict_of_tags['old_price'])
    else:
        dict_of_price['discount'] = 'Скидки нет'
        dict_of_price['old_price'] = dict_of_price['price_now']
    return dict_of_price


class GetResp:
    @staticmethod
    def bs4_obj_all_page(url: str, headers_: dict):
        try:
            down_html = requests.get(url, headers=headers_)
            return BeautifulSoup(down_html.text, 'html.parser')
        except Exception as e:
            logging.error(f'{e} url - {url} don`t work ')
            return None


class GetInfoGeneralPage:
    @staticmethod
    def count_pag():
        url_start = f"{config_file['DOMAIN']}{config_file['CATALOG']}"
        first_bs4_obj = GetResp.bs4_obj_all_page(url_start, headers_=create_headers())
        if check_and_get_info(first_bs4_obj, tags_gen_page_start['pagins']):
            return int(check_and_get_info(first_bs4_obj, tags_gen_page_start['pagins']))
        else:
            return 0


class GetInfoIndividualPage:
    pass
