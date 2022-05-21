int leds[8] = { 8, 9, 10,11};
int potencio[5] = {A0, A1, A2, A3, A5};
int values[5] = {0, 0, 0, 0, 0};
int pushBs[4] = {3, 4, 5, 6};
int claseInst = 0;
int enviar = -1;
int tipoInst = 0;
int cont = 0;
int stateBefo = 1;
String clasesIris[3] = {"Iris-setosa","Iris-versicolor","Iris-virginica"};

String auxPot;
String cadena;

void setup() {
  // put your setup code here, to run once:
  for (int i  = 0; i < 4; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);

  cadena = "";
}

char v[8];
String cadenaAux = "";
int aux = 0;
//"AxxxxxxxxG"  donde x = {0, 1}
//A11100110G
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    cadena += Serial.readString();

    //Opciones:
    // 1 = cadena completa  COMPLETO
    // 2 = varias cadenas completas  COMPLETO
    // 3 = cadena incompleta
    //  3.1 = recibir la parte que acompleta a la cadena incompleta
    //  3.2 = recibid una cadena incompleta de inicio junto con una cadena completa despues
    // 4 = cadena completa y la parte final es una cadena incompleta


    int ultimaVezDeA = cadena.lastIndexOf("A");// -1 cuando no lo encuentra
    int ultimaVezDeG = cadena.lastIndexOf("G");// -1 cuando no lo encuentra

    String subCadena = "";

    if (cadenaAux.length() > 0)
    {
      int primeraVezDeG = cadena.indexOf("G");
      subCadena = cadena.substring(0, primeraVezDeG);
      subCadena = cadenaAux + subCadena;
      subCadena.replace("\n", "");
      cadenaAux = "";

    } else
    {

      if (ultimaVezDeA < ultimaVezDeG && ultimaVezDeA != -1 )
      {
        subCadena = cadena.substring(ultimaVezDeA + 1, ultimaVezDeG);

      } else if (ultimaVezDeA != -1)
      {
        cadenaAux = cadena.substring(ultimaVezDeA + 1);

      }

      cadena = "";
    }

   // Serial.println(subCadena);

  
    if (!subCadena.equals("4") && !subCadena.equals("9") && !subCadena.equals("13")) {
      if (subCadena.length() > 0 ) {
        subCadena.toCharArray(v, 8 + 1);
        aplicarSubCadena();
      }
    } else
    {
      tipoInst = subCadena.toInt();
      cont = 0;
      auxPot ="";
    }

  }


  //PROCESO 2 - lectura de boton clase

  //if cont == 0, sirve para saber si previamente ya se leyo la claseInst
  //en el caso de A4G, no aplica, solo para A10G Y A13G.
  if (cont == 0)
  {
    for (int i = 0; i < 3; i++)
    {
      aux = digitalRead(pushBs[i]);

      if (aux != 1)
      {
        digitalWrite(leds[3],0);
        claseInst = i + 1;
        break;
      }

    }

  }

  //if se quiere saber si claseInst ya tiene un valor entre [1-3]
  if (claseInst != 0)
  {
    enviar = digitalRead(pushBs[3]);

    if(enviar != stateBefo)
    {
      stateBefo = enviar;
    }else if (stateBefo == 0 && enviar == 0)
    {
      enviar = 1;  
    }
  }

  

  //PROCESO 3 - lectura de potenciometros y escritura serial

  // Si el boton enviar se esta presionando es 0, entonces se quiere imprimer o guardar el valor de los potenciometros
  if (enviar == 0) {
    for (int i = 0; i < 5; i++)
    {
      values[i] = map(analogRead(potencio[i]), 0, 1024, 1, 11);;
    }

    //Serial.println("A" + String(values[0]) + "," + String(values[1]) + "," + String(values[2]) + "," + String(values[3]) + "," + String(values[4]) + "," + String(claseInst) + "G");

    //Dependiendo del numero de tipoIns, se sabe si se guarda o imprimer el valor de los potenciometros.
    switch (tipoInst)
    {
      case 4: //Iris - tiene 4 variables
        Serial.println("A" + String(values[0]) + "," + String(values[1]) + "," + String(values[2]) + "," + String(values[3]) + "," + clasesIris[claseInst-1] + "G");
         digitalWrite(leds[3],1);
         claseInst = 0;
        break;
      case 9: //cancer tiene 9 variables
        
        if (cont == 0)
        {
          auxPot = "A" + String(values[0]) + "," + String(values[1]) + "," + String(values[2]) + "," + String(values[3]) + "," + String(values[4]);
          cont++;
         
        } else
        {
          Serial.println(auxPot + "," + String(values[0]) + "," + String(values[1]) + "," + String(values[2]) + "," + String(values[3])  +"," + String(claseInst*2) + "G");
          digitalWrite(leds[3],1);
          cont = 0;
          claseInst = 0;
          auxPot ="";
        }
        break;
      case 13: // Instancia wine - 13 variables
        if(cont == 0  ||  cont == 1)
        {
          auxPot += String(values[0]) + "," + String(values[1]) + "," + String(values[2]) + "," + String(values[3]) + "," + String(values[4])+",";
          cont++;
        }else
        {
          Serial.println("A" + auxPot + String(values[0]) + "," + String(values[1]) + "," + String(values[2]) + "," + String(claseInst) + "G");
          digitalWrite(leds[3],1);
          cont = 0;
          claseInst = 0;
          auxPot ="";
        }
        
    }
    enviar = - 1;
    
  }



  //PROCESO 3...

  //PROCESO N

  delay(100);

}

void aplicarSubCadena() {
  String vValor;
  // La cadena con un formato AxxxG llega.
  // Es convertida a entero
  for (int i  = 0; i < 3; i++) {
    vValor = String(v[i]);
   // Serial.println("It: " + String(i) + "  V: " + vValor);
    digitalWrite(leds[i], v[i] - 48);
    //digitalWrite(leds[i], vValor.toInt());
  }

  delay(1000);

  //Se apagan los les después de 1seg de encendido
  for (int i = 0; i < 3; i++)
  {
    digitalWrite(leds[i], 0);
  }
}
