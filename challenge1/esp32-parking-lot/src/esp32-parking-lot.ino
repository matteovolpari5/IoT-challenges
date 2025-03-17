#include <esp_now.h>
#include <WiFi.h>

// 1 debug active, 0 not active
#define DEBUG 0

// 1 prints the time measurement, 0 doesn't 
// to be used with DEBUG off, because DEBUG introduces delays
#define TIME_MEASUREMENT 0

unsigned long board_start = 0;
unsigned long measurements_start = 0;
unsigned long wifi_start = 0;
unsigned long send_message_start = 0;
unsigned long send_message_end = 0;
unsigned long deep_sleep_start = 0;

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

  // set transmission power
  WiFi.setTxPower(WIFI_POWER_2dBm);

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
  if (DEBUG) {
    Serial.print("Send status: ");
    Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Message sent" : "Error sending message");
  }
}

// receiving callback
void OnDataRecv(const uint8_t * mac, const uint8_t *data, int len) {
  if (DEBUG) {
    Serial.print("Message received: ");
    char receivedString[len];
    memcpy(receivedString, data, len);
    Serial.println(String(receivedString));
  }
}

float getDistanceSensorMeasurement() {
  // start a new measurement
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // read result 
  int durationPulseMicros = pulseIn(ECHO, HIGH);
  float distanceCm = durationPulseMicros / 58;

  return distanceCm;
}

void setup() {
  if (TIME_MEASUREMENT) {
    board_start = micros();
  }
  
  // serial setup
  Serial.begin(115200);

  // pins setup 
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  if (TIME_MEASUREMENT) {
    measurements_start = micros();
    Serial.println("Idle duration: " + String(measurements_start - board_start));
  }

  // get a new measurement
  float distanceCm = getDistanceSensorMeasurement();
  // compute occupancy
  String occupancy = distanceCm <= DISTANCE_LIMIT ? "OCCUPIED" : "FREE";

  if (TIME_MEASUREMENT) {
    wifi_start = micros();
    Serial.println("Measurement duration: " + String(wifi_start - measurements_start));
  }

  // setup ESP-NOW
  setupESP_NOW();

  if (TIME_MEASUREMENT) {
    send_message_start = micros();
  }
  // send message
  esp_now_send(broadcastAddress, (uint8_t*)occupancy.c_str(), occupancy.length() + 1);
  if (TIME_MEASUREMENT) {
    send_message_end = micros();
    Serial.println("Sending duration: " + String(send_message_end - send_message_start));
  }
  
  if (DEBUG) {
    // add some delay to receive the message 
    delay(10);
  }

  // turn WiFi off 
  WiFi.mode(WIFI_OFF);

  if (TIME_MEASUREMENT) {
    deep_sleep_start = micros();
    Serial.println("WiFi duration: " + String(deep_sleep_start - wifi_start));
  }

  // set deep sleep time 
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  // go to deep sleep 
  esp_deep_sleep_start();
}

void loop() {
  // will never be called 
}