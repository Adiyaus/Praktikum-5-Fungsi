#include <stdio.h>

// Fungsi untuk menentukan nilai maksimal
int maksimal(int a, int b) {
    return (a > b) ? a : b;
}

// Fungsi untuk menentukan nilai minimal
int minimal(int a, int b) {
    return (a < b) ? a : b;
}

int main() {
    int bilangan, nilai;
    int maks = -100000;
    int minim = 100000;

    scanf("%d", &bilangan);

    for (int batas = 0; batas < bilangan; batas++) {
        scanf("%d", &nilai);
        maks = maksimal(maks, nilai);
        minim = minimal(minim, nilai);
    }

    printf("%d %d", maks, minim);

    return 0;
}
