#include <Arduino.h>
int Z=0,Y=0,X=0;
int D,C,B,A;

//Code released under GNU GPL.  Free to use for anything.
void disp_7447(int D, int C, int B, int A)
{
  digitalWrite(2, A); //LSB
  digitalWrite(3, B);
  digitalWrite(4, C);
  digitalWrite(5, D); //MSB

}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, INPUT);
    pinMode(7, INPUT);
    pinMode(8, INPUT);
    pinMode(13,OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
Z = digitalRead(6);//LSB
Y = digitalRead(7);
X = digitalRead(8);;//MSB
  A=(X&&Y)||(!X&&!Y)||(!Y&&Z);
  B=0;
  C=0;
  D=0;
  digitalWrite(13,HIGH);
  delay(500);
  digitalWrite(13,LOW);
  delay(500);

disp_7447(D,C,B,A);
}

