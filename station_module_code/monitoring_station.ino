#include <DHT.h>

#define DHTPIN 2
#define DHT_TYPE DHT11

DHT dht(DHTPIN, DHT_TYPE);

void setup() {

  Serial.begin(9600);
  dht.begin();
}


void loop() {

  String received_data = "";
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  if (Serial.available())
  {


    while (Serial.available() > 0)
    {
      received_data += (char)Serial.read();
    }
    Serial.print(received_data);
    Serial.flush();
    Serial.end();
    Serial.begin(9600);
  }

  if (received_data == "R")
  {
    delay(500);
    Serial.print("T"+String(temperature)+";H"+ String(humidity));
    Serial.flush();
    Serial.end();
    Serial.begin(9600);
  }

  delay(1000);
}
