#include <iostream>
using namespace std;

struct Alumno {

string nombre;
string codigo;
int notas[3];

};

int main() {
  Alumno estudiantes[3];

  for (int i = 0; i < 3; i++){
    
    cout << "ingrese el nombre del estudiante " << i << ": ";
    cin >> estudiantes[i].nombre;
    cout << "Ingrese el codigo del estudiante " << i << ": ";
    cin >> estudiantes[i].codigo;
    
    for (int y = 0; y < 3; y++){
      cout << "por favor ingrese la nota " << y << " del estudiante " << i << ": ";
      cin >> estudiantes[i].notas[y];
    }
    
  }
  
  for(int j = 0; j < 3; j++){
    Alumno* ap = &estudiantes[j];
    
    cout << "El estudiante " << j << " es: " << ap->nombre << " con codigo: " << ap->codigo << " tiene las siguientes notas: " << "\n";
    
    for(int x = 0; x < 3; x++){
      cout << "las notas de " << ap->nombre << " son: " << ap->notas[x] << "\n";
    }

  }
    
}
