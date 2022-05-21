int leds[8] = {3, 4, 5, 6, 7, 8, 9, 10};

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);


}


long tiempoCambioAnterior = 0;
long tiempoActual;
int cont = 0;
boolean estadoLED = false;
void loop() {
  
  tiempoActual = millis();
  Serial.println(tiempoActual);
  
  if(tiempoActual - tiempoCambioAnterior >= 1000 ){
    estadoLED =  !estadoLED;
    for(int i = 0; i < 8; i++)
    {
      digitalWrite(leds[cont], 0);
    
    }

    digitalWrite(leds[cont], 1);
    tiempoCambioAnterior = tiempoActual;
  }

  if (cont == 7)
  {
    cont = 0;  
  }
  cont ++;
}


 
