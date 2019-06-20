import math

file = open('text.txt', mode="r", encoding="utf-8")


def to_list(file_):
    symbols_ = []
    for symbol in file_.read():
        symbols_.append(symbol)
    return symbols_


def to_dict(symbols_):
    result = {}
    for symbol in symbols_:
        if result.get(symbol):
            result[symbol] = result[symbol] + 1
        else:
            result[symbol] = 1
    for symbol, count in result.items():
        result[symbol] = count / len(symbols_)
    return result


def calculate_entropy(probabilities):
    result = 0
    for prob in probabilities:
        result = result - (prob * math.log2(prob))
    return result


def calculate_max_entropy(pow_):
    probabilities = []
    for i in (range(pow_)):
        probabilities.append(1 / pow_)
    return calculate_entropy(probabilities)


def calculate_redundancy(max_entropy_, entropy_):
    return (max_entropy_ - entropy_) / max_entropy_


symbols = to_list(file)
symbols_probability = to_dict(symbols)
print(symbols_probability)

entropy = calculate_entropy(symbols_probability.values())
print('Энтропия = ' + str(entropy))

max_entropy = calculate_max_entropy(32)
print('Максимальная энтропия = ' + str(max_entropy))

redundancy = calculate_redundancy(max_entropy, entropy)
print('Избыточность = ' + str(redundancy))

print('Количество символов = ' + str(len(symbols)))
print('Количество бит закодированного текста = ' + str(len(symbols) * 5))
