# task3.py
import math

def calculate_distances(points1, points2):
    """Вычисляет расстояния между двумя массивами точек."""
    distances = []
    
    for p1, p2 in zip(points1, points2):
        distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        distances.append(distance)
        
    return distances

def filter_distances(distances, threshold):
    """Фильтрует расстояния по заданному порогу."""
    return [d for d in distances if d > threshold]

def task3_menu():
    """Меню третьего задания."""
    while True:
        points1 = [(int(x), int(y)) for x, y in zip(input("Введите точки первого массива (x,y): ").split(), input().split())]
        points2 = [(int(x), int(y)) for x, y in zip(input("Введите точки второго массива (x,y): ").split(), input().split())]
        
        threshold = float(input("Введите порог расстояния: "))
        
        distances = calculate_distances(points1, points2)
        filtered_distances = filter_distances(distances, threshold)
        
        print(f"Расстояния между точками: {distances}")
        print(f"Расстояния больше порога {threshold}: {filtered_distances}")

        if input("Хотите продолжить? (y/n): ") != 'y':
            break