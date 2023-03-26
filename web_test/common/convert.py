def zip_dict(keys, values):
    if not values:
        values += [''] * (len(keys) - len(values))
    pairs = zip(keys, values)
    non_empty_pairs = [(key, value) for key, value in pairs if key != '']
    non_empty_keys, non_empty_values = zip(*non_empty_pairs)
    result = {key: value for key, value in zip(non_empty_keys, non_empty_values)}
    return result


def format_decimal_number_with_commas(number):
    formatted_number = f'{float(number):,}'
    return formatted_number
