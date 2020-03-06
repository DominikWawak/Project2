#include <Servo.h>

int servoPin = 3;
int buttonPin = 2;

boolean buttonState = HIGH;
boolean lastButtonState = HIGH;

int locked = 80;
int unlocked = 180;




Servo Servo1;

void setup(){
  Servo1.attach(servoPin);
 pinMode(buttonPin, INPUT_PULLUP);
 digitalWrite(5, HIGH);
  
 }


void loop(){
  buttonState = digitalRead(buttonPin);
   if (buttonState != lastButtonState)
   {
      if (buttonState == LOW)
      {
         Servo1.write(unlocked);
         delay(2000);  
         Servo1.write(locked);
      }
      lastButtonState = buttonState;
   }
}


    
    

  /*
  Servo1.write(0);
  delay(1000);

   Servo1.write(90);
  delay(1000);

  

   Servo1.write(180);
  delay(1000);
*/
  
