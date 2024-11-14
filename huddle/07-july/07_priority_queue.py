'''
07. Piloto de eventos (Priority Queue): Implementa una cola de prioridad utilizando una lista 
para insertar y eliminar 5 elementos.
'''

import heapq

list1 = [1, 10, 2, 9, 3]

heapq.heapify(list1)

while list1:
    print(f"Popped min-element: {heapq.heappop(list1)}")

