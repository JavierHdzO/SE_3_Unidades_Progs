int push[5] = {3, 4, 5, 6, 7};
int value[5];
int leds[5] = {8, 9, 10, 11, 12};


void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 5; i++ ) {
    pinMode(push[i], INPUT_PULLUP);
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
}

int pushes = 0;
void loop() {

  for (int i = 0; i < 5; i++)
  {
    value[i] = digitalRead(push[i]);
  }

  //Serial.println( String(value[0])+ String(value[1])+ String(value[2])+ String(value[3])+ String(value[4]));


  for (int i = 1; i <= 5; i++)
  {
    pushes = pushes + (value[i-1]*i);
  }


  for (int i = 0; i < 5; i++)
  {
    digitalWrite(leds[i], 0);
  }
  
  
  Serial.println(pushes);
  switch (pushes)
  {
    case 14:
      digitalWrite(leds[0], 1);
      Serial.println(pushes);
      break;

    case 13:
      digitalWrite(leds[1], 1);
      Serial.println(pushes);
      break;

    case 12:

      digitalWrite(leds[2], 1);
      Serial.println(pushes);
      break;
    case 11:
      digitalWrite(leds[3], 1);
      Serial.println(pushes);
      break;
    case 10:
      digitalWrite(leds[4], 1);
      Serial.println(pushes);
      break;      
    
  }
  pushes = 0;
  delay(100);
  
}
