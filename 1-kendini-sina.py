# 1. ADIM
# Kullanıcıdan adını, soyadını ve yaşını aldıktan sonra
# aşağıdaki gibi bir cümle kuran programı kodlayınız.
# Örnek Cümle:
# Ercan Bozkurt adlı kişi 39 yaşındadır.

# Kullanicidan istenilen bilgileri aliyoruz
ad = input("Adinizi giriniz:").capitalize()
soy_ad = input("Soy adinizi giriniz:").capitalize()
yas = input("Yasinizi giriniz:")

print(f"{ad} {soy_ad} adli kullanici {yas} yasindadir.")

# Egitimin basinda yukarıdaki gibi yazmayı bilmedigim icin bir alt satirdaki gibi kodlamistim
# print(ad, soy_ad,"adli kisi",yas,"yasindadir.")
# Bir baska yazim sekli:
# print(ad + " " + soy_ad + " adlı kişi " + yas + " yaşındadır.")

# 2. ADIM
# Hepsi küçük harflerle olacak şekilde
# ad ve soyad bilgilerini kullanarak
# email adresi oluşturup ekranda görüntüleyen
# programı kodlayınız.
# Örnek Adres: ercan.bozkurt@vakademi.com.tr

# Ad ve soy ad bilgilerini bir onceki adimda almistik
print(f"{ad.lower()}.{soy_ad.lower()}@vakademi.com.tr")

"""
Yukarıdaki gibi yazmayi bilmedigim donemde yazigim kodlar:
domain = "hotmail.com"
email = ad.lower() +"." +soy_ad.lower() +"@" +domain
print(email)
"""
# Yorum satirlarinda da gosterdigim orneklerle farkli yazim sekillerini inceleyebilirisniz