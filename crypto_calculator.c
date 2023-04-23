#include <stdio.h>
#include <stdlib.h>

// Prototipos de función de ensamblador
extern double convert_to_pesos(double value, double usd_to_pesos_rate);
extern double convert_to_euros(double value, double usd_to_euros_rate);

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Uso: ./crypto_calculator [valor_cripto] [tasa_usd_a_pesos] [tasa_usd_a_euros]\n");
        return 1;
    }

    double crypto_value = atof(argv[1]);
    double usd_to_pesos_rate = atof(argv[2]);
    double usd_to_euros_rate = atof(argv[3]);

    // Aquí llamarás a las funciones de ensamblador
    // y les pasarás los valores de tasas de cambio
    double crypto_in_pesos = convert_to_pesos(crypto_value, usd_to_pesos_rate);
    double crypto_in_euros = convert_to_euros(crypto_value, usd_to_euros_rate);

    printf("Valor en pesos: %.2f\n", crypto_in_pesos);
    printf("Valor en euros: %.2f\n", crypto_in_euros);

    return 0;
}
