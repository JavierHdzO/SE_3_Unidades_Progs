void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  Serial.println("PROGRAMA T15: Juego de Piedra, Papel o Tijera");
}

int estado = 0;
int valorP1, randomPC, repetir;
String lectura;
int combinaciones [3][3] =  {
  //Piedra, Papel, Tijera
  {0, -1, 1}, //Piedra
  {1, 0, -1}, //Papel
  { -1, 1, 0}, //Tijera
};
void loop() {
  // put your main code here, to run repeatedly:
  randomPC = random(1, 3);

  switch (estado) {

    case 0:
      Serial.println("Ingresa un numero:\n1.-[Piedra]\n2.-[Papel]\n3.-[Tijera]");
      estado = 1;
      break;

    case 1:
    case 5:
      if (Serial.available() > 0) {
        lectura = Serial.readString();
        if (estado == 1) {
          estado = 2;
        } else {
          estado = 6;
        }
      }
      break;

    case 2:
    case 6:
      if (!lectura.equals("")) {
        if (estado == 2) {
          valorP1 = lectura.toInt();
          if ((valorP1 > 0) and (valorP1 < 4)) {
            Serial.println(valorP1);
            estado = 3;
          } else {
            estado = 1;
          }
        } else {
          repetir = lectura.toInt();
          if (repetir == 1) {
            estado = 0;
          }
          else {
            estado = 4;
          }
        }
      } else {
        estado -= 1;
      }
      break;

    case 3:
      Serial.println("Valor de PC: " + String(randomPC));
      if ( (combinaciones[valorP1 - 1][randomPC - 1]) == 1 ) {
        Serial.println("GANASTE");
      } else if ((combinaciones[valorP1 - 1][randomPC - 1]) == 0) {
        Serial.println("EMPATE");
      } else {
        Serial.println("GANO LA PC");
      }
      estado = 4;
      break;

    case 4:
      Serial.println("Deseas Repetir el algoritmo? (1 = SI / 0 = NO)");
      estado = 5;
      break;

  }

  delay(100);
}
