#include <stdio.h>

void Biodata(int TahunLahir, char NamaLengkap[], char AsalKota[])
{
    int TahunSekarang = 2023;
    int umur = TahunSekarang - TahunLahir;
    printf("\nPerkenalkan Nama Saya : %s\n", NamaLengkap);
    printf("Umur Saya : %d\n", umur);
    printf("Saya adalah angkatan : %d\n", TahunSekarang);
    printf("Asal Saya dari : %s\n", AsalKota);
}
int main()
{
    int TahunLahir;
    char NamaLengkap[100], AsalKota[100];
    scanf(" %d",&TahunLahir);
    scanf(" %[^\n]%*c", NamaLengkap);
    scanf(" %[^\n]%*c", AsalKota);
    Biodata(TahunLahir, NamaLengkap, AsalKota);

    return 0;
}