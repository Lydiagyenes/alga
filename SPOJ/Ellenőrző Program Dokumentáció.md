# Ellenőrző Program Dokumentáció

Ez a dokumentáció bemutatja a tesztelő programot, amelyet a `Prime Generator` algoritmus ellenőrzésére készítettünk. A program futtatja a megadott teszteseteket és ellenőrzi, hogy a kimenet megfelel-e az elvárt eredményeknek.

## Program Célja

A tesztelő program célja, hogy ellenőrizze a `Prime Generator` algoritmus helyes működését különböző bemeneti adatokat felhasználva. A tesztek során az algoritmus által generált prímszámokat hasonlítjuk össze az elvárt kimenetekkel.

## Program Működése

### 1. Tesztesetek Listája
A tesztesetek egy listában (`tests`) találhatók, mindegyik tartalmazza:
- A bemenetet (`input`)
- Az elvárt kimenetet (`expected_output`)

A program az alábbi teszteseteket futtatja:

- **Kisebb intervallumok**: Olyan tesztek, mint például 1 és 10 közötti számok, vagy 3 és 5 közötti számok.
- **Közepes intervallumok**: Intervallumok, mint 1 és 100 között, vagy 10 és 20 között.
- **Nagy intervallumok**: Tesztek a nagy számú prímek generálására, például 500,000,000 - 500,000,010, vagy 1,000,000,000 - 1,000,000,010 intervallumokban.
- **Maximális tartomány**: A teljes tartomány tesztelése, mint például 1 és 100,000 között.

### 2. Teszt Kimenet Ellenőrzése
A tesztek futtatása után a program ellenőrzi, hogy a kimenet megegyezik-e az elvárt eredménnyel:
- Ha a kimenet helyes, a program "Test Passed" üzenetet ír ki.
- Ha a kimenet nem felel meg, a program kiírja az elvárt és a tényleges kimenetet, valamint jelzi, hogy a teszt hibás.

### 3. Futás
A tesztelőt a következő parancs segítségével lehet futtatni:
```bash
python3 test_prime1.py
```

A program automatikusan végrehajtja az összes tesztet, és eredményüket a konzolon jeleníti meg.

## Tesztelő Program Kódja

A program Python-ban készült, és a `subprocess` modult használja a teszteléshez. Az alábbiakban bemutatjuk a kódot:

```python
import subprocess

def run_test(test_input, expected_output):
    # Futtatjuk a programot a teszt bemenettel
    process = subprocess.Popen(
        ["python3", "prime1.py"],  # A fájl neve, amit tesztelni szeretnénk
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Bemenet átadása a programnak
    stdout, stderr = process.communicate(input=test_input.encode())

    # Eredmény összehasonlítása
    if stdout.decode().strip() == expected_output.strip():
        print("Test Passed")
    else:
        print("Test Failed")
        print("Expected Output:")
        print(expected_output)
        print("Actual Output:")
        print(stdout.decode().strip())

# Tesztesetek listája
tests = [
    {
        "input": "1\n1 10\n", 
        "expected_output": "2\n3\n5\n7\n"
    },
    {
        "input": "1\n3 5\n", 
        "expected_output": "3\n5\n"
    },
    {
        "input": "1\n10 20\n", 
        "expected_output": "11\n13\n17\n19\n"
    },
    {
        "input": "1\n1 100\n", 
        "expected_output": "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n31\n37\n41\n43\n47\n53\n59\n61\n67\n71\n73\n79\n83\n89\n97\n"
    },
    {
        "input": "1\n100 200\n", 
        "expected_output": "101\n103\n107\n109\n113\n127\n131\n137\n139\n149\n151\n157\n163\n167\n173\n179\n181\n191\n193\n197\n199\n"
    },
    {
        "input": "1\n500000000 500000010\n", 
        "expected_output": "500000003\n500000009\n"
    },
    {
        "input": "1\n999999990 1000000000\n", 
        "expected_output": "999999991\n"
    },
    {
        "input": "1\n1000000000 1000000010\n", 
        "expected_output": "1000000003\n1000000009\n"
    },
    {
        "input": "1\n500 1000\n", 
        "expected_output": "503\n509\n521\n523\n541\n547\n557\n563\n569\n571\n577\n587\n593\n599\n607\n613\n617\n619\n631\n641\n643\n"
    },
    {
        "input": "1\n1 100000\n", 
        "expected_output": "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n31\n37\n41\n43\n47\n53\n59\n61\n67\n71\n73\n79\n83\n89\n97\n"
    }
]

# Tesztek futtatása
for test in tests:
    print(f"Running test with input: {test['input']}")
    run_test(test["input"], test["expected_output"])
    print("\n---\n")
```

## Tesztelési Eredmények

Minden teszteset után a következő üzenet fog megjelenni:

- **Test Passed**: Ha a teszt sikeres és az eredmény helyes.
- **Test Failed**: Ha a teszt nem sikerült, és a program az elvárt és tényleges kimenetet is megjeleníti.

A program kimenete a tesztek száma alapján a következő formátumban jelenik meg:

```
Running test with input: 1\n1 10\n
Test Passed

---

Running test with input: 1\n3 5\n
Test Passed

---
```

## Fontosabb Megjegyzések

1. A program automatikusan futtatja a teszteseteket, és minden tesztet külön-külön ellenőriz.
2. A `subprocess` modult használjuk a program futtatására, így a tesztelés könnyen automatizálható.
3. A tesztelés célja az algoritmus helyes működésének biztosítása különböző bemeneti tartományokban.