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

