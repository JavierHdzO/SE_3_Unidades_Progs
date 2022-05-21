int leds[8] = {3, 4, 5, 6, 7, 8, 9, 10};
//Bit menos significativo - 10
//Bit menos significativo - 3

int estado = 0;
void setup() {

  Serial.begin(9600);
  Serial.setTimeout(100);
}

String valor;
int v = 0;
void loop() {

  switch (estado)
  {
    case 0:
      Serial.println("Ingresa un numero: ");

      estado = 1;
      break;

    case 1, 6:
      if (Serial.available() > 0)
      {
        v = Serial.readString();
        estado = 2;

      } else {
        estado = 1;
      }
      break;

    case 2,7:
      if (!valor.equals(""))
      {
        v = valor.toInt();
        if (estado == 2) {
          estado = 3;
        }
        else {
          if (v == 1) {
            estad0 = 5;
          }else{
            estado = 5;
           }
          }
        } else {
          if (estado == 2) {
            estado = 1;
          } else {
            estado = 6;
          }
        }
        break;

      case 3:
        v = v * v;
        estado = 4;
        break;

      case 4:
        Serial.println("El resultado " + v);
        estado = 5;
        break;

      case 5:
        Serial.println("Desea repetir programa? ");
        estado = 1;
        break;

      }
      delay(100);
  }
