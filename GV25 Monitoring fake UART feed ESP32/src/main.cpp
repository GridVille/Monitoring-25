#include <Arduino.h>

// Define TX and RX pins for UART (change if needed)
#define TXD1 19
#define RXD1 21

// Use Serial1 for UART communication
HardwareSerial mySerial(1);



int counter = 0;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600, SERIAL_8N1, RXD1, TXD1);  // UART setup
  while(!mySerial){}                             // Loop until USB is ready
  
  Serial.println("ESP32 UART Transmitter");
}

void loop() {
  
  // Send message over UART
  mySerial.println("V0:" + String(sin(millis()*0.02)));
  mySerial.println("V1:" + String(sin(millis()*0.03)));
  mySerial.println("V2:" + String(sin(millis()*0.01)));
  mySerial.println("V3:" + String(sin(millis()*0.09)));

  Serial.println("Printed cycle " + String(counter));
  
  // increment the counter
  counter++;
  
  delay(500); 
}
