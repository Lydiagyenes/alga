
# Mandragora Ellenőrző Program Dokumentáció

## Bevezetés

Ez a dokumentáció leírja a Mandragora ellenőrző program működését, amely a `mandragora` függvény helyességét teszteli különböző tesztesetek futtatásával. A program célja, hogy ellenőrizze a funkció teljesítményét és megbízhatóságát, különböző mandragóra egészségügyi értékek mellett.

## Funkciók

### `mandragora(H)`

Ez a függvény kiszámítja a maximális tapasztalati pontszámot, amelyet Garnet elérhet a mandragórák legyőzésével. A függvény a következő lépéseket hajtja végre:

1. A mandragórák egészségügyi értékeit csökkenő sorrendbe rendezi.
2. Inicializálja a kezdő egészségpontot (s = 1) és tapasztalati pontot (p = 0).
3. Iterál a mandragórák listáján, miközben számolja a tapasztalati pontokat és frissíti a maximális tapasztalati pontszámot.

### `run_tests()`

Ez a funkció tartalmazza a teszteseteket, amelyeket a `mandragora` függvényen hajt végre. A következő lépések szerint működik:

1. **Teszt Esetek**: A program 10 különböző teszt esetet tartalmaz, amelyek különböző mandragóra egészségügyi értékeket tartalmaznak.
2. **Eredmények Ellenőrzése**: Minden teszt esetnél ellenőrzi, hogy a `mandragora` függvény által visszaadott érték megegyezik-e a várt eredménnyel.
3. **Eredmények Kiírása**: Ha a teszt sikeres, kiírja a teszt eset számát és az eredményt; ha a teszt nem sikerül, hibaüzenetet küld.

## Tesztesetek

A program a következő teszteseteket tartalmazza:

1. **Teszt eset 1**: `H = [3, 2, 2]`, várt eredmény: `10`
2. **Teszt eset 2**: `H = [1, 2, 3]`, várt eredmény: `6`
3. **Teszt eset 3**: `H = [5, 5, 5, 5]`, várt eredmény: `60`
4. **Teszt eset 4**: `H = [1, 1, 1, 1, 1]`, várt eredmény: `15`
5. **Teszt eset 5**: `H = [10, 20, 30]`, várt eredmény: `90`
6. **Teszt eset 6**: `H = [1]*100`, várt eredmény: `5050`
7. **Teszt eset 7**: `H = [10]*100`, várt eredmény: `50500`
8. **Teszt eset 8**: `H = [7, 2, 5, 8, 1]`, várt eredmény: `54`
9. **Teszt eset 9**: `H = [9, 3, 6, 8]`, várt eredmény: `45`
10. **Teszt eset 10**: `H = [100, 200, 300, 400, 500]`, várt eredmény: `3000`

## Futtatás

1. **Python Fájl Létrehozása**: Másold a kódot egy `.py` fájlba (pl. `mandragora_test.py`).
2. **Futtatás**: A parancssorban navigálj a fájl helyére, majd futtasd a következő parancsot:

   ```bash
   python mandragora_test.py
   ```

## Következtetés

Ez az ellenőrző program biztosítja, hogy a `mandragora` függvény megfelelően működik különböző mandragóra egészségügyi értékek mellett. A tesztelési folyamat révén az esetleges hibák korai felismerése lehetővé teszi a hatékonyabb fejlesztést és a kód megbízhatóságát.
```
