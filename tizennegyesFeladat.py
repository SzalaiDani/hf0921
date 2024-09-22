def tizennegy():
    # 14. feladat – Kocka
    # A program olvasson be a konzolról egy egész számot! Ha a szám pozitív, akkor legyen a beolvasott szám egy kocka élének hossza. A program számítsa ki és írja ki a kocka felszínét, térfogatát a konzolra! Ha a szám nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kocka élének hossza nem pozitív!"!

    szam = int(input("Kérem adjon meg egy egész számot: "))

    if (szam >= 0):
        # térfogat
        terfogat = szam * szam * szam
        print("A kocka térfogata: "+str(terfogat))
        # felszín
        felszin = 6 * szam * szam
        print("A kocka felszíne: "+str(felszin))
    else:
        print("Hiba: a kocka élének hossza nem pozitív!")