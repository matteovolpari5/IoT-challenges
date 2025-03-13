import pandas as pd 

# read CSV file 
dataset_sensor_reading = pd.read_csv("sensor_read.csv", parse_dates=['Timestamp'])

# filter data with power >= 400mW, referring to measurement 
measurement_data = dataset_sensor_reading[dataset_sensor_reading['Data'] >= 400]

# compute average
measurement_avg_power = measurement_data['Data'].mean()

# print average 
print("Average power consumption measurement: ", measurement_avg_power)

# Average power consumption measurement:  465.18097744360904