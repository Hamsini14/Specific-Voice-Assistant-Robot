char command;

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT); 
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    command = Serial.read();

    switch (command) {
      case 'F': 
        moveForward();
        break;
      case 'B': 
        moveBackward();
        break;
      case 'L': 
        turnLeft();
        break;
      case 'R': 
        turnRight();
        break;
      case 'S': 
        stopMotors();
        break;
 
    }
  }
}

void turnLeft() {
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, HIGH);
}

void turnRight() {
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, LOW);
}

void moveForward() {
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(10, HIGH);
  digitalWrite(11, LOW);
}

void moveBackward() {
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(10, LOW);
  digitalWrite(11, HIGH);
}

void stopMotors() {
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
}
