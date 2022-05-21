int leds[8] = {3, 4, 5, 6, 7, 8, 9, 10};

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);

}


int vNueva;
int v;
void loop() {
  // put your main code here, to run repeatedly:
  v= analogRead(A0);
  
  vNueva = map(v,0,1023,0,7); //permite pasar de un intervalo origen a un intervalo destino

  // V    = varaible a cambiar de ineervalo
  //0     = limite inferiro del intervalo origen
  //1023  = limite supperior del intervalo origen
  // 0    = limite inferior del intervalo destino
  // 7     = limite superior del intervalo destino.

  limpiar();

  digitalWrite(leds[vNueva],1);

  
  Serial.println("v: " +String(v) + " vNueva" +String(vNueva));
  delay(100);

}


void limpiar()
{
    for(int i = 0; i < 8; i++)
  {
    digitalWrite(leds[i],0);    
  }  
}
