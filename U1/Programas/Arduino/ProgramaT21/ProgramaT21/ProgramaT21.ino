void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

}

int controlVar = 0;
int multiplier;
int correct_answers = 0;
int answer;
int i = 1;
void loop() {
  // put your main code here, to run repeatedly:
  switch (controlVar) {
    case 0:
      Serial.println("Introduce a number to apply a multiplication table exam");
      controlVar = 1;
      correct_answers = 0;
      break;

    case 1:
    case 3:
    case 6: 
      if (Serial.available() > 0) {
        if (controlVar == 1) {
          multiplier = Serial.readString().toInt();
          Serial.println(multiplier);
          controlVar = 2;
          i = 1;
        } else if(controlVar == 3) {
          answer = Serial.readString().toInt();
          Serial.println(answer);
          correct_answers = (multiplier * i == answer) ? correct_answers += 1 : correct_answers += 0;
          i++;
          controlVar = 2;
        }else{
          answer = Serial.readString().toInt();
          controlVar = (answer == 1) ? 0 : 7;
        }
        
      }
      break;

    case 2:
      if (i <= 10) {
        Serial.println((String)multiplier + " x " + (String) i + "=" );
        controlVar = 3;
      } else {
        controlVar = 4;
      }
      break;

    case 4:
      Serial.println((String)correct_answers + " correct answers "  );
      controlVar = 5;
      break;

      case 5:
      Serial.println("Do you want to repeat the exam?  1. YES / 2. NO"  );
      controlVar = 6;
      break;

      case 7:
      exit(0); 
      break;
  }

}
