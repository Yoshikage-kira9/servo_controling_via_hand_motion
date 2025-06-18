#include <Servo.h>

Servo servo;

int angel;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);


}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    angel= Serial.parseInt();
    angel= constrain(angel,0,180);
    servo.write(angel);
  }

}
