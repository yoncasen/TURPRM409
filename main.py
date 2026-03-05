import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Parolanın uzunluğu kaç olsun?"))

parola = ""

for i in range(uzunluk):
    parola += random.choice(karakterler)

print("Parolanız:", parola)
