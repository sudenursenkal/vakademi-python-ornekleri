# Ad ve Soyad bilgilerinden oluşan bir listemiz var.
# Listede bulunan her kişinin adı ve soyadı yine bir liste olarak tanımlanmış.

users = [
    ['Hakan', 'Yalçınkaya', ],
    ['Ercan', 'Bozkurt', ],
    ['Ayşenur', 'Kara', ],
    ['Yasemin Duru', 'Eryılmaz Güngör', ],
]

# 1. Liste içindeki tüm kullanıcı isimlerini ve soyisimlerini ekrana yazdır

for user in users:
    print(user[0], user[1])

# 2. Kullanıcı adının ilk karakteri, soyadın ilk 3 karakteri
# gözükecek şekilde kalan kısımları yıldızlarla doldurarak
# bilgileri ekranda görüntüleyiniz.
# H**** Yal*******

for user in users:
    print(
        user[0][0] + ("*" * (len(user[0]) - 1)),
        user[1][:3] + ("*" * (len(user[1]) - 3))
        )
# Ismin uzunluguna bakip gorunen harf sayisini cikartinca
# istenen kadar yildiz kullanmis olduk.
