void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}
int sucesion1 = 0;
int sucesion2 = 0;
int num1 = 0;
int num2 = 0;
int controlVar = 0;
int continuar;
void loop() {
  // put your main code here, to run repeatedly:
  switch (controlVar) {
    case 2:
    case 0:
      if (controlVar == 0) {
        Serial.println("INTRODUCE EL NUMERO PARA LA PRIMERA SUCESION");
        controlVar = 1;
      } else {
        Serial.println("INTRODUCE EL NUMERO PARA LA SEGUNDA SUCESION");
        controlVar = 1;
      }

      break;

    case 1:
    case 4:
      if (Serial.available()) {
        if (num1 == 0) {
          num1 = Serial.readString().toInt();
          Serial.println(num1);
          controlVar = 2;
        } else if (num2 == 0) {
          num2 = Serial.readString().toInt();
          Serial.println(num2);
          controlVar = 3;
        } else {
          continuar = Serial.readString().toInt();
          Serial.println(continuar);
          controlVar = 5;
        }
      }
      break;


    case 3:
      Serial.println("SUCESIÓN 1: " + (String)sucesion1);
      Serial.println("SUCESIÓN 2: " +  (String)sucesion2);
      Serial.println("CONTINUAR SUCESIÓN? 1.SI / 2.NO(SALIR)");
      controlVar = 4;
      break;

    case 5:
      if (continuar == 1) {
        sucesion1 += num1;
        sucesion2 += num2;
        controlVar = 3;
      } else {
        exit(0);
      }

      break;
  }
}
