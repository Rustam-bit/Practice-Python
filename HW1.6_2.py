def main():
    # Чтение количества записей
    num_records = int(input())

    max_values = []

    # Чтение каждой записи
    for _ in range(num_records):
        # Получение текущей записи и преобразование в список чисел
        record = list(map(int, input().split()))
        # Нахождение максимального значения в записи
        max_value = max(record)
        # Добавление максимального значения в список
        max_values.append(max_value)

    # Сортировка значений по убыванию
    max_values.sort(reverse=True)

    # Вывод значений, разделенных ";"
    print(";".join(map(str, max_values)))

if __name__ == "__main__":
    main()
