#include <MKRWAN.h>
#include <DHT.h>

#define DHTPIN 7
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

LoRaModem modem(Serial1);

// TTN credentials
String appEui = "0000000000000000";  
String appKey = "9D265EE3895BE505824143EBD5FDC46B";

void setup() {
  // initialization
  Serial.begin(115200);
  dht.begin();
  
  // LoRa module initialization
  if (!modem.begin(EU868)) {
    Serial.println("Errore avvio LoRa"); 
    while (1);
  }
  
  // join network server
  int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) {
    Serial.println("- Something went wrong; are you indoor? Move near a window and retry...");
    while (1);
  }
}

void loop() {
  // read humidity and temperature
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  
  // check readings 
  if (isnan(h) || isnan(t)) return;

  // encode reads 
  byte payload[4];
  int16_t tt = t * 100;
  int16_t hh = h * 100;
  payload[0] = highByte(tt);
  payload[1] = lowByte(tt);
  payload[2] = highByte(hh);
  payload[3] = lowByte(hh);

  // send message
  modem.beginPacket();
  modem.write(payload, sizeof(payload));
  modem.endPacket();

  // send a reading every minute 
  delay(60000);
}
