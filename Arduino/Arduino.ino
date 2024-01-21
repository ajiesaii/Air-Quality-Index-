#include "MQ135.h"
#include "MQ7.h"

#define MQ135 A0
#define MQ7 A1

void setup() {
  Serial.begin(4800);
  pinMode(MQ135, INPUT);
  pinMode(MQ7, INPUT);

}

void loop() {
  //BACA NILAI CO2
  int valueMQ135 = analogRead(A0);
  //BACA NILAI CO
  int valueMQ7 = analogRead(A1);
  Serial.print(valueMQ7);
  Serial.print(",");
  Serial.print(valueMQ135);
  Serial.println();
  delay(10000);

}