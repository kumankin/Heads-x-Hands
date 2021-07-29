# Тестовое задание для поступающих в школу разработки Heads x Hands
На любом языке программирования (который вам знаком или с которым у вас есть опыт работы) напишите функцию алгоритма описанного ниже.
Результаты вашей работы загрузите в репозиторий на сервисе github с открытым доступом и отправьте нам ссылку на него.
Критерием для оценки будет служить не только правильность работы кода, но и его аккуратность и оформление.

## Задача
На входе функция получает параметр n - натуральное число. Необходимо сгенерировать n-массивов, заполнить их случайными числами, каждый массив имеет случайный размер. Размеры массивов не должны совпадать. Далее необходимо отсортировать массивы. Массивы с четным порядковым номером отсортировать по возрастанию, с нечетным порядковым номером - по убыванию. На выходе функция должна вернуть массив с отсортированными массивами.

## Решение
В папке src находятся два файла:
    - main.py - запуск написанных функций
    - create_arrays.py - сам модуль содержащий написанные функции (почему их две, об это ниже).

В модуле create_arrays содержится две функции - long() и short() - являющиеся решениями задачи.
Обе функции принимают своим аргументом заведомо натуральное число. 

Функция long(n) - более читабельно написанная версия функции.
Функция short(n) - пример того, как данную задачу можно написать в одну строчку. 