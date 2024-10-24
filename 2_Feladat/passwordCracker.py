def passwordCracker(passwords, loginAttempt):
    # Memoizációs táblázat, tárolja, hogy egy részstring megoldható-e
    dp = [None] * (len(loginAttempt) + 1)
    dp[0] = []  # Alapeset: egy üres string megoldható jelszavak nélkül
    
    # Végigmegyünk a loginAttempt-en
    for i in range(len(loginAttempt)):
        if dp[i] is not None:
            # Minden jelszót ellenőrzünk, hogy illeszkedik-e a részstringhez i-től
            for password in passwords:
                if loginAttempt[i:i + len(password)] == password:
                    if i + len(password) <= len(loginAttempt):
                        # Ha találunk egyezést, bővítjük a dp táblát az új megoldással
                        dp[i + len(password)] = dp[i] + [password]
    
    # Ha az utolsó pozíció megoldható, visszaadjuk az összefűzött jelszavakat
    if dp[len(loginAttempt)] is not None:
        return ' '.join(dp[len(loginAttempt)])
    else:
        return "WRONG PASSWORD"

# Driver kód a több teszteset feldolgozásához
if __name__ == '__main__':
    t = int(input().strip())  # Tesztesetek száma
    for _ in range(t):
        n = int(input().strip())  # Jelszavak száma
        passwords = input().split()  # Jelszavak listája
        loginAttempt = input().strip()  # A bejelentkezési próbálkozás sztringje
        # Megoldjuk és kiírjuk az eredményt
        print(passwordCracker(passwords, loginAttempt))
