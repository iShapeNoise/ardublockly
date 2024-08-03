int LEDs;
int ReadLight;
int i;

// Describe this function...
void updateShiftRegister() {
  digitalWrite(11, LOW);
  shiftOut(12, 9, LSBFIRST, LEDs);
  digitalWrite(11, HIGH);
}


void setup() {
  pinMode(11, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(A0, INPUT);

  digitalWrite(9, HIGH);
  digitalWrite(12, HIGH);
  LEDs = 0;

}

void loop() {
  ReadLight = analogRead(A0) / 57;
  if (ReadLight > 8) {
    ReadLight = 8;
  }
  LEDs = 0;
  int i_inc = 1;
  if (0 > ReadLight) {
    i_inc = -i_inc;
  }
  for (i = 0;
       i_inc >= 0 ? i <= ReadLight : i >= ReadLight;
       i += i_inc) {
    LEDs = LEDs + (1 << i);
  }
  updateShiftRegister();

}