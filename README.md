# prakt9-11
def input_large_number_array(prompt):
    """Ввод массива чисел вручную.
    Args:
        prompt (str): Сообщение, которое будет отображаться пользователю для ввода данных.  
    Returns:
        list: Список целых чисел, введенных пользователем.
    """
    return list(map(int, input(prompt).split()))

def generate_large_number_array(size):
    """Генерация случайного массива чисел.
    Args:
        size (int): Размер генерируемого массива. 
    Returns:
        list: Список случайных целых чисел от 0 до 9 заданного размера.
    """
    import random
    return [random.randint(0, 9) for _ in range(size)]
def sum_arrays(array1, array2):
    """Суммирует два массива.
    Если массивы имеют разную длину, то более короткий массив дополняется нулями слева.
    Args:
        array1 (list): Первый массив целых чисел.
        array2 (list): Второй массив целых чисел.
        
    Returns:
        list: Новый массив, содержащий сумму элементов двух массивов поэлементно.
    """
    max_length = max(len(array1), len(array2))
    array1 = [0] * (max_length - len(array1)) + array1
    array2 = [0] * (max_length - len(array2)) + array2
    return [a + b for a, b in zip(array1, array2)]

def subtract_arrays(array1, array2):
    """Вычитает второй массив из первого.
    
    Если массивы имеют разную длину, то более короткий массив дополняется нулями слева.
    
    Args:
        array1 (list): Первый массив целых чисел.
        array2 (list): Второй массив целых чисел.
        
    Returns:
        list: Новый массив, содержащий разность элементов первого массива и второго поэлементно.
    """
    max_length = max(len(array1), len(array2))
    array1 = [0] * (max_length - len(array1)) + array1
    array2 = [0] * (max_length - len(array2)) + array2
    return [a - b for a, b in zip(array1, array2)]

def task1_menu():
    """Меню первого задания для работы с массивами.

    Позволяет пользователю выбирать между вводом массивов вручную или их генерацией,
    а также выполнять операции сложения и вычитания над ними. 
    Меню будет продолжать отображаться до тех пор, пока пользователь не выберет выход.

    Returns:
        None
    """
    while True:
        print("\nЗадание 1: Сумма и разность массивов")
        print("1) Ввод массивов вручную")
        print("2) Генерация случайных массивов")
        print("3) Выполнить операцию")
        print("4) Вернуться в главное меню")

        choice = input("Выберите опцию: ")

        if choice == '1':
            # Ввод массивов вручную
            array1 = input_large_number_array("Введите первый массив чисел: ")
            array2 = input_large_number_array("Введите второй массив чисел: ")
        elif choice == '2':
            # Генерация случайных массивов
            size = int(input("Введите размер массивов: "))
            array1 = generate_large_number_array(size)
            array2 = generate_large_number_array(size)
            print(f"Сгенерированный первый массив: {array1}")
            print(f"Сгенерированный второй массив: {array2}")
        elif choice == '3':
            # Выполнение операции над массивами
            operation = input("Введите операцию (+ или -): ")
            if operation == '+':
                result = sum_arrays(array1, array2)
                print(f"Результат суммы: {result}")
            elif operation == '-':
                result = subtract_arrays(array1, array2)
                print(f"Результат разности: {result}")
            else:
                print("Неверная операция.")
        elif choice == '4':
            # Выход из меню
            break
        else:
            print("Неверный выбор.")

import task1
import task2
import task3

def main_menu():
    """Главное меню приложения.

    Отображает главное меню, позволяющее пользователю выбирать между различными заданиями
    и завершать работу программы. Меню будет продолжать отображаться до тех пор, пока 
    пользователь не выберет опцию выхода.

    Returns:
        None
    """
    while True:
        print("\nГлавное меню:")
        print("1) Задание 1")
        print("2) Задание 2")
        print("3) Задание 3")
        print("4) Завершить работу программы")

        choice = input("Выберите опцию: ")

        if choice == '1':
            # Переход к меню первого задания
            task1.task1_menu()
        elif choice == '2':
            # Переход к меню второго задания
            task2.task2_menu()
        elif choice == '3':
            # Переход к меню третьего задания
            task3.task3_menu()
        elif choice == '4':
            # Завершение работы программы
            print("Выход из программы.")
            break
        else:
            # Обработка неверного выбора
            print("Неверный выбор.")

if __name__ == "__main__":
    main_menu()

def count_subarrays_with_sum(array, target_sum):
    """Подсчитывает количество подмассивов с заданной суммой.
    
    Эта функция перебирает все возможные подмассивы заданного массива и 
    подсчитывает, сколько из них имеют заданную сумму.

    Args:
        array (list): Список целых чисел, в котором нужно искать подмассивы.
        target_sum (int): Целевая сумма, которую должны иметь подмассивы.

    Returns:
        int: Количество подмассивов, сумма которых равна target_sum.
    """
    count = 0
    n = len(array)
    
    # Перебор всех возможных начальных индексов подмассивов
    for i in range(n):
        current_sum = 0
        # Перебор всех возможных конечных индексов подмассивов
        for j in range(i, n):
            current_sum += array[j]
            # Проверка, равна ли текущая сумма целевой сумме
            if current_sum == target_sum:
                count += 1
                
    return count

def task2_menu():
    """Меню второго задания.

    Позволяет пользователю вводить массив чисел и целевую сумму,
    а затем выводит количество подмассивов с заданной суммой. 
    Меню будет продолжать отображаться до тех пор, пока пользователь 
    не решит завершить работу.

    Returns:
        None
    """
    while True:
        print("\nЗадание 2: Подмассивы с заданной суммой")
        # Ввод массива чисел от пользователя
        array = list(map(int, input("Введите массив чисел через пробел: ").split()))
        # Ввод целевой суммы от пользователя
        target_sum = int(input("Введите целевую сумму: "))
        
        # Подсчет подмассивов с заданной суммой
        result = count_subarrays_with_sum(array, target_sum)
        print(f"Количество подмассивов с суммой {target_sum}: {result}")

        # Запрос на продолжение работы или выход из меню
        if input("Хотите продолжить? (y/n): ") != 'y':
            break

import math

def calculate_distances(points1, points2):
    """Вычисляет расстояния между двумя массивами точек.
    
    Эта функция принимает два массива точек и вычисляет расстояние 
    между соответствующими точками из каждого массива с использованием 
    формулы Евклидова расстояния.

    Args:
        points1 (list): Список кортежей, представляющих координаты точек (x, y) первого массива.
        points2 (list): Список кортежей, представляющих координаты точек (x, y) второго массива.

    Returns:
        list: Список расстояний между соответствующими точками из двух массивов.
    """
    distances = []
    
    # Вычисление расстояния между соответствующими точками
    for p1, p2 in zip(points1, points2):
        distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        distances.append(distance)
        
    return distances

def filter_distances(distances, threshold):
    """Фильтрует расстояния по заданному порогу.
    
    Эта функция возвращает новый список, содержащий только те расстояния,
    которые превышают заданный порог.

    Args:
        distances (list): Список расстояний для фильтрации.
        threshold (float): Пороговое значение для фильтрации расстояний.

    Returns:
        list: Список расстояний, превышающих заданный порог.
    """
    return [d for d in distances if d > threshold]

def task3_menu():
    """Меню третьего задания.

    Позволяет пользователю вводить координаты точек из двух массивов,
    вычислять расстояния между ними и фильтровать результаты по заданному порогу. 
    Меню будет продолжать отображаться до тех пор, пока пользователь 
    не решит завершить работу.

    Returns:
        None
    """
    while True:
        # Ввод точек первого массива
        points1 = [(int(x), int(y)) for x, y in zip(input("Введите точки первого массива (x,y): ").split(), input().split())]
        # Ввод точек второго массива
        points2 = [(int(x), int(y)) for x, y in zip(input("Введите точки второго массива (x,y): ").split(), input().split())]
        
        # Ввод порога расстояния
        threshold = float(input("Введите порог расстояния: "))
        
        # Вычисление расстояний и фильтрация
        distances = calculate_distances(points1, points2)
        filtered_distances = filter_distances(distances, threshold)
        
        # Вывод результатов
        print(f"Расстояния между точками: {distances}")
        print(f"Расстояния больше порога {threshold}: {filtered_distances}")

        # Запрос на продолжение работы или выход из меню
        if input("Хотите продолжить? (y/n): ") != 'y':
<<<<<<< HEAD
            break
=======
            break
>>>>>>> 52f9d45dd10ae6a2515525bb16ec1e0b92ada94a
