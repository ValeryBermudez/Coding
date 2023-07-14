#include <iostream>
#include <string>
using namespace std;

int numerosdevocales(string oracion){
    int total = 0;
    for (int i = 0; i < oracion.length(); i++) {
        char letra = oracion[i];
        if (letra == 'A' || letra == 'a' || letra == 'E' || letra == 'e' || letra == 'I' || letra == 'i' || letra == 'O' || letra == 'o' || letra == 'U' || letra == 'u'){
            total = total + 1;
        }
    }
    
    return total;
}

int main()
{
    string oracion;
    cout << "escribir una oracion: " << endl;
    cin >> oracion;
    
    cout << "El total de vocales es: " << numerosdevocales(oracion) << endl;
}
