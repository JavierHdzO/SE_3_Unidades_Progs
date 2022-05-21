void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  Serial.println("PROGRAMA T16: Leer N numeros y decir cuales son pares");
}

int estado = 0, numero, dato;
String lectura;
char* s;

void loop() {
  // put your main code here, to run repeatedly:

  switch (estado) {

    case 0:
      Serial.println("Ingresa los numeros separados por comas: ");
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
        dato = lectura.toInt();
        if (estado == 2) {
          estado = 3;
        } else {
          if (dato == 1) {
            estado = 0;
          } else {
            estado = 4;
          }
        }
      } else {
        estado -= 1;
      }
      break;

    case 3:
      s = strtok(lectura.c_str(), ",");
      while (s != NULL) {
        numero = String(s).toInt();
        if (numero % 2 == 0) {
          Serial.println("El numero {" + String(numero) + "} es PAR");
        }
        s = strtok(NULL, ",");
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
