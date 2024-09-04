import random
import string


def generate_string(length):
    a = []
    all_symbols = string.ascii_uppercase + string.digits
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    for i in range(length):
        a.append(list(result))
    return a


print(generate_string(6))