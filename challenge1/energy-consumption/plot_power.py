import pandas as pd
import matplotlib.pyplot as plt

# read CSV file 
df = pd.read_csv('transmission_power.csv', parse_dates=['Timestamp'])

# plot data
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Data'], linestyle='-', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Power [mW]')
plt.title('Power consumption transmission')
plt.grid(True)
plt.show()
