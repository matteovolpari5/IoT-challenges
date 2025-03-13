import re
import statistics

# open log file
with open("log.txt", "r") as file:
    log_text = file.read()

# extract values from log using a regex 
idle_values = list(map(int, re.findall(r"Idle duration:\s*(\d+)", log_text)))
measurement_values = list(map(int, re.findall(r"Measurement duration:\s*(\d+)", log_text)))
sending_values = list(map(int, re.findall(r"Sending duration:\s*(\d+)", log_text)))
wifi_values = list(map(int, re.findall(r"WiFi duration:\s*(\d+)", log_text)))

# filter wrong values, given by the simulation
wifi_values = [value for value in wifi_values if value <= 200000]

# compute averages
avg_idle = statistics.mean(idle_values) if idle_values else 0
avg_measurement = statistics.mean(measurement_values) if measurement_values else 0
avg_sending = statistics.mean(sending_values) if sending_values else 0
avg_wifi = statistics.mean(wifi_values) if wifi_values else 0

print("Average Idle duration:", avg_idle)
print("Average Measurement duration:", avg_measurement)
print("Average Sending duration:", avg_sending)
print("Average WiFi duration:", avg_wifi)
