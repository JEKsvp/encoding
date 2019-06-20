import app.firs_task as first
import collections


def merge(first_part, second_part):
    result = {}
    for i in range(len(first_part)):
        first_key = list(first_part.keys())[i]
        second_key = list(second_part.keys())[i]
        result[first_key] = first_part.get(first_key)
        result[second_key] = second_part.get(second_key)
    return result


def slice_from(index, symbols_codes_):
    keys = list(symbols_codes_.keys())[index::2]
    values = list(symbols_codes_.values())[index::2]
    result = collections.OrderedDict()
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result


def encode(symbols_codes_):
    first_part = slice_from(0, symbols_codes_)
    second_part = slice_from(1, symbols_codes_)

    if len(symbols_codes_) is 1:
        return symbols_codes_
    else:
        for key, value in first_part.items():
            first_part[key] = first_part[key] + '0'
        for key, value in second_part.items():
            second_part[key] = second_part[key] + '1'
        return merge(encode(first_part), encode(second_part))


def fill_empty_codes(sorted_symbols_probability_):
    result = {}
    for key, value in sorted_symbols_probability_.items():
        result[key] = ''
    return result


file = open('text.txt', mode="r", encoding="utf-8")

symbols = first.to_list(file)
symbols_probability = first.to_dict(symbols)
sorted_symbols_probability = sorted(symbols_probability.items(), key=lambda kv: kv[1], reverse=True)
sorted_symbols_probability = collections.OrderedDict(sorted_symbols_probability)
sorted_symbols_codes = fill_empty_codes(sorted_symbols_probability)
symbols_codes = encode(sorted_symbols_codes)

# average_length = calculate_average_length(symbols_codes)
print(symbols_codes)
