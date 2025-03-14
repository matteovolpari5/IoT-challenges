import pandas as pd
import matplotlib.pyplot as plt

# read CSV file 
df = pd.read_csv('deep_sleep.csv', parse_dates=['Timestamp'])

# plot data
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Data'], linestyle='-', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Power [mW]')
plt.title('Power consumption deep sleep')
plt.grid(True)

# save and shows
plt.savefig("power_consumption_deep_sleep.pdf", format="pdf", bbox_inches="tight")
plt.show()
