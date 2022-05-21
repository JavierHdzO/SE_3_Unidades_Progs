int leds[] = {12, 11, 10, 9, 8, 7, 6, 5, 4};
int limitesSuperiores[] = {2, 113, 226, 339, 452, 565, 678, 791, 904 };
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for (int i = 0; i <= 9; i++) {
    pinMode(leds[i], OUTPUT);
  }
}
int value = 0;
int i;
int contador = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if (value != analogRead(A0)) {
    value = analogRead(A0);
    Serial.println(value);
  }

  if (value == 0) {
    ledsOff();
  }
  else {
    for (i = 12; i >= 4; i--) {
      if (i >= 12 - howManyLedsOn()) {
        digitalWrite(i, 1);
      } else {
        digitalWrite(i, 0);
      }
    }
  }
}


int howManyLedsOn() {
  contador = -1;
  for (int j = 0; j < 9; j++) {
    contador = (value >= limitesSuperiores[j]) ? contador += 1 : contador += 0 ;
  }
  //Serial.println( "contador " + (String)contador);
  return contador;
}

void ledsOff() {
  for (int i = 0; i <= 9; i++) {
    digitalWrite(leds[i], 0);
  }
}
