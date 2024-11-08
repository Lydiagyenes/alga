## Feladat Leírása - Minimum Penalty Path

Egy irányítatlan gráfban `N` darab csomópont és `M` darab él található. Minden élhez tartozik egy egész szám típusú költség `Ci`.

Egy útvonal büntetése a csomópontpár közötti minden él költségeinek bitenkénti **VAGY (OR)** műveletével számítandó. Tehát, ha egy útvonal élei `M1`, `M2`,..., `Mk`, akkor ennek az útnak a büntetése `C1 OR C2 OR ... OR Ck`.

A feladat célja, hogy a megadott gráfban találjuk meg két adott csomópont `A` és `B` közötti olyan útvonalat, amely minimális büntetéssel rendelkezik, és adjuk meg ennek az útnak a büntetését. Ha nincs út `A` és `B` között, akkor `-1`-et kell visszaadni.

**Megjegyzés**: Hurkok és többszörös élek megengedettek. A bitenkénti **VAGY** művelet Pascal nyelven `or`, C++ és Java nyelven `|` operátorral írható.

### Bemenet Formátuma

- Az első sor két szóközzel elválasztott egész számot tartalmaz: `N` (csomópontok száma) és `M` (élek száma).
- A következő `M` sor mindegyike három szóközzel elválasztott egész számot tartalmaz: `Ui`, `Vi` és `Ci`, amelyek az `Mi` élt leírják. Ez az él `Ui` és `Vi` csomópontokat köti össze, a büntetése pedig `Ci`.
- Az utolsó sor két szóközzel elválasztott egész számot tartalmaz: `A` (kiindulási csomópont) és `B` (cél csomópont).

### Korlátok

- 1≤N≤10^3
- 1≤𝑀≤10^4
- 1≤Ci<1024
- 1≤Ui,Vi≤N
- 1≤A,B≤N
- `A` és `B` különböző csomópontok.


### Kimenet Formátuma

- Írjuk ki a minimális büntetést az `A` és `B` közötti optimális útvonalra. Ha nincs elérhető út `A` és `B` között, akkor írjuk ki `-1`-et.

### Példa

**Bemenet:**
```
3 4
1 2 1
1 2 1000
2 3 3
1 3 100
1 3
```

**Kimenet:**
```
3
```

**Magyarázat:**

Az optimális útvonal: `1 -> 2 -> 3`.

- Az `1` és `2` csomópontok közötti él költsége `1`, míg a `2` és `3` közötti él költsége `3`.
- Az útvonal büntetése: `1 OR 3 = 3`, így `3`-at adunk vissza.

### Megjegyzés a Megoldáshoz

1. A gráfot egy szomszédsági lista segítségével reprezentáljuk, amely az élek költségeit is tartalmazza.
2. Egy Dijkstra-szerű algoritmust alkalmazunk prioritási sorral, hogy a minimális büntetést megtaláljuk a célcsomópontig.
3. A bitenkénti VAGY művelettel kiszámítjuk az aktuális út büntetését, és csak akkor folytatjuk, ha ez az új érték kisebb, mint egy korábban regisztrált útvonal büntetése ugyanannak a csomópontnak.