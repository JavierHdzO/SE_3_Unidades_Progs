int leds[8] = {3,4,5,6,7,8,9,10};

void setup() {
  // put your setup code here, to run once:
for(int i=0;i<8;i++)
{
  pinMode(leds[i],OUTPUT);
}
Serial.begin(9600);
Serial.setTimeout(100);
}

String v;
void loop() {

  if(Serial.available()>0)
  {
    v =Serial.readString().substring(0,8);
    
    Serial.print(v);
    digitalWrite(leds[v],1);
  }
  delay(100);
}
