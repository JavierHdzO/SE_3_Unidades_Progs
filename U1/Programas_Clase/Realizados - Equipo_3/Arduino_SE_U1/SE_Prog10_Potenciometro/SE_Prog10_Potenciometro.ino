int leds[8] = {3, 4, 5, 6, 7, 8, 9, 10};

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);

}


int v;
void loop() {
  // put your main code here, to run repeatedly:
  v= analogRead(A0);

  Serial.println("v: " +String(v));
  delay(100);

}
