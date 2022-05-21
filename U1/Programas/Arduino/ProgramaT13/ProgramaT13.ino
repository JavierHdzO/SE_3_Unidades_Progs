void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  // Distancia entre dos puntos
}

double X1 = -999, X2 = -999, Y1 = -999, Y2 = -999, resultado;
int estado = 0, repetir;
String lectura;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
      Serial.println("Ingresa X1: ");
      estado = 1;
      break;

    case 1:
    case 8:
      if (Serial.available() > 0) {
        lectura = Serial.readString();
        if ((estado == 1)) {
          estado = 2;
        } else {
          estado = 9;
        }
      }
      break;

    case 2:
    case 9:
      if (!lectura.equals("")) {
        if (estado == 2) {
          if (X1 == -999) {
            X1 = lectura.toDouble();
            Serial.println(X1);
            estado = 3;
          } else if (X2 == -999) {
            X2 = lectura.toDouble();
            Serial.println(X2);
            estado = 4;
          } else if (Y1 == -999) {
            Y1 = lectura.toDouble();
            Serial.println(Y1);
            estado = 5;
          } else {
            Y2 = lectura.toDouble();
            Serial.println(Y2);
            estado = 6;
          }
        } else {
          repetir = lectura.toInt();
          if (repetir == 1) {
            estado = 0;
          }
          else {
            estado = 7;
          }
        }
      } else {
        estado -= 1;
      }
      break;

    case 3:
      Serial.println("Ingresa X2: ");
      estado = 1;
      break;

    case 4:
      Serial.println("Ingresa Y1: ");
      estado = 1;
      break;

    case 5:
      Serial.println("Ingresa Y2: ");
      estado = 1;
      break;

    case 6:
      resultado = sqrt( pow((X2 - X1), 2) + pow((Y2 - Y1), 2) );
      Serial.println("Distancia entre dos puntos:  " + String(resultado));
      X1 = -999; X2 = -999; Y1 = -999; Y2 = -999;
      estado = 7;
      break;

    case 7:
      Serial.println("Deseas Repetir el algoritmo? (1 = SI / 0 = NO)");
      estado = 8;
      break;
  }

  delay(100);
}
