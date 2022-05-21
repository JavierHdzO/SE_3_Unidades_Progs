void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  // Área de un Polígono Regular de N Lados 
}

int nlados = -1;
double lado = -1, apotema = -1, resultado;
int estado = 0, repetir;
String lectura;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
      Serial.println("Ingresa el numero de lados: ");
      estado = 1;
      break;

    case 1:
    case 7:
      if (Serial.available() > 0) {
        lectura = Serial.readString();
        if ((estado == 1) or (estado == 3) or (estado == 4)) {
          estado = 2;
        } else {
          estado = 8;
        }
      }
      break;

    case 2:
    case 8:
      if (!lectura.equals("")) {
        if (estado == 2) {
          if (nlados == -1) {
            nlados = lectura.toInt();
            Serial.println(nlados);
            estado = 3;
          } else if(lado == -1) {
            lado = lectura.toDouble();
            Serial.println(lado);
            estado = 4;
          }else{
            apotema = lectura.toDouble();
            Serial.println(apotema);
            estado = 5;
          }
        } else {
          repetir = lectura.toInt();
          if (repetir == 1) {
            estado = 0;
          }
          else {
            estado = 6;
          }
        }
      } else {
        estado -= 1;
      }
      break;

    case 3:
      Serial.println("Ingresa el tamano del lado: ");
      estado = 1;
      break;

    case 4:
      Serial.println("Ingresa la apotema: ");
      estado = 1;
      break;

    case 5:
      resultado = nlados * lado;
      resultado = (resultado * apotema) / 2;
      Serial.println("Area del poligono regular:  " + String(resultado));
      nlados = -1; lado = -1; apotema = -1;
      estado = 6;
      break;

    case 6:
      Serial.println("Deseas Repetir el algoritmo? (1 = SI / 0 = NO)");
      estado = 7;
      break;
  }

  delay(100);
}
