#include <Servo.h>
int pin=3;
Servo Servo1;
int x=0;
String str;
void setup() {
  Serial.begin(2000000);
  Servo1.attach(pin);
}

void loop() {
  
  
  while(!Serial.available()){
    Servo1.write(x);
    delay(10);
  }
  Servo1.write(x);
  str=Serial.readString();
  Servo1.write(x);
  x=str.toInt();
  Servo1.write(x);
    
  
  

}
