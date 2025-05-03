#!/bin/bash

# Создание и запуск screen-сессии для 'bot'
screen -dmS bot bash -c '
    source /home/pars_with_teleg_bot/venvBot_Pars/bin/activate;
    export PYTHONPATH=$PYTHONPATH:/home/pars_with_teleg_bot/;  # Активация виртуального окружения
    python3.12 /home/pars_with_teleg_bot/bot_telegram/bot_run.py;  # Запуск Python-скрипта
    exec bash
'

# Создание и запуск screen-сессии для 'pars'
screen -dmS pars bash -c '
    source /home/pars_with_teleg_bot/venvBot_Pars/bin/activate;  # Активация виртуального окружения
    export PYTHONPATH=$PYTHONPATH:/home/pars_with_teleg_bot/;  # Установка PYTHONPATH
    python3.12 /home/pars_with_teleg_bot/parser_/main.py;  # Запуск Python-скрипта
    exec bash
'

echo "Скрипты запущены в screen сессиях 'bot' и 'pars'."

