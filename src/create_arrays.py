import random

def long(n):
    """
    This function returns an array of n arrays of arbitrary length filled with random numbers,
    the even subarrays of which are sorted in ascending order, and the odd ones in descending order.

    This is a long version of the function. it reads well.

    >> long(3)
    [[14, 15, 26, 55, 58, 92], [58], [47, 79, 88]]
    """
    # Создаём список в котором будем хранить длины массивов
    # (при этом должны учесть, что длина массивов должна быть различной от 1 до 100)
    arrays_len = random.sample(range(1, random.randint(n + 1, 101)), n)
    arrays = []
    # Заполняем массив массивами случайных чисел сразу сортируя их, чётные массивы по возрастанию, нечётные по убыванию
    for i in range(len(arrays_len)):
        arrays.append(sorted([random.randint(0, 100) for j in range(int(arrays_len[i]))], reverse=bool(i % 2)))
    return arrays

def short(n):
    """
    This function returns an array of n arrays of arbitrary length filled with random numbers,
    the even subarrays of which are sorted in ascending order, and the odd ones in descending order.

    This is a short version of the function. It doesn't read well.

    >> short(3)
    [[14, 15, 26, 55, 58, 92], [58], [47, 79, 88]]
    """
    return [sorted([random.randint(0, 100) for i in range(int(random.sample(range(1, random.randint(n + 1, 100)), n)[i]))], reverse=bool(i % 2)) for i in range(int(n))]