#include <esp_now.h>
#include <WiFi.h>

// pins 
#define TRIG 4
#define ECHO 2

// MAC receiver
uint8_t broadcastAddress[] = {0x8C, 0xAA, 0xB5, 0x84, 0xFB, 0x90};
// peer info
esp_now_peer_info_t peerInfo;

// deep sleep time
// person code 10773593: (93 % 50) + 5 = 48 seconds
#define TIME_TO_SLEEP 48
#define uS_TO_S_FACTOR 1000000

// distance [cm]
#define DISTANCE_LIMIT 50

// setup ESP-NOW
void setupESP_NOW() {
  // WiFi setup 
  WiFi.mode(WIFI_STA);
  esp_now_init();

  // send callback
  esp_now_register_send_cb(OnDataSent);
  // receive callback
  esp_now_register_recv_cb(OnDataRecv);

  // add peer
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  esp_now_add_peer(&peerInfo);
}

// sending callback
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("Send status: ");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Message sent" : "Error sending message");
}

// receiving callback
void OnDataRecv(const uint8_t * mac, const uint8_t *data, int len) {
  Serial.print("Message received: ");
  char receivedString[len];
  memcpy(receivedString, data, len);
  Serial.println(String(receivedString));
}

float getDistanceSensorMeasurement() {
  // start a new measurement
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // read result 
  int durationPulseMicros = pulseIn(ECHO, HIGH);    // TODO map ?
  float distanceCm = durationPulseMicros / 58;

  return distanceCm;
}

void setup() {
  // pins setup 
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  
  // setup ESP-NOW
  setupESP_NOW();

  // serial setup
  Serial.begin(115200);
}

void loop() {
  // get a new measurement
  float distanceCm = getDistanceSensorMeasurement();

  // compute occupancy
  String occupancy = distanceCm <= DISTANCE_LIMIT ? "OCCUPIED" : "FREE";

  // send message
  esp_now_send(broadcastAddress, (uint8_t*)occupancy.c_str(), occupancy.length() + 1);

  //delay(10);  // TODO 

  // set deep sleep time 
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  // go to deep sleep 
  esp_deep_sleep_start();

  // TODO debug
  // delay(5000);
}