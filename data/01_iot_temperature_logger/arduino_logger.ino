#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
void setup(){ Serial.begin(9600); dht.begin(); }
void loop(){
  float t=dht.readTemperature();
  float h=dht.readHumidity();
  if(!isnan(t)&&!isnan(h)){
    Serial.print(t); Serial.print(","); Serial.println(h);
  }
  delay(2000);
}