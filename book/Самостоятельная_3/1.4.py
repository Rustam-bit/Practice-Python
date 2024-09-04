def fill_snake(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    num = 1
    top, left, bottom, right = 0, 0, rows - 1, cols - 1

    while top <= bottom and left <= right:
        # Заполняем верхнюю строку слева направо
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Заполняем правый столбец сверху вниз
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # Заполняем нижнюю строку справа налево
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        # Заполняем левый столбец снизу вверх
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix

# Пример использования
matrix = [[0]*4 for _ in range(4)]
filled_matrix = fill_snake(matrix)

for row in filled_matrix:
    print(row)