#include <Servo.h>
#include <SR04.h>

boolean OnOff;
int rightDistance;
int leftDistance;
int RootNote;
int Distance;
boolean RightIR;
boolean LeftIR;
boolean StartBtn;

Servo myServo8;
SR04 sr04_13(13, 12);

int mathRandomInt(int min, int max) {
  if (min > max) {
    // Swap min and max to ensure min is smaller.
    int temp = min;
    min = max;
    max = temp;
  }
  return min + (rand() % (max - min + 1));
}

// Describe this function...
void Right() {
  digitalWrite(5, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(10, LOW);
}

// Describe this function...
void Forward() {
  digitalWrite(5, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, HIGH);
}

// Describe this function...
void Left() {
  digitalWrite(5, LOW);
  digitalWrite(6, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(10, HIGH);
}

// Describe this function...
void Backward() {
  digitalWrite(5, LOW);
  digitalWrite(6, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, LOW);
}

// Describe this function...
void lookRight() {
  myServo8.write(45);
  delay(500);
  rightDistance = sr04_13.Distance();
  delay(100);
  myServo8.write(90);
}

// Describe this function...
void lookLeft() {
  myServo8.write(135);
  delay(500);
  leftDistance = sr04_13.Distance();
  delay(100);
  myServo8.write(90);
}

// Describe this function...
void Stop() {
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
}


void setup() {
  myServo8.attach(8);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(11, INPUT_PULLUP);
  pinMode(4, OUTPUT);


  myServo8.write(90);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  OnOff = false;
  rightDistance = 0;
  leftDistance = 0;
  lookRight();
  lookLeft();
  RootNote = 440;

}

void loop() {
  Distance = sr04_13.Distance();
  RightIR = digitalRead(A0);
  LeftIR = digitalRead(A1);
  StartBtn = digitalRead(11);
  if (OnOff == true) {
    if (Distance < 50 && Distance > 20) {
      tone(4,(RootNote * (mathRandomInt(1, 4) + (rand() / RAND_MAX))));
    } else {
      noTone(4);
    }
    if (LeftIR == 0 && RightIR == 0) {
      if (Distance <= 20 && Distance > 0) {
        Stop();
        delay(300);
        Backward();
        delay(400);
        Stop();
        delay(300);
        lookRight();
        delay(300);
        lookLeft();
        delay(300);
        if (leftDistance >= rightDistance) {
          Left();
          delay(500);
          Stop();
          delay(500);
        } else if (rightDistance > leftDistance) {
          Right();
          delay(500);
          Stop();
          delay(500);
        }
      } else {
        Forward();
      }
    } else if (LeftIR == 1 && RightIR == 0) {
      Left();
    } else if (LeftIR == 0 && RightIR == 1) {
      Right();
    } else if (LeftIR == 1 && RightIR == 1) {
      Stop();
    }
  }
  if (StartBtn == LOW && OnOff == false) {
    OnOff = true;
  } else if (StartBtn == LOW && OnOff == true) {
    OnOff = false;
  }

}