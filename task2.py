# task2.py
def count_subarrays_with_sum(array, target_sum):
    """Подсчитывает количество подмассивов с заданной суммой."""
    count = 0
    n = len(array)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += array[j]
            if current_sum == target_sum:
                count += 1
                
    return count

def task2_menu():
    """Меню второго задания."""
    while True:
        print("\nЗадание 2: Подмассивы с заданной суммой")
        array = list(map(int, input("Введите массив чисел через пробел: ").split()))
        target_sum = int(input("Введите целевую сумму: "))
        
        result = count_subarrays_with_sum(array, target_sum)
        print(f"Количество подмассивов с суммой {target_sum}: {result}")

        if input("Хотите продолжить? (y/n): ") != 'y':
            break