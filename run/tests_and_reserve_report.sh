#!/bin/bash

pkill -f allure
pytest tests --alluredir=reports "${@:1}"
allure serve reports