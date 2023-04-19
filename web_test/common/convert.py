import re
from typing import List, Any, Dict


def zip_dict(keys: List, values: Any) -> Dict:
    if not values:
        values = [_ for _ in values]
        values += [''] * (len(keys) - len(values))
    pairs = zip(keys, values)
    non_empty_pairs = [(key, value) for key, value in pairs if key != '']
    non_empty_keys, non_empty_values = zip(*non_empty_pairs)
    result = {key: value for key, value in zip(non_empty_keys, non_empty_values)}
    return result


def format_decimal_number_with_commas(number):
    formatted_number = f'{float(number):,}'
    return formatted_number


def string_to_binary6(input_string):
    result = ''
    for char in input_string:
        binary_string = format(ord(char), '08b')
        binary6_string = binary_string[-6:]
        result += binary6_string
    return result


def search_matching_dictionaries(dictionaries: List[Dict], dictionary: Dict) -> List:
    return [
        _
        for _ in dictionaries
        if all(
            _[__] == dictionary[__]
            for __ in dictionary
        )
    ]


def search_matching_dictionaries_with_re(dictionaries: List[Dict], dictionary: Dict) -> List:
    return [
        _
        for _ in dictionaries
        if all(
            re.search(dictionary[__], _[__])
            for __ in dictionary
        )
    ]
