import pandas as pd
import matplotlib.pyplot as plt

# read CSV file - base
#df = pd.read_csv('power_profile.csv', parse_dates=['Timestamp'])
# read CSV file - improved
df = pd.read_csv('power_profile_improved.csv', parse_dates=['Timestamp'])

# plot data
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Data'], linestyle='-', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Power [mW]')
#plt.title('Power consumption implementation')
plt.title('Power consumption improved')
plt.grid(True)

# save and shows
#plt.savefig("power_consumption_implementation.pdf", format="pdf", bbox_inches="tight") 
plt.savefig("power_consumption_improved.pdf", format="pdf", bbox_inches="tight") 
plt.show()
