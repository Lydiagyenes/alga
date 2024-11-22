import math

# Funkció a szokásos Eratosthenes-szita alkalmazására, hogy meghatározza az összes prímszámot 1-től sqrt(n)-ig
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

# Funkció, amely az adott [m, n] tartományban meghatározza a prímszámokat a szegmentált szita segítségével
def segmented_sieve(m, n, primes):
    # Boolean tömb létrehozása a [m, n] tartomány számára
    range_sieve = [True] * (n - m + 1)
    
    # Külön kezeljük a m = 1 esetet, mivel 1 nem prím
    if m == 1:
        range_sieve[0] = False

    # Minden egyes prímmel megjelöljük a többi prímet a tartományban
    for prime in primes:
        # Az első többszörösét találjuk a prime-nak a [m, n] tartományban
        start = max(prime*prime, (m + prime - 1) // prime * prime)  # Kezdjük a max(prime^2, első többszörös)
        if start <= n:
            for i in range(start, n + 1, prime):
                range_sieve[i - m] = False
    
    # A prímek összegyűjtése a [m, n] tartományból
    primes_in_range = [i for i in range(m, n + 1) if range_sieve[i - m]]
    return primes_in_range

# Fő funkció, amely minden tesztesetre meghívja a szegmentált szita függvényt
def prime_generator(t, test_cases):
    # Először kiszámoljuk az összes prímet sqrt(10^9)-ig (ami 31622)
    max_limit = int(math.sqrt(1000000000)) + 1
    primes_up_to_sqrt = sieve_of_eratosthenes(max_limit)
    
    results = []
    
    # Minden tesztesetre alkalmazzuk a szegmentált szitát
    for m, n in test_cases:
        primes_in_range = segmented_sieve(m, n, primes_up_to_sqrt)
        results.append(primes_in_range)
    
    return results

# Bemenet beolvasása
if __name__ == '__main__':
    t = int(input().strip())  # Tesztesetek számának beolvasása
    test_cases = []
    
    # Minden tesztesetet beolvasunk
    for _ in range(t):
        m, n = map(int, input().split())  # M és N tartományok beolvasása
        test_cases.append((m, n))
    
    # A prímszámokat generáljuk és az eredményeket összegyűjtjük
    results = prime_generator(t, test_cases)
    
    # Az eredményeket kiírjuk a megadott formátumban
    for result in results:
        for prime in result:
            print(prime)
        print()
