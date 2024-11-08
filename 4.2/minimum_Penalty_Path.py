#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from collections import defaultdict, deque

#
# Complete the 'beautifulPath' function below.
#
# A függvény egy egész számot ad vissza.
# A függvény paraméterei:
#  1. 2D_INTEGER_ARRAY edges
#  2. INTEGER A
#  3. INTEGER B
#

def beautifulPath(edges, A, B):
    # A gráf inicializálása szomszédsági listaként, élekhez tartozó költségekkel
    graph = defaultdict(list)
    for u, v, cost in edges:
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    # Szótár a minimális büntetés nyilvántartására (csomópont, büntetés) állapothoz
    visited = defaultdict(lambda: float('inf'))
    visited[(A, 0)] = 0

    # Prioritási sor Dijkstra-szerű megközelítéshez, (jelenlegi_büntetés, jelenlegi_csomópont)
    pq = [(0, A)]  # Kezdés az A csomópontból 0 büntetéssel

    while pq:
        current_penalty, node = heapq.heappop(pq)

        # Ha elérjük a B csomópontot, visszatérünk a büntetéssel
        if node == B:
            return current_penalty

        # Minden szomszédot megvizsgálunk
        for neighbor, cost in graph[node]:
            new_penalty = current_penalty | cost  # Új büntetés számítása bitenkénti VAGY használatával

            # Csak akkor adjuk hozzá a sorhoz, ha az új büntetés kisebb, mint egy korábban rögzített ezen az útvonalon
            if new_penalty < visited[(neighbor, new_penalty)]:
                visited[(neighbor, new_penalty)] = new_penalty
                heapq.heappush(pq, (new_penalty, neighbor))

    # Ha nincs út A-ból B-be, visszatérünk -1-gyel
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    second_multiple_input = input().rstrip().split()

    A = int(second_multiple_input[0])
    B = int(second_multiple_input[1])

    result = beautifulPath(edges, A, B)

    fptr.write(str(result) + '\n')
    fptr.close()
