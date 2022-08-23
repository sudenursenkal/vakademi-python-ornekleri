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
