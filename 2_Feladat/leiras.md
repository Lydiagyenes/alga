### Feladat leírása

Egy CuteKittens.com nevű weboldalon regisztrált **n** felhasználó mindegyikének egyedi jelszava van, amelyeket a `pass[1]`, `pass[2]`, ..., `pass[n]` tömb reprezentál. Ez egy nagyon aranyos weboldal, amelyhez sok ember szeretne hozzáférni, hogy megnézhesse a cuki kiscicás képeket. Az oldal adminisztrátora azonban nem szeretné, ha az oldal nyilvánosan elérhető lenne, így csak azok a felhasználók férhetnek hozzá, akik rendelkeznek a megfelelő jelszóval.

Egy ügyes hacker, Yu, felfedez egy hibát a jelszóellenőrző rendszerben: a rendszer elfogad bármilyen olyan karakterláncot is, amely egy vagy több jelszó összefűzéséből áll, tetszőleges sorrendben. Bármelyik jelszó többször is szerepelhet az adott karakterláncban. A feladat az, hogy adjuk meg a felhasználók jelszavait és egy bejelentkezési próbálkozást. Döntsük el, hogy a megadott karakterlánc elfogadható-e a jelszóellenőrző rendszer által.

Ha a bejelentkezési karakterlánc előállítható a jelszavakból, adjuk meg a jelszavakat a megfelelő sorrendben, szóközzel elválasztva. Ha nem állítható elő, akkor a visszatérési érték legyen **"WRONG PASSWORD"**.

### Feladat leírása funkcionálisan

**Paraméterek:**
- `passwordCracker(passwords, loginAttempt)`
  - **passwords** (*list of strings*): A felhasználók jelszavai.
  - **loginAttempt** (*string*): A bejelentkezési próbálkozás karakterlánca.

**Visszatérési érték:**
- Ha a `loginAttempt` karakterlánc előállítható a jelszavak összefűzésével, adjuk vissza a jelszavakat megfelelő sorrendben, szóközzel elválasztva. Ha nem lehetséges, térjünk vissza a **"WRONG PASSWORD"** üzenettel.

### Input formátuma

Az első sorban egy egész szám, **t**, a tesztesetek száma.

A következő **t** teszteset mindegyike a következőképpen van megadva:
- Az első sor tartalmazza az egész számot, **n**, amely a jelszavak számát jelzi.
- A második sor tartalmaz **n** darab szóközzel elválasztott jelszót.
- A harmadik sor a **loginAttempt** karakterláncot tartalmazza, amelyet tesztelni kell.

### Korlátok

- \( 1 \leq t \leq 10 \)
- \( 1 \leq n \leq 10 \)
- \( passwords[i] \neq passwords[j] \), ahol \( i \neq j \)
- \( 1 \leq |passwords[i]| \leq 10 \), ahol \( i \in [1, n] \)
- \( 1 < |loginAttempt| \leq 2000 \)
- A **loginAttempt** és a **passwords[i]** csak kisbetűs latin betűket tartalmaznak ('a'-'z').

### Példa

**Bemenet:**
```
3
6
because can do must we what
wedowhatwemustbecausewecan
2
hello planet
helloworld
3
ab abcd cd
abcd
```

**Kimenet:**
```
we do what we must because we can
WRONG PASSWORD
ab cd
```

### Magyarázat

1. Az első tesztesetben a `wedowhatwemustbecausewecan` karakterlánc előállítható a következő jelszavakból: `we`, `do`, `what`, `we`, `must`, `because`, `we`, `can`. Ezért a visszatérési érték: **"we do what we must because we can"**.
2. A második tesztesetben a `helloworld` nem állítható elő a `hello` és `planet` jelszavakból. Ezért a visszatérési érték: **"WRONG PASSWORD"**.
3. A harmadik tesztesetben az `abcd` kétféleképpen állítható elő: `ab` és `cd`, vagy közvetlenül `abcd`. Ezért a visszatérési érték: **"ab cd"**.

---
