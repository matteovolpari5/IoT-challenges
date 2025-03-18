import csv
from datetime import datetime, timedelta

# initial timestamp
start_time = datetime(1970, 1, 1, 00, 00, 00, 000000)

segments = [
    (100000,      59.66),   # deep sleep 
    (30,       451.47),  # peak
    (833.70,   322.62),  # idle setup, delay +10000 to see better
    (18647.79, 465.18),  # measurement
    (30,       322.62),  # idle calculation, delay +10000 to see better
    (182801,   59.66),  # WiFi on, before transimission
    (59.60,    59.66),  # transmission
    (5900,     59.66),  # WiFi on, after transmission
    (100000,      59.66)    # deep sleep
]

# boundaries
boundaries = [0]
for duration, _ in segments:
    boundaries.append(boundaries[-1] + duration)
total_time = boundaries[-1]

# list of intervals 
seg_intervals = []
for i in range(len(segments)):
    start_seg = boundaries[i]
    end_seg = boundaries[i+1]
    power = segments[i][1]
    seg_intervals.append((start_seg, end_seg, power))

# step time (30 us)
step = 30

# create csv file
with open("power_profile_improved.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Timestamp", "Data"])
    
    t = 0
    while t <= total_time:
        for seg in seg_intervals:
            start_seg, end_seg, power = seg
            if start_seg <= t < end_seg:
                current_power = power
                break
        else:
            current_power = seg_intervals[-1][2]
        
        current_time = start_time + timedelta(microseconds=t)
        writer.writerow([current_time.strftime("%Y-%m-%d %H:%M:%S.%f"), f"{current_power:.2f}"])
        t += step

print("File successfully created: power_profile_improved.csv")
