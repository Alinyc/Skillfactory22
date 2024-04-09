sequence = list(map(float, input("Введите последовательность чисел через пробел: ").split()))
number = float(input("Введите любое число: "))

def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence[:]
    else:
        middle = len(sequence) // 2
        left = merge_sort(sequence[:middle])
        right = merge_sort(sequence[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

sequence = merge_sort(sequence)
print("Отсортированный список: ", sequence)


def binary_search(sequence, number, left, right):
    if left > right:
        return("Указанного числа нет в последовательности.")
    middle = (left + right) // 2
    if sequence[middle] == number:
        return ("Номер позиции элемента, меньше введённого числа, причём следующий элемент больше введённого числа или равен ему: ", middle - 1)
    elif number < sequence[middle]:
        return binary_search(sequence, number, left, middle - 1)
    else:
        return binary_search(sequence, number, middle + 1, right)

print(binary_search(sequence, number, 0, len(sequence) - 1))