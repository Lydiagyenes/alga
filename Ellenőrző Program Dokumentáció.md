# Ellenőrző Program Dokumentáció

## Bevezetés
Ez a dokumentáció bemutatja az ice cream parlor problémához készült ellenőrző programot, amely ellenőrzi, hogy a megoldás helyesen működik-e a különböző bemenetek esetén. A program a Python nyelven készült, és több tesztesetet tartalmaz, beleértve kisebb és nagyobb méretű bemeneteket is.

## Program Leírása
A program célja, hogy megtalálja a két különböző ízt, amelyek árának összege pontosan megegyezik a barátok által összegyűjtött pénzösszeggel.

### Fő Funkció
- **icecreamParlor(m, arr)**: A függvény bemeneti paraméterei a `m` (a barátok összegyűjtött pénze) és az `arr` (az ízek ára). A függvény visszaadja a két íz indexét, amelyek ára összeadva egyenlő `m`-mel.

### Bemeneti Formátum
- Az első sor tartalmazza a tesztek számát.
- A következő sorokban a következő információk találhatók:
  - Az összeg (m).
  - Az ízek száma (n).
  - Az ízek ára, amely egy listában szerepel.

## Ellenőrző Program Környezete

### Telepítési Útmutató
1. **Python telepítése**: Győződj meg róla, hogy a Python 3.x verzió telepítve van a gépeden.
2. **Függőségek**: Nincsenek külső függőségek, csak a Python beépített könyvtárai szükségesek.

### Futtatás
- A program futtatásához mentsd el a kódot egy `.py` fájlba, pl. `icecream_parlor.py`.
- Használj terminált vagy parancssort, és futtasd a következő parancsot:
```bash
python icecream_parlor.py < input.txt > output.txt
```
- Az `input.txt` fájl tartalmazza a bemenetet, az `output.txt` fájl pedig a program kimenetét.

### Tesztesetek
A programhoz készült tesztesetek a következők:

1. **Teszt 1:**
    ```
    1
    15
    15
    12 15 13 14 7 10 9 8 11 6 5 4 3 2 1
    ```
   - **Várt Kimenet:**
    ```
    1 12
    ```

2. **Teszt 2:**
    ```
    2
    20
    10
    2 3 5 7 11 13 17 19 4 6 8 9 12 14 16 18 15 20 1 10
    ```
   - **Várt Kimenet:**
    ```
    5 11
    ```

## Tesztelés
A tesztek a kimenet helyességét ellenőrzik a bemenetek alapján. A várt kimenetet összehasonlítjuk a tényleges kimenettel.

### Tesztelési Folyamat
1. Futtasd a programot a tesztadatokkal.
2. Ellenőrizd a `output.txt` fájl tartalmát.
3. Hasonlítsd össze a várt kimenettel.

## Összegzés
Ez a dokumentáció bemutatja az ice cream parlor problémához készült ellenőrző programot, amely képes validálni a megoldások helyességét. A program több tesztesetet használ, beleértve a közepes és nagyobb méretű bemeneteket is.
