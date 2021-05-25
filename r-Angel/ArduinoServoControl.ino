#include <Servo.h>
int pin=3;
int pin2=5;
Servo Servo1;
int x=0;
String str;
void setup() {
  pinMode(pin2, OUTPUT);
  Serial.begin(2000000);
  Servo1.attach(pin);
}

void loop() {
  
  digitalWrite(pin2,HIGH);
  while(!Serial.available()){
    digitalWrite(pin2,LOW);
    Servo1.write(x);
    
  }
  digitalWrite(pin2,HIGH);
  Servo1.write(x);
  str=Serial.readString();
  Servo1.write(x);
  x=str.toInt();
  Servo1.write(x);
    
  
}
