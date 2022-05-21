void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  Serial.println("PROGRAMA T17: Leer numeros hasta que uno sea negativo");
}

int estado = 0, numero, cont = 0;
String lectura, numeros;
char* s;

void loop() {
  // put your main code here, to run repeatedly:

  switch (estado) {

    case 0:
      Serial.println("Ingresa el numero: ");
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
          Serial.print(lectura);
          numero = lectura.toInt();
          estado = 3;
        } else {
          if ((lectura.toInt()) == 1) {
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
      if (numero >= 0) {
        if (numero != 0) {
          if (cont == 0) {
            numeros = numeros + numero;
            estado = 0;
            cont += 1;
          }else{
            numeros = numeros + "," + numero;
            estado = 0;
          }
        }else{
          Serial.print("El 0 es neutro, ingresa otro numero: ");
          estado = 1;
        }
      } else {
        estado = 4;
      }
      break;

    case 4:
      Serial.println(String(numeros));
      numeros = "";
      Serial.print("Deseas Repetir el algoritmo? (1 = SI / 0 = NO)");
      estado = 5;
      break;

  }

  delay(100);

}
