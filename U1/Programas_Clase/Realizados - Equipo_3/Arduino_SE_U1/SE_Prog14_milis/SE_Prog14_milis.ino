int leds[8] = {3, 4, 5, 6, 7, 8, 9, 10};

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);


}


long tiempoMiliseg;
void loop() {
  tiempoMiliseg = millis();

  Serial.println(tiempoMiliseg);
  delay(1000);

}


 
