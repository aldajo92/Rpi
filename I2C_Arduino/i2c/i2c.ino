#include <Wire.h>
#include <Servo.h> 

#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;

//Configuramos el servomotor
Servo myservo;

//Creamos los leds del panel de indicadores
int led1 = 13, led2 = 12, led3 = 11, led4 = 10;
char inChar;
int  inValue;
boolean chOp = false;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
  //Creamos el servo en el pin6
  myservo.attach(6);
  //Inicializamos los puertos para los leds
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
}

void loop(){
  if(chOp){
      switch(inChar){
        case 's':
          operation1();
          break; 
        case 'o':
          operation2();
          break;
        case 'p':
          operation3();
          break;
        case 'q':
          operation4();
          break;
        case 'a':
          operation5();
          break;
      }
      chOp = false;
  }
}

void operation1(){
  myservo.write(inValue);
}

void operation2(){
  if(inValue > 30){
    digitalWrite(led2,HIGH);
  }else{
    digitalWrite(led2,LOW);
  }
}

void operation3(){
  if(inValue > 30){
    digitalWrite(led3,HIGH);
  }else{
    digitalWrite(led3,LOW);
  }
}

void operation4(){
  if(inValue > 30){
    digitalWrite(led4,HIGH);
  }else{
    digitalWrite(led4,LOW);
  }
}

void operation5(){
  if(inValue == 0){
    Serial.print("a0 ");
    Serial.println(analogRead(A0));
  }else if(inValue == 1){
    Serial.print("a1 ");
    Serial.println(analogRead(A1));
  }
}

// callback for received data
void receiveData(int byteCount){
  while(Wire.available()) {
    number = Wire.read();
    Serial.print("data received: ");
    Serial.println(number);
    
    if (number == 1){
      if (state == 0){
        digitalWrite(13, HIGH); // set the LED on
        state = 1;
      }
      else{
        digitalWrite(13, LOW); // set the LED off
        state = 0;
      }
    }
  }
}

// callback for sending data
void sendData(){
  Wire.write(number);
}
