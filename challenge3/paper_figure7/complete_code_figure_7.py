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
    duration = 30 * 86400000
    tx_rate = 1e6

    for n_nodes in list(range(1,10)) + list(range(10,100,10)) + list(range(100,1000,100)) + list(range(1000,1601,200)):
        print(f"Simulating {n_nodes} nodes")
        simulate(n_nodes, tx_rate, 0, duration, 1)
        simulate(n_nodes, tx_rate, 0, duration, 2)
        simulate(n_nodes, tx_rate, 0, duration, 3)
        simulate(n_nodes, tx_rate, 0, duration, 4)
        simulate(n_nodes, tx_rate, 0, duration, 8)
        simulate(n_nodes, tx_rate, 0, duration, 24)

    data_bs_1 = pd.read_csv("exp0BS1.dat", 
        delim_whitespace=True, comment="#", names=["nrNodes", "DER"])
    data_bs_2 = pd.read_csv("exp0BS2.dat", delim_whitespace=True, comment="#", names=["nrNodes", "DER"])
    data_bs_3 = pd.read_csv("exp0BS3.dat",delim_whitespace=True, comment="#", names=["nrNodes", "DER"])
    data_bs_4 = pd.read_csv("exp0BS4.dat", delim_whitespace=True, comment="#", names=["nrNodes", "DER"])
    data_bs_8 = pd.read_csv("exp0BS8.dat", delim_whitespace=True, comment="#", names=["nrNodes", "DER"])
    data_bs_24 = pd.read_csv("exp0BS24.dat", delim_whitespace=True, comment="#", names=["nrNodes", "DER"])
   
    plt.plot(data_bs_1["nrNodes"], data_bs_1["DER"], marker = 'o', label="1 sink")
    plt.plot(data_bs_2["nrNodes"], data_bs_2["DER"], marker = 'o', label="2 sink")
    plt.plot(data_bs_3["nrNodes"], data_bs_3["DER"], marker = 'o', label="3 sink")
    plt.plot(data_bs_4["nrNodes"], data_bs_4["DER"], marker = 'o', label="4 sink")
    plt.plot(data_bs_8["nrNodes"], data_bs_8["DER"], marker = 'o', label="8 sink")
    plt.plot(data_bs_24["nrNodes"], data_bs_24["DER"], marker = 'o', label="24 sink")

    plt.title("Success Rate (%)")
    plt.xlabel("Number of nodes")
    plt.ylabel("Rate")
    plt.legend()
    plt.grid()

    plt.savefig("figure7.pdf")
    plt.show()

if __name__ == '__main__':
    main()
