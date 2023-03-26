#!/bin/bash

pkill -f allure
poetry run pytest tests --alluredir=reports "${@:1}"
allure serve reports