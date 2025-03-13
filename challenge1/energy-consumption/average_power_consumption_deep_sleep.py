import pandas as pd 

# read CSV file 
dataset_deep_sleep = pd.read_csv("deep_sleep.csv", parse_dates=['Timestamp'])

# filter data with power < 100mW, referring to deep sleep mode
deep_sleep_data = dataset_deep_sleep[dataset_deep_sleep["Data"] < 100]

# compute average
deep_sleep_avg_power = deep_sleep_data["Data"].mean()

# print average 
print("Average power consumption deep sleep: ", deep_sleep_avg_power)

# Average power consumption deep sleep:  59.66093555093555
