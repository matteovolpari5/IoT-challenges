import pandas as pd 

# read CSV file 
dataset_deep_sleep = pd.read_csv("deep_sleep.csv", parse_dates=['Timestamp'])
dataset_sensor_reading = pd.read_csv("sensor_read.csv", parse_dates=['Timestamp'])

# filter data with power between 200mW and 500mW, referring to idle mode
idle_data_deep_sleep = dataset_deep_sleep[(dataset_deep_sleep['Data'] >= 200) & (dataset_deep_sleep['Data'] <= 500)]
# filter data with power <= 400mW, reffering to idle mode
idle_data_sensor_reading = dataset_sensor_reading[dataset_sensor_reading['Data'] <= 400]

# merge values 
idle_merged = pd.concat([idle_data_deep_sleep, idle_data_sensor_reading], ignore_index=True)

# compute average
idle_avg_power = idle_merged['Data'].mean()

# print average 
print("Average power consumption idle: ", idle_avg_power)

# Average power consumption idle:  322.62464743589743
