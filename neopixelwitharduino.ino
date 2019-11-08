#include <Adafruit_NeoPixel.h>

int PIN = 6;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(16,PIN, NEO_GRB+NEO_KHZ800);

 

void setup() {

  pixels.begin();

  pixels.show();

  

}

 

void loop() {

  int val = analogRead(A0);

  int lightpwr = map(val,0,1023,0,255);

  pixels.setBrightness(lightpwr);

  color();   

  pixels.show();

  delay(200);

}

 

void color() {

  for (int i = 0; i<20; i++) {

    pixels.setPixelColor(i,pixels.Color(127,127,127));

  }

}
