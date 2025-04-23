import os
import subprocess
import math
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def simulate(n_nodes, tx_rate, exp, duration):
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"

    # Use subprocess.run to execute the command and capture output
    result = subprocess.run(
        [
            "python2",
            "lorasim/loraDir.py",
            str(int(n_nodes)),
            str(int(tx_rate)),
            str(int(exp)),
            str(int(duration)),
            str(int(1))
        ],
        env=env,
        capture_output=True,
        text=True,  # Capture output as text
    )

# Der in aloha defined as S/G = e^(-2G)
def aloha_der(n_nodes,t):
    rate = 1e-6
    return math.exp(-2 * n_nodes * rate * t)

def main():
    duration = 58 * 86400000
    tx_rate = 1e6

    for n_nodes in list(range(1,10)) + list(range(10,100,10)) + list(range(100,1000,100)) + list(range(1000,1601,200)):
        print(f"Simulating {n_nodes} nodes")
        simulate(n_nodes, tx_rate, 4, duration)
        simulate(n_nodes, tx_rate, 3, duration)
        simulate(n_nodes, tx_rate, 5, duration)

    data_sn3 = pd.read_csv("exp4.dat", sep=" ")
    data_sn4 = pd.read_csv("exp3.dat", sep=" ")
    data_sn5 = pd.read_csv("exp5.dat", sep=" ")
    data_sn3["der"] = (data_sn3["nrTransmissions"] - data_sn3["nrCollisions"]) / data_sn3["nrTransmissions"]
    data_sn4["der"] = (data_sn4["nrTransmissions"] - data_sn4["nrCollisions"]) / data_sn4["nrTransmissions"]
    data_sn5["der"] = (data_sn5["nrTransmissions"] - data_sn5["nrCollisions"]) / data_sn5["nrTransmissions"]
    
    plt.plot(data_sn3["#nrNodes"], data_sn3["der"], marker = 'o', label="SN3")
    plt.plot(data_sn4["#nrNodes"], data_sn4["der"], marker = 'o', label="SN4")
    plt.plot(data_sn5["#nrNodes"], data_sn5["der"], marker = 'o', label="SN5")
    plt.title("Success Rate (%)")
    plt.xlabel("Number of nodes")
    plt.ylabel("Rate")
    plt.legend()
    plt.grid()

    plt.savefig("figure5.pdf")
    plt.show()

if __name__ == '__main__':
    main()
