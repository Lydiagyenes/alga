# Snakes and Ladders Ellenőrző Program Dokumentációja

## Áttekintés

Ez a Python program a Snakes and Ladders játék `quickestWayUp` függvényének helyes működését ellenőrzi. A program 10 tesztesetet tartalmaz, köztük néhány nagy méretűt is, hogy biztosítsa a funkcionalitás helyességét különböző helyzetekben.

## Telepítés

A program futtatásához Python 3.x verzió szükséges. 

1. Másold a kódot egy `.py` fájlba (pl. `snakes_and_ladders_test.py`).
2. Nyisd meg a terminált.
3. Navigálj ahhoz a mappához, ahol a fájl található.
4. Futtasd a következő parancsot:

   ```bash
   python snakes_and_ladders_test.py
   ```

## Program Leírása

### `quickestWayUp(ladders, snakes)`

Ez a függvény kiszámítja a minimum dobások számát, amely szükséges a 100. mező eléréséhez a megadott létrák és kígyók figyelembevételével.

**Paraméterek:**
- `ladders`: 2D tömb, ahol a létrák kezdő és végső mezőit tárolja.
- `snakes`: 2D tömb, ahol a kígyók kezdő és végső mezőit tárolja.

**Visszatérési érték:**
- Az egész szám, amely a minimum dobások számát jelzi a célmező eléréséhez. Ha nincs megoldás, a függvény -1-et ad vissza.

### Tesztesetek

A program 10 tesztesetet tartalmaz, amelyek a következő helyzeteket tesztelik:

1. **Példa tesztek:** 3 és 5 dobás elérésének tesztelése a létrák és kígyók figyelembevételével.
2. **Nincs létra és kígyó:** Ellenőrzi, hogy a program helyesen kezeli a létrák és kígyók hiányát (-1 visszatérési érték).
3. **Egyszerű létra és kígyó:** Alacsony értékek, egyszerű esetek tesztelése.
4. **Összetett elrendezések:** Különböző létra és kígyó kombinációk, hogy a program különböző helyzeteket tudjon kezelni.

## Kimenet

A program minden teszt futtatása után kiírja a következőket:
- Ha a teszt sikeres: `Test case X passed!`
- Ha a teszt nem sikeres: `Test case X failed: expected Y, got Z`

## Hibaelhárítás

- **ImportError**: Ellenőrizd, hogy a Python telepítve van a gépen.
- **AssertionError**: Ha egy teszt megbukik, ellenőrizd a várt eredmény és a kapott eredmény közötti eltéréseket.

