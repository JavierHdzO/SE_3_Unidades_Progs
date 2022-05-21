int leds[8] = {3, 4, 5, 6, 7, 8, 9, 10};
//Bit menos significativo - 10
//Bit menos significativo - 3
void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);
}

int  cociente, residuo; //num decimal a leer
int k = 7, cont = 1, valor = 0;
void loop() {

  if (Serial.available() > 0)
  {
    valor = Serial.readString().toInt();
    cont = 0;
    while ( cont <=  valor ) {
      cociente = cont;
      k = 7;
      while (cociente > 0) {
        residuo = cociente % 2;
        digitalWrite(leds[k--], residuo);
        cociente = cociente / 2;
      }

      for (; k >= 0; k--) {
        digitalWrite(leds[k], 0);
      }
      cont++;
      delay(1000);
    }


  }
  delay(100);
}
