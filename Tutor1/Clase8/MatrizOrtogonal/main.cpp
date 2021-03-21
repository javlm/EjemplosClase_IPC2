#include <iostream>
#include <MatrizOrtogonal.h>
#include <string.h>
using namespace std;

int main()
{
    Matriz * matriz = new Matriz();
    matriz->insertar(1, 0, "silla");
    matriz->insertar(2, 1, "arbol");
    matriz->insertar(0, 1, "casa");
    matriz->insertar(1, 2, "zapato");
    matriz->insertar(0, 2, "mesa");
    matriz->insertar(0, 0, "avion");

    matriz->recorrerColumnas();
    matriz->recorrerFilas();
    delete matriz;

    return 0;
}

