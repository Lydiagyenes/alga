# Prime1 - Prím Generátor

## Leírás

Peter prím számokat szeretne generálni a kriptoszisztémája számára. Segíts neki! A feladatod, hogy generáld le az összes prím számot két adott szám között!

## Bemenet

A bemenet egyetlen sorban a tesztesetek számát tartalmazza, `t` (t <= 10). A következő `t` sor mindegyikében két számot tartalmaz, `m` és `n` (1 <= m <= n <= 1,000,000,000, n - m <= 100,000), amelyek egy intervallumot jelölnek, amelyen belül prím számokat kell generálni.

## Kimenet

Minden tesztesetre írj ki egy új sort, amely tartalmazza az összes prím számot, amelyek `m <= p <= n` között vannak, egy számot soronként. A tesztesetek között hagyj egy üres sort.

## Példa

### Bemenet

```
2
1 10
3 5
```

### Kimenet

```
2
3
5
7

3
5
```

## Magyarázat

Az első tesztesetben a [1, 10] intervallumban található prímszámok: 2, 3, 5 és 7.

A második tesztesetben a [3, 5] intervallumban található prímszámok: 3 és 5.

## Korlátok

- 1 <= m <= n <= 1,000,000,000
- n - m <= 100,000
- 1 <= t <= 10
- m, n, és a prím számok értéke pozitívak és kisebbek, mint 10^7

## Megjegyzés

A feladat célja a prím számok gyors generálása nagy tartományokban is. A legjobb megoldás a szegmentált szita (segmented sieve) módszer alkalmazásával érhető el.