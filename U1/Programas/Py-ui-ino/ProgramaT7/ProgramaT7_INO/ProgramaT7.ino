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

int values[8] = {1, 2, 4, 8, 16, 32, 64, 128};
int  cociente, residuo; //num decimal a leer
int val =-1, val2;
int k = 7;
void loop() {

  if (Serial.available() > 0)
  {
    val = Serial.readString().toInt();  
  }
  
  if ( val != -1) {
    val = val % 8;
    val2 = (val + 1)%8;    
    cociente = values[val] + values[val2];

    k = 7;
    while (cociente > 0) {
      residuo = cociente % 2;
      digitalWrite(leds[k--], residuo);
      cociente = cociente / 2;
    }

    for (; k >= 0; k--) {
      digitalWrite(leds[k], 0);
    }
    val = val +1;

  }else{
      limpiar();
    
    }
  delay(2000);
}


void limpiar(){
  for(int i =0; i < 8; i++){
      digitalWrite(leds[i],0);
   } 
 }
