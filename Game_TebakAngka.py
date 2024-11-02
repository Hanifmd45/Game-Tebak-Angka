import random
import os
hayoo = random.randint(1, 15)
print("="*50)
print("        Game Tebak Angka dari 1 sampai 15")
print("="*50)
nyawa = 4
while nyawa > 0:
    print(f"Nyawa anda yang tersisa = {nyawa}")
    nyawa -= 1
    jawab = int(input("Sebutkan angka yang akan muncul: "))
    if jawab == hayoo:
        print("Benarrr Cuyyy")
        break
    elif jawab > hayoo:
        print("Jawaban terlalu besar, coba lagi")
    elif jawab < hayoo:
        print("Jawaban terlalu kecil")
    elif nyawa == 0:
        break