#include <cvzone.h>
#include<Servo.h>
#define TRIG 12 //TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO 13 //ECHO 핀 설정 (초음파 받는 핀)
#define TRIG2 10 //TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO2 11 //ECHO 핀 설정 (초음파 받는 핀)
SerialData serialData(2,3); //(numOfValsRec,digitsPerValRec)
Servo servo;
Servo servo2;
/* 오른쪽 112
 왼쪽 600
*/
int rec=5;
int playe=4;
int inputPin=6;
int val=0;
int valsRec[2];
int x=90;
int y=90;
int z = 0;
void setup() {
  servo.attach(7);
  servo2.attach(8);
  serialData.begin();
  Serial.begin(9600);
   pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
   pinMode(TRIG2, OUTPUT);
  pinMode(ECHO2, INPUT);
  servo.write(x);
  delay(1000);
  servo2.write(y);
  pinMode(inputPin,INPUT);
//  digitalWrite(rec,HIGH);
//  delay(10000);
//  digitalWrite(rec,LOW);
}
void loop() {
  serialData.Get(valsRec);
  if (valsRec[0]==0&&valsRec[1]==0){
    val=digitalRead(inputPin);
  long duration, distance;
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  duration = pulseIn (ECHO, HIGH); 
  distance = duration * 17 / 1000; 
  long duration2, distance2;
  digitalWrite(TRIG2, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG2, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG2, LOW);
  duration2 = pulseIn (ECHO2, HIGH); 
  distance2 = duration2 * 17 / 1000; 
   if (val==HIGH){
     if (distance<20||distance2<20){
        digitalWrite(playe,HIGH); 
        delay(10);
        digitalWrite(playe,LOW);
     }
    }
  }
    while (valsRec[0] != 0&&valsRec[1] != 0){
      val=digitalRead(inputPin);
  long duration, distance;
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  duration = pulseIn (ECHO, HIGH); 
  distance = duration * 17 / 1000; 
  long duration2, distance2;
  digitalWrite(TRIG2, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG2, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG2, LOW);
  duration2 = pulseIn (ECHO2, HIGH); 
  distance2 = duration2 * 17 / 1000; 
   if (val==HIGH){
     if (distance<20||distance2<20){
        digitalWrite(playe,HIGH); 
        delay(10);
        digitalWrite(playe,LOW);
     }
    }
      serialData.Get(valsRec);
    if (valsRec[0]>340){//x축
      x-=2;
    }
    if (valsRec[0]<240){
      x+=2;
    }
    if (valsRec[1]>280){//y축
      y-=1;
    }
    if (valsRec[1]<200){
      y+=1;
    }
    if (x<0){
    x=0;
    }
    if (x>180){
      x=180;
    }
     if (y<80){
       y=80;
    }
    if (y>140){
      y=140;
    }
    servo.write(x);
    servo2.write(y);
    delay(100);
   serialData.Get(valsRec);
   valsRec[0] = 0;
   valsRec[1] = 1;
  }
  
}
