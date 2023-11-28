def NilaiMutlak(NilaiYangDiubah):
    NilaiYangDiubah = int(NilaiYangDiubah)

    if NilaiYangDiubah < 0:
        NilaiYangDiubah = NilaiYangDiubah * -1

    return NilaiYangDiubah

def HitungJarak(a, b, c, d):
    JarakX = a - c
    Hasil1 = NilaiMutlak(JarakX)

    JarakY = b - d
    Hasil2 = NilaiMutlak(JarakY)

    JarakAsli = Hasil1 + Hasil2

    return JarakAsli

bil1, bil2, bil3, bil4 = map(int, input().split())

Jarak = HitungJarak(bil1, bil2, bil3, bil4)
print(Jarak)

