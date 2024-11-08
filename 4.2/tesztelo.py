import beautifulPath # A függvény, amit tesztelünk

# Tesztelési adatok: minden teszt eset bemenetével és elvárt kimenetével
test_cases = [
    # 1. Egyszerű teszt eset
    {
        "edges": [[1, 2, 1], [2, 3, 3], [1, 3, 5]],
        "A": 1,
        "B": 3,
        "expected": 3
    },
    # 2. Más útvonal büntetés nélkül
    {
        "edges": [[1, 2, 0], [2, 3, 0], [1, 3, 1]],
        "A": 1,
        "B": 3,
        "expected": 0
    },
    # 3. Egyetlen él
    {
        "edges": [[1, 2, 5]],
        "A": 1,
        "B": 2,
        "expected": 5
    },
    # 4. Több él, minimális büntetés kiválasztása
    {
        "edges": [[1, 2, 10], [2, 3, 5], [1, 3, 15]],
        "A": 1,
        "B": 3,
        "expected": 10
    },
    # 5. Nincs útvonal
    {
        "edges": [[1, 2, 2], [3, 4, 1]],
        "A": 1,
        "B": 4,
        "expected": -1
    },
    # 6. Nagy teszt eset - 10 csomópont, lineáris útvonal
    {
        "edges": [[i, i+1, i] for i in range(1, 10)],
        "A": 1,
        "B": 10,
        "expected": 9  # Várhatóan minden él költsége maximum
    },
    # 7. Nagy teszt eset - 10 csomópont, összefüggő
    {
        "edges": [[i, j, i+j] for i in range(1, 10) for j in range(i+1, 11)],
        "A": 1,
        "B": 10,
        "expected": 15
    },
    # 8. Nagy büntetések, minimális kiválasztásával
    {
        "edges": [[1, 2, 100], [2, 3, 50], [1, 3, 25]],
        "A": 1,
        "B": 3,
        "expected": 25
    },
    # 9. Nincs út a célhoz (izolált csomópont)
    {
        "edges": [[1, 2, 2], [2, 3, 3]],
        "A": 1,
        "B": 4,
        "expected": -1
    },
    # 10. Nagy teszt eset - körkörös elrendezés
    {
        "edges": [[i, (i % 10) + 1, i] for i in range(1, 11)],
        "A": 1,
        "B": 5,
        "expected": 5
    }
]

# Futtatja az összes teszt esetet, és kiírja az eredményt
def run_tests():
    for i, case in enumerate(test_cases):
        edges = case["edges"]
        A = case["A"]
        B = case["B"]
        expected = case["expected"]
        
        result = beautifulPath(edges, A, B)
        
        if result == expected:
            print(f"Teszt {i+1} sikeres. (Eredmény: {result})")
        else:
            print(f"Teszt {i+1} sikertelen. (Eredmény: {result}, Elvárt: {expected})")

if __name__ == "__main__":
    run_tests()
