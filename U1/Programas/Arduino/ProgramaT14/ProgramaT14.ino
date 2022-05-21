void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  Serial.println("PROGRAMA T14: AREA DE UN TRIANGULO");
}

double base = -1, altura = -1, resultado;
int estado = 0, repetir;
String lectura;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
      Serial.println("Ingresa la base del triangulo: ");
      estado = 1;
      break;

    case 1:
    case 6:
      if (Serial.available() > 0) {
        lectura = Serial.readString();
        if ((estado == 1) or (estado == 3)) {
          estado = 2;
        } else {
          estado = 7;
        }
      }
      break;

    case 2:
    case 7:
      if (!lectura.equals("")) {
        if (estado == 2) {
          if (base == -1) {
            base = lectura.toDouble();
            Serial.println(base);
            estado = 3;
          } else {
            altura = lectura.toDouble();
            Serial.println(altura);
            estado = 4;
          }
        } else {
          repetir = lectura.toInt();
          if (repetir == 1) {
            estado = 0;
          }
          else {
            estado = 5;
          }
        }
      } else {
        estado -= 1;
      }
      break;

    case 3:
      Serial.println("Ingresa la altura del triangulo: ");
      estado = 1;
      break;

    case 4:
      resultado = (base * altura) / 2;
      base = -1;
      altura = -1;
      Serial.println("Area del triangulo: " + String(resultado));
      estado = 5;
      break;

    case 5:
      Serial.println("Deseas Repetir el algoritmo? (1 = SI / 0 = NO)");
      estado = 6;
      break;
  }

  delay(100);
}
