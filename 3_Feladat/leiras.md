# Mandragora Kalandja

## Feladat Leírása

A gonosz erdőt dühös mandragórák őrzik. Garnet és kedvenc állata egy úton indulnak át rajta. Garnet 1 egészségponttal (s) és 0 tapasztalati ponttal (p) kezd. 

Minden egyes mandragóra találkozásakor Garnet választási lehetőségei a következők:

1. Garnet kedvence megeszi az i. mandragórát. Ekkor s értéke 1-gyel növekszik, és legyőzi az i. mandragórát.
2. Garnet kedvence megküzd az i. mandragórával. Ekkor p értéke s * H[i] tapasztalati ponttal növekszik, és legyőzi az i. mandragórát.

Miután legyőz egy mandragórát, az már nem játszható. Adott egy lista a mandragórák különböző egészségértékeivel, határozzuk meg, hogy a lehető legtöbb tapasztalati pontot tudja-e Garnet összegyűjteni az útja során.

### Példa

Például, a mandragórák egészségértékei: H = [3, 2, 5]. Minden mandragórával kapcsolatos választási lehetőségek:

| Akció       | s   | p  |
|-------------|-----|----|
| e, e, e     | 4   | 0  |
| e, e, b     | 3   | 15 |
| e, b, b     | 2   | 14 |
| b, b, b     | 1   | 10 |
| b, b, e     | 2   | 10 |
| b, e, e     | 3   | 9  |
| b, e, b     | 2   | 16 |
| e, b, e     | 3   | 6  |

A legjobb lehetőség, ha megeszi a 3 pontot érő mandragórát, majd a másik kettővel megküzd, így 2 * (3 + 5) = 16 tapasztalati pontot ér el.

## Függvény Leírása

A `mandragora` függvénynek a következő paraméterekkel kell rendelkeznie:

- `H`: egy egész számokból álló tömb, amely a mandragórák egészségértékeit reprezentálja.

### Visszatérési Érték

- A függvény egy egész számot ad vissza, amely a maximális tapasztalati pontokat jelöli, amelyet Garnet összegyűjthet.

## Bemenet Formátum

1. Az első sorban egy egész szám t, a tesztesetek számát jelöli.
2. Minden teszteset két sorból áll:
   - Az első sorban egy egész szám n, a mandragórák számát jelöli.
   - A második sorban n darab szóközökkel elválasztott egész szám, amelyek a mandragórák egészségértékei H[H[1], H[2], ..., H[n]].

## Korlátozások

- \(1 \leq t \leq 10^5\)
- \(1 \leq n \leq 10^5\)
- \(1 \leq H[i] \leq 10^7\), ahol \(1 \leq i \leq n\)
- A tesztesetben szereplő összes s összege legfeljebb \(10^6\)

## Kimenet Formátum

Minden tesztesethez egy sorban egy egész számot kell kiírni, amely a maximális tapasztalati pontok számát jelöli, amelyet Garnet összegyűjthet.

## Példa Bemenet

```
1
3
3 2 2
```

## Példa Kimenet

```
10
```

### Magyarázat

A 3 mandragóra egészségértékei: H = [3, 2, 2]. Kezdetben s = 1 és p = 0. Az optimális akciósorozat a következő:

1. Együk meg a második mandragórát (H[2] = 2). Ekkor s = 2, p = 0.
2. Harcoljunk az első mandragórával (H[1] = 3). Ekkor s = 2, p = p + s * H[1] = 2 * 3 = 6.
3. Harcoljunk a harmadik mandragórával (H[3] = 2). Ekkor s = 2, p = p + s * H[3] = 2 * 2 = 4.

Összesen: p = 6 + 4 = 10 tapasztalati pontot kapunk.