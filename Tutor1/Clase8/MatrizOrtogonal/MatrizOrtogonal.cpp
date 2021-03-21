#include <MatrizOrtogonal.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

Nodo::Nodo(int fila, int columna, char * valor)
{
    this->fila = fila;
    this->columna = columna;
    this->valor = valor;
    this->abajo = NULL;
    this->arriba = NULL;
    this->derecha = NULL;
    this->izquierda = NULL;
}

Encabezado::Encabezado(int id)
{
    this->id = id;
    this->siguiente = NULL;
    this->anterior = NULL;
    this->acceso = NULL;
}

void ListaEncabezados::insertar(Encabezado * nuevo)
{
    if(primero == NULL)
    {
       primero = nuevo;
    }
    else
    {
        if(nuevo->id < primero->id) //Inserción al inicio
        {
            nuevo->siguiente = primero;
            primero->anterior = nuevo;
            primero = nuevo;
        }
        else
        {
            Encabezado * actual = primero;
            while(actual->siguiente != NULL)
            {
                if(nuevo->id < actual->siguiente->id) //Inserción en el medio
                {
                    nuevo->siguiente = actual->siguiente;
                    actual->siguiente->anterior = nuevo;
                    nuevo->anterior = actual;
                    actual->siguiente = nuevo;
                    break;
                }

                actual = actual->siguiente;
            }

            if(actual->siguiente == NULL) //Inserción al final
            {
                actual->siguiente = nuevo;
                nuevo->anterior = actual;
            }
        }
    }
}

Encabezado * ListaEncabezados::getEncabezado(int id)
{
    Encabezado * actual = primero;
    while(actual != NULL)
    {
        if(actual->id == id)
        {
            return actual;
        }

        actual = actual->siguiente;
    }

    return NULL;
}

Matriz::Matriz()
{
    this->eFilas = new ListaEncabezados();
    this->eColumnas = new ListaEncabezados();
}

void Matriz::insertar(int fila, int columna, char * valor)
{
    Nodo * nuevo = new Nodo(fila, columna, valor);

    //INSERCION_FILAS
    Encabezado * eFila = eFilas->getEncabezado(fila);
    if(eFila == NULL) //Si no existe encabezado se crea.
    {
        eFila = new Encabezado(fila);
        eFilas->insertar(eFila);
        eFila->acceso = nuevo;
    }
    else
    {
        if(nuevo->columna < eFila->acceso->columna) //Inserción al inicio
        {
            nuevo->derecha = eFila->acceso;
            eFila->acceso->izquierda = nuevo;
            eFila->acceso = nuevo;
        }
        else
        {
            Nodo * actual = eFila->acceso;
            while(actual->derecha != NULL)
            {
                if(nuevo->columna < actual->derecha->columna) //Inserción en el medio
                {
                    nuevo->derecha = actual->derecha;
                    actual->derecha->izquierda = nuevo;
                    nuevo->izquierda = actual;
                    actual->derecha = nuevo;
                    break;
                }

                actual = actual->derecha;
            }

            if(actual->derecha == NULL) //Inserción al final
            {
                actual->derecha = nuevo;
                nuevo->izquierda = actual;
            }
        }
    }
    //FIN_FILAS

    //INSERCION_COLUMNAS
    Encabezado * eColumna = eColumnas->getEncabezado(columna);
    if(eColumna == NULL) //Si no existe encabezado se crea.
    {
        eColumna = new Encabezado(columna);
        eColumnas->insertar(eColumna);
        eColumna->acceso = nuevo;
    }
    else
    {
        if(nuevo->fila < eColumna->acceso->fila) //Inserción al inicio
        {
            nuevo->abajo = eColumna->acceso;
            eColumna->acceso->arriba = nuevo;
            eColumna->acceso = nuevo;
        }
        else
        {
            Nodo * actual = eColumna->acceso;
            while(actual->abajo != NULL)
            {
                if(nuevo->fila < actual->abajo->fila) //Inserción en el medio
                {
                    nuevo->abajo = actual->abajo;
                    actual->abajo->arriba = nuevo;
                    nuevo->arriba = actual;
                    actual->abajo = nuevo;
                    break;
                }

                actual = actual->abajo;
            }

            if(actual->abajo == NULL) //Inserción al final
            {
                actual->abajo = nuevo;
                nuevo->arriba = actual;
            }
        }
    }
    //FIN_COLUMNAS
}

void Matriz::recorrerFilas()
{
    Encabezado * eFila = eFilas->primero;
    cout << "Recorrido Por Filas: ";

    while(eFila != NULL)
    {
        Nodo * actual = eFila->acceso;
        while(actual != NULL)
        {
            cout << actual->valor;
                cout << actual->fila;
                cout << actual->columna;

            if(eFila->siguiente != NULL || actual->derecha != NULL)
            {
                cout << "->";
            }


            actual = actual->derecha;
        }

        eFila = eFila->siguiente;
    }

    cout << endl;
}

void Matriz::recorrerColumnas()
{
    Encabezado * eColumna = eColumnas->primero;
    cout << "Recorrido Por Columnas: ";

    while(eColumna != NULL)
    {
        Nodo * actual = eColumna->acceso;
        while(actual != NULL)
        {
            cout << actual->valor;

            if(eColumna->siguiente != NULL || actual->abajo != NULL)
            {
                cout << "->";
            }

            actual = actual->abajo;
        }

        eColumna = eColumna->siguiente;
    }

    cout << endl;
}
