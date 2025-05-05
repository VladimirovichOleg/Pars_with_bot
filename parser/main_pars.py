import logging
from time import sleep
from datetime import datetime
import schedule

from get_info import GetInfoGeneralPage, GetResp, check_and_get_info
from pars_config import config_file
from headers_for_requests import create_headers
from sqlite_db import DbExecute
from dict_of_path_of_tags import tags_into_a, tags_indiv_page, tags_gen_page_start
from bot_telegram.heandlers.admin.error_pars import notify_error

logger = logging.getLogger(__name__)


def parsing():
    logger.info("main_pars is starts at %s", datetime.now())
    keramag_db = DbExecute("/home/pars_with_teleg_bot/sqlite_db/db_for_keramag.db")
    keramag_db.create_table_tile_data()
    keramag_db.create_table_users_requests()
    count_pag = GetInfoGeneralPage.count_pag()

    for number_of_page in range(1, count_pag + 1):
        sleep(1)
        url = f"{config_file['DOMAIN']}{config_file['CATALOG']}{config_file['PAGE']}{number_of_page}"
        first_bs4_obj = GetResp.bs4_obj_all_page(url, headers_=create_headers())
        tags_a = check_and_get_info(first_bs4_obj, tags_gen_page_start['main_tags_a'])
        full_inform = {}
        if tags_a:
            for a in tags_a:
                for key, value in tags_into_a.items():
                    full_inform[key] = check_and_get_info(a, value)

                if full_inform.get('in_stock') != 'В наявності':
                    logger.info("has been processed %s pages.  Data - %s", number_of_page,
                                datetime.today().strftime('%d-%m-%Y'))
                    break

                prod_avail = keramag_db.prod_availability("tile_data", full_inform)
                if not prod_avail:
                    sleep(1)
                    href_individual_page = check_and_get_info(a, tags_into_a['url_individual_page'])
                    full_inform['url_individual_page'] = f"{config_file['DOMAIN']}{href_individual_page}"
                    bs_obj_individual_page = GetResp.bs4_obj_all_page(full_inform['url_individual_page'],
                                                                      headers_=create_headers())

                    for key, value in tags_indiv_page.items():
                        full_inform[key] = check_and_get_info(bs_obj_individual_page, value)
                    keramag_db.add_prod_on_LAST_pos("tile_data", full_inform)

                else:
                    if str(prod_avail[4]) != str(full_inform['price_now']):
                        keramag_db.update_price("tile_data", full_inform)
                        logger.info("Product %s has been updated", full_inform['name'])

        else:
            notify_error(config_file['admin'], "Not find 'tags_a'")
            break

        if full_inform.get('in_stock') != 'В наявності':
            break


def main():
    try:
        print("Parsing has been started")
        parsing()
    except Exception as ex:
        print("Parsing has not been started")
        logger.error("!!! Parsing has not been started  !!! str 66 %s", ex)
        notify_error(config_file['admin'], "!!! Parsing has not been started  !!!")

    schedule.every().day.at('08:00').do(parsing)
    while True:
        try:
            schedule.run_pending()
        except Exception as ex:
            print("Parsing has been stopped")
            logger.error("!!! Parsing has been stopped !!!  %s", ex)
            notify_error(config_file['admin'], "!!! Parsing has been stopped !!!")
            break
