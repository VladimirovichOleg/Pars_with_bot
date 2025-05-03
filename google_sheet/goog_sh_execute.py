import logging
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

logger = logging.getLogger()

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = '/home/oleg/python_progect/keramag/google_sheet/creds.json'  # /home/pars_with_teleg_bot/google_sheet/creds.json
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = 'example'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http=httpAuth)


def add_data_on_g_sh(val_s: dict, pos: int):
    try:
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "valueInputOption": "RAW",
                "data": [
                    {"range": f"A{pos}",
                     "majorDimension": "ROWS",
                     "values": [[str(data) for data in val_s.values()]]}
                ]
            }
        ).execute()
    except Exception as ex:
        logger.error("error add_data_on_g_sh %s", ex)


def update_price_g_sh(val_s: dict, pos: int) -> None:
    try:
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "valueInputOption": "RAW",
                "data": [
                    {"range": f"C{pos}",
                     "majorDimension": "ROWS",
                     "values": [[str(data) for data in val_s.values()]]}
                ]
            }
        ).execute()
    except Exception as ex:
        logger.error("update_price_g_sh %s", ex)


def insert_row_on_g_sh(val_s: dict):
    try:
        body = {
            'requests': [
                {
                    'insertRange': {
                        'range': {
                            'sheetId': 0,  # ID листа
                            'startRowIndex': 0,  # Начальный индекс строки для вставки
                            'endRowIndex': 1  # Конечный индекс строки для вставки
                        },
                        'shiftDimension': 'ROWS'  # Сдвиг строк вниз
                    }
                },
                {
                    'updateCells': {
                        'rows': {
                            'values': [
                                {'userEnteredValue': {'stringValue': str(value)}} for value in val_s.values()
                            ]
                        },
                        'fields': 'userEnteredValue',
                        'start': {
                            'sheetId': 0,  # ID листа
                            'rowIndex': 0,  # Индекс строки для вставки данных
                            'columnIndex': 0  # Индекс столбца для вставки данных
                        }
                    }
                }
            ]
        }
        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()
    except Exception as ex:
        logger.error("insert_row_on_g_sh %s", ex)
