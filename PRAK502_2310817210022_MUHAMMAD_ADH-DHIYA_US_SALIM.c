#include <stdio.h>
#include <math.h>

// Fungsi untuk menghitung jarak antara dua titik
int hitung(int nilai1, int nilai2) {
    return nilai1 - nilai2;
}

// Fungsi untuk menghitung nilai mutlak
int mutlak(int angka) {
    return (angka < 0) ? -angka : angka;
}

int main() {
    int x1, y1, x2, y2;

    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

    int hasil = mutlak(hitung(x1, x2)) + mutlak(hitung(y1, y2));

    printf("%d", hasil);

    return 0;
}
    