# Snakes and Ladders - Gyorsabb Út a Győzelemhez

Markov előveszi a Snakes and Ladders (Kígyók és Létrák) játékát, ránéz a táblára, és elgondolkodik: „Ha mindig a kívánt számot dobnám, hány dobásra lenne szükségem, hogy elérjem a célt?”

## Szabályok

- A játékot egy 6 oldalú dobókockával játsszák, amelynek oldalai 1-től 6-ig számozva vannak.
- A játékos az 1. négyzetből indul, és a 100. négyzetbe kell eljutnia a pontos dobásával.
- Ha a dobott szám a 100. négyzeten túlra vinné a játékost, akkor nem lép.
- Ha a játékos egy létra alján áll, fel kell másznia a létrán. A létrák csak felfelé vezetnek.
- Ha a játékos egy kígyó szájánál áll, le kell csúsznia a kígyón, és a farkánál fog kijönni. A kígyók csak lefelé vezetnek.

## Funkció Leírása

Fejezd be a `quickestWayUp` függvényt az alábbiak szerint. A függvény egy egész számot ad vissza, amely a szükséges dobások minimális számát jelzi.

### `quickestWayUp` Paraméterei:

- **ladders**: egy 2D egész számokból álló tömb, ahol minden `ladders[i]` tartalmazza a létra kezdő és végpontját.
- **snakes**: egy 2D egész számokból álló tömb, ahol minden `snakes[i]` tartalmazza a kígyó kezdő és végpontját.

## Bemeneti Formátum

Az első sor tartalmazza a tesztek számát, `t`.

Minden teszthez:
- Az első sor tartalmaz egy egész számot, `n`, a létrák számát.
- Az ezt követő `n` sor mindegyike két szóközön elválasztott egész számot tartalmaz, amelyek a létra kezdő és végpontját jelölik.
- A következő sor tartalmaz egy egész számot, `m`, a kígyók számát.
- Az ezt követő `m` sor mindegyike két szóközön elválasztott egész számot tartalmaz, amelyek a kígyó kezdő és végpontját jelölik.

## Korlátok

- \(1 \leq t \leq 10\)
- \(1 \leq n, m \leq 15\)

A tábla mindig 10 x 10-es, a négyzetek számozása 1-től 100-ig terjed.
Sem az 1. négyzet, sem a 100. négyzet nem lesz létra vagy kígyó kezdőpontja.
Egy négyzet legfeljebb egy végpontot tartalmazhat a kígyóktól vagy létráktól.

## Kimeneti Formátum

Minden `t` tesztesetre írd ki egy új sorba a legkevesebb dobások számát, amely szükséges a célhoz való eljutáshoz. Ha nincs megoldás, írd ki a -1-et.

## Példa Bemenet

```
2
3
32 62
42 68
12 98
7
95 13
97 25
93 37
79 27
75 19
49 47
67 17
4
8 52
6 80
26 42
2 72
9
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21 
```

## Példa Kimenet

```
3
5
```

### Magyarázat

Az első tesztnél:

- A játékos 5-öt dob, és a 12. négyzethez érkezik. Itt egy létra vezet a 98. négyzethez. 
- Ezt követően 2-t dob, ami lehetővé teszi, hogy a játékos a célhoz érkezzen a 3 dobással.

A második tesztnél:

- A játékos először 5-öt dob, és felmászik a létrára a 80. négyzethez.
- Három 6-os dobás szükséges, hogy a 98. négyzethez érkezzen. 
- Végül 2-t dob, amellyel eléri a cél négyzetet, összesen 5 dobással.

