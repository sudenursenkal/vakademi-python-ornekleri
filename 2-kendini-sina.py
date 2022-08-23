# Ürün adı, fiyatı, vergi oranı ve adet bilgilerini kullanıcıdan alan,
# bu bilgileri kullanarak ödenmesi gereken toplam miktarı hesaplayan
# Hesaplama sonucunda aşağıdaki gibi bir sonucu ekranda görüntüleyen
# Python programını kodlayınız.

# Örnek Çıktı:
# 12 adet Mouse için ödenmesi gereken
# toplam miktar KDV dahil 123 Liradır.

# Kullanicidan sirayla gerekli bilgileri al
urun = input("Urunun ismini giriniz:")  # urun adi
fiyat = float(input("Urunun fiyatini giriniz:"))  # urunun fiyati
vergi = float(input("Uygulanacak vergi orani :"))  # vergi orani
adet = int(input("Urunden kac adet alacaginizi giriniz:"))  #adet bilgisi

# Odenecek tutari hesapliyoruz
tutar = adet * (fiyat + ((fiyat * vergi)/100))

# Ekrana yazdiriyoruz
print(f"{adet} adet {urun} icin odenmesi gereken \
    toplam mikar KDV dahil {tutar} Liradir.")

"""
bir baska  cozum

vergili_fiyat = fiyat + (fiyat * vergi / 100)
odenecek_toplam = vergili_fiyat * adet

cumle = str(adet) + " adet " + urun + \
    " için ödenmesi gereken toplam miktar KDV dahil " + \
    str(odenecek_toplam) + " Liradır."
print(cumle)
"""