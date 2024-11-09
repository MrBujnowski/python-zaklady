retezec = input("Zadej řetězec pro zjičtění počtu znaků:")
ceska_abeceda = "AÁBCČDĎEÉĚFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž0123456789.?!,"

def charFrequency(retezec):
    list(retezec)
    vysledek ={}
    for char in retezec:
        if char in ceska_abeceda:
            vysledek[char] = vysledek.get(char, 0) + 1
    vysledek = list(vysledek.items())
    print(vysledek)

charFrequency(retezec)