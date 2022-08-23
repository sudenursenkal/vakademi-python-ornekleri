"""
Kullanicidan aldiginiz vize ve final
notlarini asagida belirtilen 
standartlara uygun hesaplayiniz.

Vize %30
Final %70

85-100 -> A
70-84  -> B
55-69  -> C
45-54  -> D
25-44  -> E
0-24   -> F

Sonucu hem puan, hem de harf olarak veriniz.
"""

# Kullanicidan vize ve final bilgilerini al
vize = float(input("Vize notunuzu giriniz:"))
final = float(input("Final notunuzu giriniz:"))

# Ondalikli sayida virgul degil nokta kullanilir
# Girilen vize ve final notuna gore ders notunu hesaplayalim
sonuc = (vize * 0.3) + (final * 0.7)
print(sonuc)
# Bir diger hesaplanma sekli:
# sonuc = (vize * .30) + (final * .70)

# Karar yapilarini kullanarak harf notunu buluyoruz
if sonuc >= 85:
    print("Harf notunuz: A")
elif sonuc >= 70:
    print("Harf notunuz: B")
elif sonuc >= 55:
    print("Harf notunuz: C")
elif sonuc >= 45:
    print("Harf notunuz: D")
elif sonuc >= 25:
    print("Harf notunuz: E")
else:
    print("Harf notunuz: F")

"""
Karar yapilarini bu sekilde de kullanabilirsiniz

if sonuc >= 85:
    harf = "A"
elif sonuc >= 70:
    harf = "B"
elif sonuc >= 55:
    harf = "C"
elif sonuc >= 45:
    harf = "D"
elif sonuc >= 25:
    harf = "E"
else:
    harf = "F"

print("Sonuç: ", sonuc, "Harf Değeri", harf)
"""