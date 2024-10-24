import math
import os
import random
import re
import sys
from collections import deque  

# A függvény egy INTEGER-t vár vissza.
# A következő paramétereket fogadja el a függvény:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes

def quickestWayUp(ladders, snakes):
    # Hozd létre a táblát a létrák és a kígyók alapján
    board = list(range(101))  # Tábla 0-tól 100-ig
    
    for start, end in ladders:
        board[start] = end  # Állítsd be a létra kezdőpontját a végpontjára
    for start, end in snakes:
        board[start] = end  # Állítsd be a kígyó kezdőpontját a végpontjára
    
    # BFS inicializálás
    queue = deque([1])  # Kezdj az 1. négyzetből
    visited = [False] * 101  # Nyomon követi a látogatott négyzeteket
    visited[1] = True
    rolls = 0  # A megtett dobások száma
    
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            
            # Ellenőrizd, hogy elérted-e a cél négyzetet
            if current == 100:
                return rolls
            
            # Fedezd fel a lehetséges lépéseket (1-től 6-ig)
            for dice_roll in range(1, 7):
                next_square = current + dice_roll
                
                if next_square <= 100:
                    next_square = board[next_square]  # Használj létrát vagy kígyót
                    if not visited[next_square]:
                        visited[next_square] = True
                        queue.append(next_square)

        rolls += 1  # Növeld a dobások számát a jelenlegi mélység minden csomópontjának felfedezése után

    return -1  # Ha nem tudtál eljutni a 100. négyzethez

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
