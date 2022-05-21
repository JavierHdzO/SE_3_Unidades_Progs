void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int matrizA[2][2];
int matrizB[2][2];
int matrizC[2][2];

int controlVar = 0;
int contador = 0;
int fila = 0, columna = 0;
String currentMatriz = "A";
int v; //variable para recibir datos, tambien funciona como variable temporal.
void loop() {
  // put your main code here, to run repeatedly:
  switch (controlVar) {
    case 0://el caso 0 y 1 sirven para controlar la iteracion de las matrices separando filas y columnas.
      if (fila < 2) {
        controlVar = 1;
      } else {//si excede de 1 la fila quiere decir que acabo de iterar las dos filas de la matriz y se pasa a la siguiente matriz (que seria B)
        if (currentMatriz.equals("A")) {//Si estamos en matriz A, pasa a B
          currentMatriz = "B";
          fila = 0;
          columna =  0;
        } else {//Si estamos en B, cambia al case 4
          controlVar = 4;
          currentMatriz = "A"; //Se pasa al estado de impresion (case 4), reseteando este valor a A para imprimir primero esta.
        }
      }
      break;

    case 1:
      if (columna < 2) {
        controlVar = 2;
      } else {//si excede de 1 la columna, quiere decir que acabó de iterar la fila, por lo que se pasa a la siguiente fila, reseteando la columna.
        fila++;
        columna = 0;
        controlVar = 0;
      }
      break;

    case 2:
      Serial.println("INGRESA EL VALOR " + (String)fila + columna + " PARA LA MATRIZ " + currentMatriz);
      controlVar = 3;
      break;

    case 3://se leen y guardan los datos en las matrices
      if (Serial.available() > 0  ) {
        v = Serial.readString().toInt();
        Serial.println(v);

        if (currentMatriz.equals("A")) {
          matrizA[fila][columna] = v;
        } else {
          matrizB[fila][columna] = v;
        }

        controlVar = 0;
        columna++;
      }
      break;

    case 4://CALCULO
      for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
          for (int k = 0; k < 2; k++) {
            matrizC[i][j] += matrizA[i][k] * matrizB[k][j];
          }
        }
      }
      controlVar = 5;
      break;

    case 5:
      //impresion de las matrices de las matrices
      Serial.println("MATRIZ " + currentMatriz);
      for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
          Serial.print("[" + (String)v + "]" = (currentMatriz.equals("A")) ? matrizA[i][j] : matrizB[i][j]); //Se usa "v" como temporal para imprimir los datos de acuerdo a la matriz actual.
        }
        Serial.println("");
      }
      if (currentMatriz.equals("A")) {
        currentMatriz = "B"; //Si estamos en la matriz A, pasamos a la B para imprimirla,
      } else {
        Serial.println("MATRIZ C");
        for (int i = 0; i < 2; i++) {
          for (int j = 0; j < 2; j++) {
            Serial.print("[" + (String)matrizC[i][j] + "]");
          }
          Serial.println("");
        }
        controlVar = 6;
      }



      break;

    case 6:
      break;
  }
}
