def mandragora(H):
    # Az egészségértékek rendezése növekvő sorrendbe
    H.sort()

    # Az összes egészségérték kiszámítása (a maximális harci potenciál érdekében)
    total_health = sum(H)

    # s kezdőértéke 1 (kezdő egészségpont)
    s = 1
    # Kezdeti tapasztalati pontok (p) 0
    max_experience = total_health

    # Iterálás a mandragórákon, és döntés, hogy együk meg vagy harcoljunk
    for i in range(len(H)):
        # Ha eszünk, növeljük s-t és csökkentjük a lehetséges tapasztalati pontokat
        s += 1
        total_health -= H[i]
        # A lehetséges tapasztalati pontok kiszámítása az új s értékkel, és frissítjük a max_experience értékét
        max_experience = max(max_experience, s * total_health)
    
    return max_experience

# Fő függvény több teszteset feldolgozására
def process_test_cases(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        H = test_cases[i][1]
        result = mandragora(H)
        results.append(result)
    
    return results

# Bemenet olvasása és kimenet megjelenítése
if __name__ == '__main__':
    t = int(input())  # tesztesetek száma
    test_cases = []
    
    for _ in range(t):
        n = int(input())  # mandragórák száma
        H = list(map(int, input().split()))  # mandragórák egészségértékei
        test_cases.append((n, H))
    
    # Minden teszteset feldolgozása és az eredmények megkapása
    results = process_test_cases(t, test_cases)
    
    # Minden eredmény megjelenítése
    for result in results:
        print(result)
