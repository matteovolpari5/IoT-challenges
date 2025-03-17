import pandas as pd 

# read CSV file 
dataset_transmission_power = pd.read_csv("transmission_power.csv", parse_dates=['Timestamp'])

# filter data with power >= 750mW and <= 900mW, referring to WiFi transmission at 2dBm
transmission_data = dataset_transmission_power[(dataset_transmission_power["Data"] >= 750) & (dataset_transmission_power["Data"] <= 900)]

# compute average
transmission_avg_power = transmission_data["Data"].mean()

# print average 
print("Average power consumption transmission at 2dBm: ", transmission_avg_power)

# Average power consumption transmission at 2dBm:  797.2942857142858
