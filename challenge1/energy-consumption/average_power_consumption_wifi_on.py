import pandas as pd 

# read CSV file 
dataset_deep_sleep = pd.read_csv("deep_sleep.csv", parse_dates=['Timestamp'])
dataset_transmission_power = pd.read_csv("transmission_power.csv", parse_dates=['Timestamp'])

# filter data with power >= 600mW, referring to WiFi on mode
wifi_on_data_deep_sleep = dataset_deep_sleep[dataset_deep_sleep['Data'] >= 600]
# filter data with power <= 750mW, reffering to WiFi on mode
wifi_on_data_transmission_power = dataset_transmission_power[dataset_transmission_power["Data"] <= 750]

# merge values 
wifi_on_merged = pd.concat([wifi_on_data_deep_sleep, wifi_on_data_transmission_power], ignore_index=True)

# compute average
wifi_on_avg_power = wifi_on_merged['Data'].mean()

# print average 
print("Average power consumption WiFi on: ", wifi_on_avg_power)

# Average power consumption WiFi on:  724.5793571428571
