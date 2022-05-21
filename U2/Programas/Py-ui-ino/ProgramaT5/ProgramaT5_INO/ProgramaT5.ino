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
int index = 0;
int pos = 0, stat = 0;

void loop() {

  if(Serial.available()>0)
  {
    limpiar();
    v =Serial.readString();
    index = 0;
    while( index < 9){
      pos = v.indexOf(",");
      stat = v.substring(0,pos).toInt();
      digitalWrite(leds[index], stat);
      v = v.substring(pos+1);
      index++;
    }
    
  }
  delay(100);
}

void limpiar() {
  for(int i=0; i < 8; i++)
  {
    digitalWrite(leds[i],0);
  }
}
