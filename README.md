# Internet of Things challenges - Politecnico di Milano 

## Description
Projects created for the Internet of Things (IoT) course at Politecnico di Milano.  
Every challenge consists of a practical project and some written exercises about topics seen during the course. 

### Challenge 1 
The goal of the project is to manage the occupancy of a parking lot based on ESP32 boards, ultrasonic distance sensors and ESP-NOW for the communication. The project also focuses on reducing the energy consumption and optimizing battery duration.  
The requirements can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/challenge1/assignment/Challenge1.pdf), while the documentation can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/challenge1/report-parking-lot/ReportParkingLot.pdf).

### Challenge 2
The goal of the project is to analyze network traffic related to IoT communication protocols like CoAP, MQTT and MQTT-SN, using Wireshark and PyShark to inspect the traffic.  
The requirements can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/challenge2/assignment/Challenge2.pdf), while the documentation can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/challenge2/packet-sniffing/PacketSniffing.pdf).

### Challenge 3 
The first goal of the project is to produce a Node-RED flow following a given specification. This flow needs to interact with an MQTT broker, read and write CSV files, plot charts using Node-RED UI and interact with a ThingSpeak channel. We also created a ThingSpeak channel, containing charts to display the contained data.  
The second goal of the project is to design a system using Arduino MKR WAN 1310,  reads temperature and humidity data from a DHT22 sensor and sends this data wirelessly to ThingSpeak over LoRaWAN.  
The third and last goal is to analyze the paper "Do LoRa Low-Power Wide-Area Networks Scale?" by M. Bor et al. and use the LoRa simulator [LoRaSim](https://www.lancaster.ac.uk/scc/sites/lora/lorasim.html) to reproduce some of the experiments conducted by the researchers.  
The requirements can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/challenge3/assignment/Challenge3.pdf), while the documentation can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/challenge3/NodeREDFlowReport/NodeREDFlowReport.pdf) and [here](https://github.com/kevinziroldi/iot-challenges/blob/main/challenge3/ExercisesLoRaWAN/ExercisesLoRaWAN.pdf).

### Challenge 4 (Homework)
The goal of the project is to design a low-cost IoT system to localize forklifts in real time, monitor their status (distance travelled, speed, etc.) and detect impacts. Forklifts operate in a logistic company warehouse, formed by an underground indoor area of 500 m<sup>2</sup> and a much larger outdoor area of 1 km<sup>2</sup>.  
The requirements can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/homework/assignment/Homework.pdf), while the documentation can be found [here](https://github.com/kevinziroldi/iot-challenges/blob/main/homework/IoTSystemForklift/IoTSystemForklift.pdf).

## Technologies and tools
In order to complete the different challenges, we used the following technologies and tools:
- [Wokwi ESP32 simulator](https://wokwi.com)
- [Wireshark](https://www.wireshark.org)
- [PyShark](https://github.com/KimiNewt/pyshark/)
- [Node-RED](https://nodered.org)
- [ThingSpeak](https://thingspeak.mathworks.com)
- [The Things Network](https://www.thethingsnetwork.org)
