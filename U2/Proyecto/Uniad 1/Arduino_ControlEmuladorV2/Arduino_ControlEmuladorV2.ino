const int pulsadores[7] = {3, 4, 5, 6, 7, 8, 9};
String botones;

void setup() {
  for (int i = 0; i < 7; i++) {
    pinMode(pulsadores[i], INPUT_PULLUP);
  }
  Serial.begin(9600);
}

void loop() {
  
  for (int i = 6; i>=0; i--) {
    if (digitalRead(pulsadores[i]) == 1) {
      botones += String(i);
    }
  }

  Serial.println(botones);
  botones = "";
  delay(100);
}
