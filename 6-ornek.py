# Verilen order no ile istenilen bicimi elde edin
# istenilen bicim : 0000000103
# 10 haneli > basinda sifirla baslasin

order_no = 103

# Eklenecek 0lari hesapladim
zero_count = 10 - len(str(order_no))
# Altta bulunan kod satırında istedigim islemi kontrol ettim
# print(zero_count)
# bir de typenı kontrol ettim
# print(type(zero_count))

print((zero_count * "0")+ str(order_no))
"""
Bir baska cozum:
print(f"{order_no:0>10}")
Bu cozumu kullanmanızı oneririm
"""

