# no 1
def print_triangle(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))

try:
    height = int(input("Height: "))
    print_triangle(height)
except ValueError:
    print("Error")

# no 2
students = {}
num_students = int(input("Masukkan jumlah siswa: "))

for i in range(1, num_students + 1):
    name = input(f"Masukkan nama siswa ke-{i}: ")
    score = int(input(f"Masukkan nilai untuk {name}: "))
    students[name] = score

print("dictionary =", students)

# no 3
name = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
resolution = input("Masukkan Resolusi di Tahun ini: ")

with open("Me.txt", "w") as file:
    file.write(f"Nama: {name}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi Tahun ini: {resolution}\n")

print("File Me.txt telah berhasil dibuat!")
