int ledPin = 9;      //  LED 핀
int inputPin = 7;     // 센서 신호핀
int pirState = LOW;   // 센서 초기상태는 움직임이 없음을 가정
int val = 0;          // 센서 신호의 판별을 위한 변수
 
void setup(){
    pinMode(ledPin, OUTPUT);    // LED를 출력으로 설정    
    pinMode(inputPin, INPUT);    // 센서 Input 설정
    Serial.begin(9600);         // 시리얼 통신, 속도는 9600
}
 
void loop(){
  val = digitalRead(inputPin);         // 센서 신호값을 읽어와서 val에 저장
    
  if (val == HIGH) {                   // 센서 신호값이 HIGH면(인체 감지가 되면)    
    digitalWrite(ledPin, HIGH);       // LED ON
    if (pirState == LOW){                         
         Serial.println("Welcome!");    // 시리얼 모니터 출력
         pirState = HIGH;
    } 
   } 
   else {                             // 센서 신호값이 LOW면(인체감지가 없으면)
    digitalWrite(ledPin, LOW);       // LED OFF
   if (pirState == HIGH){                
        Serial.println("Good Bye~");   // 시리얼 모니터 출력
        pirState = LOW;
    }
  }
}
