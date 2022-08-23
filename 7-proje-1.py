# TAS KAGIT MAKAS OYUNU

# random kutuphanesinden randint ve choice import ettim
from random import randint, choice

# tas kagit makas icin sirasiyla "t" "k" "m"
SELECTION_LIST = ("t", "k", "m")

print("Tas Kagit Makas Oyununa Hos Geldiniz")
print("Tas icin 't', kagit icin 'k', makas icin 'm' kullaniniz ")

# Oyuncunun hamlesini aliyoruz
gamer = input("Hamleniz: ").lower()
# Karsi hamleyi choice fonksiyonu sayesinde seciyoruz
makine = choice(SELECTION_LIST)
print(f"Oyunun hamlesi: {makine}")

# Oyuna skor eklemek istedim 
# Bu yüzdendegiskenleri tanimladim
gamer_score = 0
makine_score = 0

# Oyundaki olusabilecek durumlari sonuclariyla kodladim
if gamer in SELECTION_LIST:
# Hatali harf girisini tespit icin bu kontrolu yaptirdim
    if gamer == makine:
    #  Berabere olma durumu
        print("skor yok")
    else:
    # Berabere olmasi disindaki durumlar
        if gamer == "t" and makine == "m":
            gamer_score += 1
            print("Tebrikler sen kazandin!")
        elif gamer == "t" and makine == "k":
            makine_score += 1
            print("Makine kazandı!")
        elif gamer == "k" and makine == "m":
            makine_score += 1
            print("Makine kazandı!")
        elif gamer == "k" and makine == "t":
            gamer_score += 1
            print("Tebrikler sen kazandin!")
        elif gamer == "m" and makine == "t":
            makine_score += 1
            print("Makine kazandi!")
        elif gamer == "m" and makine == "k":
            gamer_score += 1
            print("Tebrikler sen kazandin!")
    print (f"Makine: {makine_score} Sen: {gamer_score}")
    # GAME OVER yazisi yazdirmak istedim 
    # Bu yuzden eger makinenin skoru oyuncudan fazlaysa
    # calisacak bir karar yapisi yazdim
    if makine_score > gamer_score:
        print("GAME OVER")
else: 
    print("Hatali hamle yaptiniz. Oyun gecersiz.")