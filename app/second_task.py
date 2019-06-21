import app.firs_task as first
import math


def fill_empty_codes(sorted_symbols_probability_):
    for i in range(len(sorted_symbols_probability_)):
        sorted_symbols_probability_[i] = list(sorted_symbols_probability[i])
        sorted_symbols_probability_[i].append('')


def calculate_max_probability(sorted_symbols_probability_):
    result = 0
    for item in sorted_symbols_probability_:
        result = result + item[1]
    return result


def divide_by_probability(sorted_symbols_probability_):
    first_part = []
    second_part = []
    max_probability = calculate_max_probability(sorted_symbols_probability_)
    current_probability = 0
    for item in sorted_symbols_probability_:
        if current_probability < max_probability / 2:
            item[2] = item[2] + '0'
            first_part.append(item)
        else:
            second_part.append(item)
            item[2] = item[2] + '1'
        current_probability = current_probability + item[1]
    return [first_part, second_part]


def encode(sorted_symbols_probability_):
    if len(sorted_symbols_probability_) is 1:
        return sorted_symbols_probability_
    else:
        first_part, second_part = divide_by_probability(sorted_symbols_probability_)
        return encode(first_part) + encode(second_part)


def calculate_average_length_by_formula(symbols_with_codes_):
    result = 0
    for item in symbols_with_codes_:
        result = result + item[1] * len(item[2])
    return result


def to_dict(symbols_with_codes_):
    result = {}
    for item in symbols_with_codes_:
        result[item[0]] = item[2]
    return result


def calculate_encoded_length(symbols_with_codes_):
    encoded_length = 0
    symbols_with_codes_dict = to_dict(symbols_with_codes_)
    for symbol in symbols:
        encoded_length = encoded_length + len(symbols_with_codes_dict[symbol])
    return encoded_length


def calculate_average_length(symbols_with_codes_, symbols_):
    return calculate_encoded_length(symbols_with_codes_) / len(symbols_)


file = open('text.txt', mode="r", encoding="utf-8")

symbols = first.to_list(file)
symbols_probability = first.to_dict(symbols)
sorted_symbols_probability = sorted(symbols_probability.items(), key=lambda kv: kv[1], reverse=True)
fill_empty_codes(sorted_symbols_probability)
symbols_with_codes = encode(sorted_symbols_probability)
print(symbols_with_codes)

average_length_by_formula = calculate_average_length_by_formula(symbols_with_codes)
print('Средняя длина кодового слова (по формуле) = ' + str(average_length_by_formula))

average_length = calculate_average_length(symbols_with_codes, symbols)
print('Средняя длина кодового слова = ' + str(average_length))

min_average_length = first.calculate_entropy(symbols_probability.values()) / math.log2(2)
print('Минимальная средняя длина кодового слова = ' + str(min_average_length))

encoded_length = calculate_encoded_length(symbols_with_codes)
print('Количество бит закодированного текста методом Шеннона-Фано = ' + str(encoded_length))
print('Коэффициент сжатия = ' + str(len(symbols) / encoded_length))
