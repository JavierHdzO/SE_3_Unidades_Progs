void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  // Cuadrilatero
}


double altura = -1, ancho = -1, largo = -1, resultado;
int estado = 0, repetir;
String lectura;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
      Serial.println("Ingresa la altura: ");
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
          if (altura == -1) {
            altura = lectura.toInt();
            Serial.println(altura);
            estado = 3;
          } else if(ancho == -1) {
            ancho = lectura.toDouble();
            Serial.println(ancho);
            estado = 4;
          }else{
            largo = lectura.toDouble();
            Serial.println(largo);
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
      Serial.println("Ingresa el ancho: ");
      estado = 1;
      break;

    case 4:
      Serial.println("Ingresa lo largo: ");
      estado = 1;
      break;

    case 5:
      resultado = altura * ancho * largo;
      Serial.println("Volumen del cuadrilatero:  " + String(resultado));
      altura = -1; ancho = -1; largo = -1;
      estado = 6;
      break;

    case 6:
      Serial.println("Deseas Repetir el algoritmo? (1 = SI / 0 = NO)");
      estado = 7;
      break;
  }

  delay(100);
}
