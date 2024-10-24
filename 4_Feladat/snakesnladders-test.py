import os

def quickestWayUp(ladders, snakes):
    from collections import deque
    
    # Tábla inicializálása
    board = {i: i for i in range(1, 101)}
    
    # Létrák és kígyók hozzáadása a táblához
    for start, end in ladders:
        board[start] = end
    for start, end in snakes:
        board[start] = end
    
    # Szélességi keresés indítása
    queue = deque([(1, 0)])  # (aktuális négyzet, dobások száma)
    visited = set()  # Meglátogatott négyzetek nyilvántartása
    
    while queue:
        position, rolls = queue.popleft()
        
        # Ha elérjük a 100. négyzetet
        if position == 100:
            return rolls
        
        # Minden lehetséges dobás vizsgálata
        for die in range(1, 7):
            next_position = position + die
            
            if next_position <= 100:
                next_position = board[next_position]  # Lépés a létra vagy kígyó hatására
                
                if next_position not in visited:
                    visited.add(next_position)
                    queue.append((next_position, rolls + 1))
    
    return -1  # Ha nincs megoldás

def test_quickestWayUp():
    test_cases = [
        # (ladders, snakes, expected result)
        ([(32, 62), (42, 68), (12, 98)], [(95, 13), (97, 25), (93, 37), (79, 27), (75, 19), (49, 47), (67, 17)], 3),
        ([(8, 52), (6, 80), (26, 42), (2, 72)], [(51, 19), (39, 11), (37, 29), (81, 3), (59, 5), (79, 23), (53, 7), (43, 33), (77, 21)], 5),
        ([], [], -1),  # No ladders or snakes
        ([(2, 50)], [(3, 1)], 1),  # Simple ladder and snake
        ([(10, 30)], [(11, 2)], 1),  # Simple ladder and snake
        ([(1, 100)], [], 1),  # Direct ladder to end
        ([(20, 80), (30, 90)], [(50, 10), (70, 20)], 4),  # Multiple ladders and snakes
        ([(40, 60), (50, 70)], [(30, 20), (90, 1)], 3),  # More complex layout
        ([(1, 99)], [(2, 1), (3, 2), (4, 3), (5, 4)], -1),  # A direct ladder and multiple snakes
        ([(1, 10), (10, 20), (20, 30), (30, 40), (40, 50)], [(50, 1)], 6),  # Long chain of ladders and one snake
        ([(5, 10), (6, 11), (7, 12), (8, 13), (9, 14)], [(15, 5)], 5)  # More ladders than snakes
    ]

    for i, (ladders, snakes, expected) in enumerate(test_cases):
        result = quickestWayUp(ladders, snakes)
        assert result == expected, f'Test case {i + 1} failed: expected {expected}, got {result}'
        print(f'Test case {i + 1} passed!')

if __name__ == '__main__':
    test_quickestWayUp()
