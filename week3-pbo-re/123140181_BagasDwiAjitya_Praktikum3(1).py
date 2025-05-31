import math

try:
    user_input = input("Masukkan angka: ")
    angka = float(user_input)
    
    if angka < 0:
        print("Input tidak valid. Harap masukkan angka positif.")
    elif angka == 0:
        print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
    else:
        akar = math.sqrt(angka)
        print(f"Akar kuadrat dari {angka} adalah {akar}")
        
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang valid.")
