#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

char sensorIdentifier;
char sensorStatus;

int irrigationPin = 4;
int fanPin = 3;

void setup() {
  
  
  
  Serial.begin(115200);
  
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Started ... ");
}

void loop() {
  sensorIdentifier = '\0';
  sensorStatus = '\0';
  
  while(Serial.available()) {
    sensorIdentifier = (char)Serial.read();
    sensorStatus = (char)Serial.read();
  }
  
  switch(sensorIdentifier) {
    case 'F' :
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Fan " + sensorStatus);
        break;

    case 'I' :
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Irrigazione " + sensorStatus);
        Serial.println("Irrigazione " + sensorStatus);
        break;

    case 'L' :
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Luce " + sensorStatus);
        Serial.println("Luce " + sensorStatus);
        break;
  }
  
}
