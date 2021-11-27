#include <SoftwareSerial.h>
#include <DHT11.h>
DHT11 dht11(A1);
int Raindrops_pin= A0;
SoftwareSerial BTSerial(2, 3);   
int autoflag = 1;
void setup() {  
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if(autoflag == 1){
    int i;
    float humi, temp;
    int rain= analogRead(Raindrops_pin);
    delay(1000);
    if((i=dht11.read(humi, temp))==0){
  //    Serial.print("humidity: ");
  //    Serial.println(humi);
  //    Serial.print("temperature: ");
  //    Serial.println(temp);
      if(humi>60 && rain<200){
        Serial.println(5);
      }
      else if(temp > 25){
        Serial.println(6);
      }
      else if(temp<20){
        Serial.println(4);
      }
    }
  }
  if (BTSerial.available()){
    char data = BTSerial.read();
    if(data == 'a'){
      Serial.println(a);
      autoflag = 1;
    }
    if(data == 'b'){
      Serial.println(b);
      autoflag = 0;
    }
    if(autoflag == 0){    
//    Serial.write(data);
    
    if(data == '0'){
      Serial.println(0);
    }
    if(data == '1'){
      Serial.println(1);
    }
    if(data == '3'){
      Serial.println(3);
    }
    if(data == '4'){
      Serial.println(4);
    }
    if(data == '5'){
      Serial.println(5);
    }
    if(data == '6'){
      Serial.println(6);
    }
    if(data == '7'){
      int data2 = (int)(BTSerial.parseInt());
      Serial.println(7);
      delay(1000);
      Serial.println(data2);
    }
  }
  }
    
  if (Serial.available())
    BTSerial.write(Serial.read());
}
