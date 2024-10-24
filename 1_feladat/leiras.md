
## Feladat: Fagylalt Parlor

Két barát szeretné összedobni a pénzüket, hogy fagylaltot vegyenek. Mindig két különböző ízt választanak, és a teljes összegüket elköltik.

Adott egy lista, amely a fagylaltok árait tartalmazza. A feladat, hogy válaszd ki azt a két fagylaltot, amelyek ára összesen éppen megegyezik azzal az összeggel, amit a barátaid el szeretnének költeni.

### Példa
- **m = 6**, **árak = [1, 3, 4, 5, 6]**

A két fagylalt, amelyek ára 1 és 5, megfelelnek a kritériumoknak. Az indexük 1 és 4 (1-alapú indexelést használunk).

### Funkció leírása

Írd meg az `icecreamParlor` függvényt, amely az alábbi paraméterekkel rendelkezik:

- **int m**: az összeg, amit a barátok el szeretnének költeni.
- **int[] arr**: a fagylaltok árait tartalmazó tömb.

A függvény térjen vissza egy **egész szám tömbbel**, amely tartalmazza a két fagylalt indexét, növekvő sorrendben.

### Bemenet formátuma

Az első sor tartalmaz egy egész számot, **t**, ami azt jelzi, hány alkalommal látogatják meg a fagylaltozót. A következő **t** látogatás mindegyike a következőképpen van leírva:

- Egy egész szám, **m**, az összeg, amit a barátok el szeretnének költeni.
- Egy egész szám, **n**, a fagylaltok száma.
- Egy **n** hosszú tömb, amely a fagylaltok árait tartalmazza.

### Kimenet formátuma

A függvény térjen vissza egy egész szám tömbbel, amely tartalmazza a fagylaltok 1-alapú indexeit növekvő sorrendben, ahol az áruk éppen összesen **m**.

### Korlátozások
- \( 1 \leq t \leq 50 \)
- \( 2 \leq m \leq 10^4 \)
- \( 2 \leq n \leq 10^4 \)
- \( 1 \leq \text{arr}[i] \leq 10^4 \)
- Minden bemenetre mindig egyértelmű megoldás létezik.

### Példa bemenet

```plaintext
2
4
5
1 4 5 3 2
4
4
2 2 4 3
```

### Példa kimenet

```plaintext
1 4
1 2
```

### Magyarázat

1. Az első látogatáskor a barátok összeadott pénze **m = 4**. Az ötféle fagylalt közül a 1-es és 4-es fagylalt ára (1 és 3) éppen 4-et ad ki.
2. A második látogatáskor a barátok ismét **m = 4** pénzzel rendelkeznek, és a 1-es és 2-es fagylalt ára (2 és 2) adja ki a 4-et.

--- 

Ez a feladat arra fókuszál, hogy a két megfelelő fagylalt ízt megtaláld, amelyek árának összege pontosan megegyezik az összegükkel.
