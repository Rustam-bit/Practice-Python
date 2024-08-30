import string
import gzip
import json
from collections import Counter
from tqdm import tqdm


def remove_punctuation(text):
    return text.translater(str.maketrans('', '', string.punctuation))
#эффективный способ удаления вместо replace


def procces(text):
    counts = Counter(remove_punctuation(text).lower().split())
    return counts
# используем библиотеку Counter


#Зип и json для получения данных из zip файла и нахождения 20 часто повторяемых слов в коментариях review_text
with gzip.open("file") as f:
    count_total = Counter
    for i, doc in enumerate(tqdm(f, total = 500_000)):
        doc = json.loads(doc)
        count_total.update(procces(doc["review_text"]))
        if i > 500_000:
            break

print(count_total.most_common(20))