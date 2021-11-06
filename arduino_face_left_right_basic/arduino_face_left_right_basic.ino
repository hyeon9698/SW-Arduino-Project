#include <cvzone.h>
#include<Servo.h>
#define TRIG 12 //TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO 13 //ECHO 핀 설정 (초음파 받는 핀)
#define TRIG2 10 //TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO2 11 //ECHO 핀 설정 (초음파 받는 핀)
SerialData serialData(2,3); //(numOfValsRec,digitsPerValRec)
Servo servo;
Servo servo2;
/*0 or 1 - 1 digit
0 to 99 -  2 digits 
0 to 999 - 3 digits 
 */
/* 오른쪽 112
 왼쪽 600
*/
int valsRec[2];
int x=90;
int y=90;
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
  servo2.write(y);
  
}
void loop() {
  //  long duration, distance;
  // digitalWrite(TRIG, LOW);
  // delayMicroseconds(2);
  // digitalWrite(TRIG, HIGH);
  // delayMicroseconds(10);
  // digitalWrite(TRIG, LOW);
  //  duration = pulseIn (ECHO, HIGH); //물체에 반사되어돌아온 초음파의 시간을 변수에 저장합니다.
  //  distance = duration * 17 / 1000; 

  //   long duration2, distance2;
  // digitalWrite(TRIG2, LOW);
  // delayMicroseconds(2);
  // digitalWrite(TRIG2, HIGH);
  // delayMicroseconds(10);
  // digitalWrite(TRIG2, LOW);
  //  duration2 = pulseIn (ECHO2, HIGH); //물체에 반사되어돌아온 초음파의 시간을 변수에 저장합니다.
  //  distance2 = duration2 * 17 / 1000; 
  
  serialData.Get(valsRec);
  /* if (distance<10)
   {
      x=30;
      y=90;
      servo.write(y);
      servo2.write(x);
    }
    else if (distance2<10){
      x=150;
      y=90;
      servo.write(y);
      servo2.write(x);
    }*/
    while (valsRec[0] != 0&&valsRec[1] != 0){
      serialData.Get(valsRec);
    if (valsRec[0]>370){//x축
      x-=1;
    }
    else if (valsRec[0]<300){
      x+=1;
    }
    if (valsRec[1]>260){//x축
      y-=1;
    }
    else if (valsRec[1]<200){
      y+=1;
    }
    if (x<0){
    x=0;
    }
    if (x>180){
      x=180;
    }
  
//  if (y<90){
//    y=90;
//  }
//  if (y>180){
//    y=180;
//  }
  servo.write(x);
    servo2.write(y);
    delay(100);
   serialData.Get(valsRec);
  }
  
}
