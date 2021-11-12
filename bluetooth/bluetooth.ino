#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3);   

void setup() {  
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (BTSerial.available()){
    char data = BTSerial.read();
    
//    Serial.write(data);
    
    if(data == '0'){
      digitalWrite(13, LOW);
      Serial.println(0);
    }
    if(data == '1'){
      digitalWrite(13, HIGH);
      Serial.println(1);
    }
    if(data == '3'){
      digitalWrite(13, HIGH);
      Serial.println(3);
    }
    if(data == '4'){
      digitalWrite(13, HIGH);
      Serial.println(4);
    }
    if(data == '5'){
      digitalWrite(13, HIGH);
      Serial.println(5);
    }
    if(data == '6'){
      digitalWrite(13, HIGH);
      Serial.println(6);
    }
    if(data == '7'){
      int data2 = (int)(BTSerial.parseInt());
      Serial.println(7);
      delay(1000);
      Serial.println(data2);
    }
  }
    
  if (Serial.available())
    BTSerial.write(Serial.read());
}
