import csv
import json
from typing import Any

import yaml

from web_test.assist.project import abs_path_from_project


def load_json(file_path: str) -> Any:
    abs_path = abs_path_from_project(file_path)
    with open(abs_path) as f:
        json_data = json.load(f)
    return json_data


def load_yml(file_path: str) -> Any:
    abs_path = abs_path_from_project(file_path)
    with open(abs_path) as f:
        yml_data = yaml.safe_load(f)
    return yml_data


def load_csv(file_path: str) -> Any:
    abs_path = abs_path_from_project(file_path)
    with open(abs_path) as f:
        csv_data = csv.reader(f)
    return csv_data
