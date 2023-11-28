# Fungsi untuk menentukan nilai maksimal
def maksimal(a, b):
    return a if a > b else b

# Fungsi untuk menentukan nilai minimal
def minimal(a, b):
    return a if a < b else b

bilangan = int(input())
nilai_list = list(map(int, input().split()))

maks = -100000
minim = 100000

for nilai in nilai_list:
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)

print(f"{maks} {minim}")
