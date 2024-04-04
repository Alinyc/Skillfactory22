sequence = list(map(float, input("Введите последовательность чисел через пробел: ").split()))
number = float(input("Введите любое число: "))

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
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

print("Отсортированный список: ", merge_sort(sequence))

def binary_search(sequence, number, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if sequence[middle] >= number and sequence[middle - 1] < number:
        return middle - 1
    elif number < sequence[middle]:
        return binary_search(sequence, number, left, middle - 1)
    else:
        return binary_search(sequence, number, middle + 1, right)

left, right = float(sequence[0]), float(sequence[-1])

if left > number > right:
    print("Число, которое Вы ввели, отсутствует в диапазоне последовательности")
else:
    print("Индекс элемента, который меньше введенного пользователем числа: ",
          binary_search(sequence, number, left, right))