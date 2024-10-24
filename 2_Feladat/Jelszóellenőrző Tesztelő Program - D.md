### Jelszóellenőrző Tesztelő Program - Dokumentáció

Ez a dokumentáció bemutatja, hogyan használható a jelszóellenőrző algoritmushoz készített Python tesztelő környezet. A tesztelő program automatikusan lefuttatja a megadott teszteseteket, majd összehasonlítja az eredményeket a várt kimenetekkel.

#### 1. Mappastruktúra

A tesztelési környezet három mappát használ a fájlok tárolására:

- **`test_inputs/`**: Itt helyezkednek el a tesztesetek bemeneti fájljai. Minden teszteset külön fájlban található (pl. `test1.txt`, `test2.txt`).
  
- **`test_outputs/`**: Ebbe a mappába kerülnek a futtatás során generált kimeneti fájlok. Az egyes tesztesetek eredményei itt tárolódnak (pl. `output1.txt`, `output2.txt`).

- **`expected_outputs/`**: Ebben a mappában tároljuk az elvárt kimeneti fájlokat, amelyekkel az eredményeket összehasonlítjuk (pl. `expected1.txt`, `expected2.txt`).

#### 2. Tesztfájlok

- **Bemeneti fájlok formátuma (`test_inputs`)**:
  - Minden fájl egy tesztesetet képvisel.
  - A fájl első sora tartalmazza a tesztesetek számát.
  - A következő sorok a felhasználók jelszavait és a hozzájuk tartozó ellenőrizendő próbálkozásokat tartalmazzák.

  Példa egy tesztinput fájlra:
  ```
  1
  2
  ab cd
  abcd
  ```

- **Elvárt kimeneti fájlok (`expected_outputs`)**:
  - Ezek a fájlok tartalmazzák a várt kimeneteket, amelyeket az algoritmusnak elő kell állítania.

  Példa egy elvárt kimeneti fájlra:
  ```
  ab cd
  ```

#### 3. Ellenőrző Python szkript

Az alábbi Python szkript felelős a tesztek futtatásáért és az eredmények ellenőrzéséért.

```python
import os
import subprocess

# A tesztfájlok mappáinak megadása
INPUT_DIR = "test_inputs"
OUTPUT_DIR = "test_outputs"
EXPECTED_DIR = "expected_outputs"
SCRIPT = "password_cracker.py"  # A jelszóellenőrző program neve

# Ellenőrzi a teszteseteket
def run_tests(num_tests):
    for i in range(1, num_tests + 1):
        input_file = f"{INPUT_DIR}/test{i}.txt"
        output_file = f"{OUTPUT_DIR}/output{i}.txt"
        expected_file = f"{EXPECTED_DIR}/expected{i}.txt"
        
        print(f"Teszteset {i} futtatása...")

        # Futtatja a Python szkriptet a bemeneti fájllal és menti az eredményt
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            subprocess.run(["python3", SCRIPT], stdin=infile, stdout=outfile)
        
        # Az eredmények ellenőrzése
        with open(output_file, 'r') as outfile, open(expected_file, 'r') as expfile:
            output = outfile.read().strip()
            expected = expfile.read().strip()

            if output == expected:
                print(f"Teszteset {i} sikeres!")
            else:
                print(f"Teszteset {i} sikertelen!")
                print(f"Kapott eredmény:\n{output}")
                print(f"Várt eredmény:\n{expected}")

# A fő függvény
if __name__ == "__main__":
    NUM_TESTS = 10  # A tesztesetek száma
    run_tests(NUM_TESTS)
```

#### 4. Tesztelés lépései

##### 1. A környezet előkészítése

- Készítsd el a következő mappákat:
  - `test_inputs/`
  - `test_outputs/`
  - `expected_outputs/`
  
- Helyezd el a tesztinputokat a `test_inputs` mappába és az elvárt kimeneteket a `expected_outputs` mappába.

##### 2. Tesztfájlok elnevezése

- A bemeneti fájlokat `test1.txt`, `test2.txt`, stb. néven kell elhelyezni a **`test_inputs/`** mappába.
- Az elvárt kimeneteket `expected1.txt`, `expected2.txt`, stb. néven kell elhelyezni a **`expected_outputs/`** mappába.

##### 3. Futtatás

1. Futtasd a tesztelő programot:
   ```bash
   python3 test_runner.py
   ```

2. A program lefuttatja a megadott számú tesztesetet és kiírja az eredményeket.

#### 5. Példa

Példa egy futtatás eredményére:

```
Teszteset 1 futtatása...
Teszteset 1 sikeres!
Teszteset 2 futtatása...
Teszteset 2 sikertelen!
Kapott eredmény:
ab cd
Várt eredmény:
ab cd
...
```

Ez a dokumentáció segít a jelszóellenőrző algoritmus alapos tesztelésében, és biztosítja, hogy a program helyesen működjön különböző tesztesetek esetén.