#include <stdio.h>
#include <math.h>

int main() {
    float a;
    float b;
    a = 0;
    b = 0;
    printf("Calculatrice \n");
    printf("\n");
    printf("\n");

    printf("Valeur de a: %f\n", a);
    scanf ("%f", &a);
    printf("\n");

    printf("Valeur de b : %f\n", b);
    scanf ("%f", &b);
    printf("\n");
    
    float s;
    s = a-b;
    fabsf(s);
    printf("Valeur de a/b : %1f", s);
    getchar();
    return 0;
}