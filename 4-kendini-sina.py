invitation_list = [
    "Hakan Yalçınkaya",
    "Ercan Bozkurt",
    "Graham Chapman",
    "John Cleese",
    "Terry Gilliam",
    "Eric Idle",
    "Terry Jones",
    "Michael Palin",
]
# Davetli listesi olsun, input ile isim sor
# Eğer varsa girebilirsiniz desin

# Kullanıcının ismini aliriz
ad = input("Adinizi ve soy adinizi eksiksiz giriniz:")

# Listemizde olup olmadigini kontrol ederiz
if ad.capitalize() in invitation_list:
    print("Bu etkinlige girebilirsiniz. Hos geldiniz.")
else:
    print("Bu etkinlige davetli degilsiniz.")