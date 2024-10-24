def mandragora(H):
    H.sort(reverse=True)  # Csökkenő sorrendbe rendezés
    max_exp = 0
    s = 1  # Kezdő egészségpont
    p = 0  # Kezdő tapasztalati pont
    n = len(H)

    for i in range(n):
        # Tapasztalati pontok számítása a legyőzött mandragórák alapján
        p += s * H[i]
        max_exp = max(max_exp, p)  # Maximális tapasztalat frissítése
        s += 1  # Növeljük az egészségpontot

    return max_exp  # Maximális tapasztalati pontok visszaadása

# Tesztelő program
#   Teszt eset 1: H = [3, 2, 2], várt eredmény: 10
#   Teszt eset 2: H = [1, 2, 3], várt eredmény: 6
#   Teszt eset 3: H = [5, 5, 5, 5], várt eredmény: 60
#   Teszt eset 4: H = [1, 1, 1, 1, 1], várt eredmény: 15
#   Teszt eset 5: H = [10, 20, 30], várt eredmény: 90
#   Teszt eset 6: H = [1]*100, várt eredmény: 5050
#   Teszt eset 7: H = [10]*100, várt eredmény: 50500
#   Teszt eset 8: H = [7, 2, 5, 8, 1], várt eredmény: 54
#   Teszt eset 9: H = [9, 3, 6, 8], várt eredmény: 45
#   Teszt eset 10: H = [100, 200, 300, 400, 500], várt eredmény: 3000
def run_tests():
    test_cases = [
        ([3, 2, 2], 10),  # Példa eset
        ([1, 2, 3], 6),   # Egyszerű eset
        ([5, 5, 5, 5], 60),  # Minden mandragóra azonos erősségű
        ([1, 1, 1, 1, 1], 15),  # Alacsony értékek
        ([10, 20, 30], 90),  # Magasabb értékek
        ([1]*100, 5050),  # Nagy számú alacsony érték
        ([10]*100, 50500),  # Nagy számú magas érték
        ([7, 2, 5, 8, 1], 54),  # Vegyes értékek
        ([9, 3, 6, 8], 45),  # Vegyes, több közepes
        ([100, 200, 300, 400, 500], 3000),  # Nagy értékek
    ]

    for i, (H, expected) in enumerate(test_cases):
        result = mandragora(H)
        assert result == expected, f'Test case {i + 1} failed: expected {expected}, got {result}'
        print(f'Test case {i + 1} passed: {result}')

if __name__ == "__main__":
    run_tests()
