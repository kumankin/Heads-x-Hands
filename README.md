# Тестовое задание для поступающих в школу разработки Heads x Hands
На любом языке программирования (который вам знаком или с которым у вас есть опыт работы) напишите функцию алгоритма описанного ниже.
Результаты вашей работы загрузите в репозиторий на сервисе github с открытым доступом и отправьте нам ссылку на него.
Критерием для оценки будет служить не только правильность работы кода, но и его аккуратность и оформление.

## Задача
На входе функция получает параметр n - натуральное число. Необходимо сгенерировать n-массивов, заполнить их случайными числами, каждый массив имеет случайный размер. Размеры массивов не должны совпадать. Далее необходимо отсортировать массивы. Массивы с четным порядковым номером отсортировать по возрастанию, с нечетным порядковым номером - по убыванию. На выходе функция должна вернуть массив с отсортированными массивами.

## Решение
Решение написанно на python. 

В папке src находятся два файла:
    - main.py - запуск написанных функций
    - create_arrays.py - сам модуль содержащий написанные функции (почему их две, об это ниже).

В модуле create_arrays содержится две функции - long() и short() - являющиеся решениями задачи.
Обе функции принимают своим аргументом заведомо натуральное число. 

Функция long(n) - более читабельно написанная версия функции:
```
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

>> long(3)
[[14, 15, 26, 55, 58, 92], [58], [47, 79, 88]]
```
Функция short(n) - пример того, как данную задачу можно написать в одну строчку.
```
def short(n):
    """
    This function returns an array of n arrays of arbitrary length filled with random numbers,
    the even subarrays of which are sorted in ascending order, and the odd ones in descending order.

    This is a short version of the function. It doesn't read well.

    >> short(3)
    [[14, 15, 26, 55, 58, 92], [58], [47, 79, 88]]
    """
    return [sorted([random.randint(0, 100) for i in range(int(random.sample(range(1, random.randint(n + 1, 100)), n)[i]))], reverse=bool(i % 2)) for i in range(int(n))]

>> short(3)
[[1, 1, 1, 12, 14, 14, 16, 17, 17, 21, 21, 24, 31, 33, 36, 36, 44, 47, 51, 55, 55, 57, 57, 59, 61, 62, 63, 77, 77, 81, 81, 88, 90, 91, 96], [98, 92, 91, 89, 88, 78, 77, 77, 76, 74, 67, 66, 65, 62, 60, 55, 53, 49, 48, 45, 38, 
34, 30, 24, 20, 13, 12, 9, 4, 0], [1, 3, 4, 6, 8, 8, 9, 9, 11, 13, 13, 16, 17, 18, 22, 22, 25, 28, 29, 31, 31, 33, 35, 43, 44, 44, 47, 48, 51, 52, 55, 60, 61, 62, 62, 62, 63, 63, 66, 69, 72, 72, 73, 75, 76, 77, 77, 77, 81, 84, 88, 89, 92, 93, 93, 94, 97, 98, 99], [100, 98, 96, 95, 94, 94, 91, 91, 87, 86, 82, 79, 78, 78, 77, 76, 75, 71, 70, 70, 70, 63, 62, 61, 60, 58, 57, 51, 50, 47, 47, 46, 42, 37, 36, 36, 33, 32, 32, 26, 25, 24, 22, 22, 18, 16, 
15, 15, 13, 12, 9, 9, 6, 1, 0], [7, 47, 93]]
```