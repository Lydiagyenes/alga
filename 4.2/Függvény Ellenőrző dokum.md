### `beautifulPath` Függvény Ellenőrző Program Dokumentációja

Ez a dokumentáció a `beautifulPath` Python-függvény tesztelésére szolgáló ellenőrző program felépítését és működését írja le. A program célja, hogy biztosítsa a függvény helyes működését különböző bemeneti esetekkel, köztük kisebb és nagyobb méretű tesztesetekkel.

#### 1. Áttekintés

Az ellenőrző program egy 10 különböző bemenetet tartalmazó tesztkészlet segítségével teszteli a `beautifulPath` függvényt. Minden teszteset egy adott gráfot és két pontot ad meg, valamint az elvárt minimális büntetést a megadott két csomópont közötti lehetséges útvonalak közül.

#### 2. A Tesztek Beállítása

A tesztkészlet minden eleme a következő adatokat tartalmazza:

- **`edges`**: Egy 2D tömb, amely az élek listáját tartalmazza. Minden él három értéket tárol: az él kezdő csomópontja, a végző csomópontja, és a büntetés értéke.
- **`A`** és **`B`**: A két csomópont, amelyek között a minimális büntetésű útvonalat keressük.
- **`expected`**: Az elvárt kimeneti érték (minimális büntetés) a `beautifulPath` függvény számára, vagy -1, ha nincs útvonal a két csomópont között.

#### 3. A Teszt Program Futtatása

Az ellenőrző program iterál a teszteseteken, és mindegyikhez lefuttatja a `beautifulPath` függvényt. A futtatott függvény által visszaadott értéket összehasonlítja az elvárt értékkel.

Ha az eredmény megegyezik az elvárt értékkel, a teszt sikeres. Ellenkező esetben a teszt sikertelennek minősül, és a program megjeleníti a várt és kapott eredményeket.

#### 4. Tesztesetek Leírása

Az ellenőrző programban szereplő tesztesetek az alábbiakat foglalják magukba:

- **Egyszerű esetek**: Pl. egyetlen él, vagy egy kétélű gráf minimális büntetéssel.
- **Nagyobb gráfok**: Különböző élek és csomópontok kombinációi, ahol a minimális büntetés meghatározása már bonyolultabb.
- **Nincs útvonal esetek**: Izolált csomópontokat tartalmazó gráfok, ahol nem létezik elérési út az adott csomópontok között.
- **Nagy tesztesetek**: Magas csomópont- és élszámú gráfok, ahol az optimális útvonal megtalálása több élt érint.

#### 5. Használat

1. Futtassa a `beautifulPath` függvény kódját, és győződjön meg róla, hogy ugyanabban a könyvtárban található, mint az ellenőrző program.
2. Futtassa az ellenőrző programot: a program minden tesztet lefuttat, majd kiírja az eredményeket.
3. Sikeres teszt esetén a program jelzi, hogy az eredmény helyes. Sikertelen teszt esetén jelzi az eltérést a várt és a kapott eredmény között.

#### 6. Példa Kimenet

A sikeres futtatás eredménye:

```
Teszt 1 sikeres. (Eredmény: 3)
Teszt 2 sikeres. (Eredmény: 0)
Teszt 3 sikeres. (Eredmény: 5)
...
Teszt 10 sikeres. (Eredmény: 5)
```

Sikertelen teszteset kimenete:

```
Teszt 4 sikertelen. (Eredmény: 10, Elvárt: 3)
```

#### 7. Korlátok

- A program a `beautifulPath` függvény feltételezett működése alapján készült.
- A bemenet nagysága és komplexitása a függvény teljesítményét befolyásolhatja.

#### 8. Kód

A teljes ellenőrző program kódja itt található:

```python
import beautifulPath # A függvény, amit tesztelünk

# Tesztelési adatok
test_cases = [
    {"edges": [[1, 2, 1], [2, 3, 3], [1, 3, 5]], "A": 1, "B": 3, "expected": 3},
    # További tesztesetek itt...
]

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
```