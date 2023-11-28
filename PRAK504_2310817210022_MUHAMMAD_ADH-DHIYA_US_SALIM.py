# Fungsi untuk membalikkan representasi desimal
def reverse(n):
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n //= 10
    return reversed_num

# Input
A, B = map(int, input().split())

# Membalikkan representasi desimal A dan B
A = reverse(A)
B = reverse(B)

# Menjumlahkan A dan B
C = A + B

# Membalikkan representasi desimal hasil penjumlahan C
result = reverse(C)

# Output
print(result)
