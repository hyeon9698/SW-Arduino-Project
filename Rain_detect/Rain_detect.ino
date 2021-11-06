int Raindrops_pin= A0;
int led=13;
void setup() {
  
  pinMode(led, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  int data= analogRead(Raindrops_pin);
  if (isnan(data)){
    Serial.println("Failed");
  }
  else if (data<800){
    digitalWrite(led,HIGH);
  }
  else{
    digitalWrite(led,LOW);
  }
  delay(500);
}
