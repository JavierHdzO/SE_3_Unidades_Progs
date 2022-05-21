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
String valores;
int  cociente, residuo; //num decimal a leer
int k = 7;
int pos = 0, v;
void loop() {

  if (Serial.available() > 0)
  {
    valores = Serial.readString();
  }

  if (!valores.equals(""))
  {
    pos = valores.indexOf(",");

    cociente = valores.substring(0, pos).toInt();
    k = 7;
    while (cociente > 0) {
      residuo = cociente % 2;
      digitalWrite(leds[k--], residuo);
      Serial.print(residuo);
      cociente = cociente / 2;
    }

    for (; k >= 0; k--) {
      digitalWrite(leds[k], 0);
      Serial.print("0");
    }
    valores = valores.substring(pos + 1);
    Serial.print("n");
    delay(5000);
    limpiar();

    
    if(pos == -1){ valores =""; Serial.print("e"); }
  }

  delay(200);
}


void limpiar() {

  for (int i = 0; i < 8; i++)
  {
    digitalWrite(leds[i], 0);
  }

}
