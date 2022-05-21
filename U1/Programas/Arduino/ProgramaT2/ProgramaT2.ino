const int lengthLeds = 8;
const int lengthLedsH = 3;
int leds[lengthLeds] = {3, 4, 5, 6, 7, 8, 9, 10};
int ledsHigh[lengthLedsH] = { -1, -1, -1};



void setup() {
  for (int i = 0; i < lengthLeds; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  randomSeed( analogRead(A0) );
  Serial.begin(9600);

}

int numRnd = 0;
int numGet = 0;
int uaxRnd = 0;

void loop() {
  do
  {
    uaxRnd = random(8);
    numRnd = leds[uaxRnd];
    
  } while ( !valida(numRnd));

  numGet = swap();

  ledsHigh[lengthLedsH - 1] = numRnd;
  if(numGet != -1)
  {
    digitalWrite(numGet, 0);
  }
  
  digitalWrite(ledsHigh[lengthLedsH-1], 1);

  for(int i=0;i<3;i++)
  {
    Serial.println(ledsHigh[i]);
  }
  delay(3000);

}


int swap(  )
{
  int aux = ledsHigh[0];
  for (int i = 1; i < lengthLedsH; i++)
  {
    ledsHigh[i-1] = ledsHigh[i];
  }

  return aux;
}

bool valida( int numRnd )
{
  for (int i = 0; i < lengthLedsH; i++)
  {
    if ( ledsHigh[i] == numRnd )
    {
      return false;
    }
  }
  return true;
}
