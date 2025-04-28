import pandas as pd
import re

csv_path = 'challenge3.csv'
df = pd.read_csv(csv_path)

# Gli ACK validi (possono avere id o altre info dopo)
valid_ack_pattern = re.compile(r'^(Subscribe Ack|Connect Ack|Publish Ack)\b')

# --- Controlli ---
violazioni = []

for idx, info in df['Info'].fillna('').astype(str).items():
    # 1) Conta quante volte compare "Ack"
    ack_count = info.count('Ack')
    
    # 2) Se ce n'è più di uno, è violazione
    if ack_count > 1:
        violazioni.append((idx+1, info, 'Più di un Ack'))
        continue
    
    # 3) Se c'è esattamente un "Ack", verifichiamo che sia uno di quelli validi
    if ack_count == 1:
        if not valid_ack_pattern.match(info):
            violazioni.append((idx+1, info, 'Ack non consentito'))
        # altrimenti è OK
    # 4) Se ack_count == 0, non ci interessa (ad es. Publish Request o altro)

# --- Output ---
if violazioni:
    print("Messaggi NON conformi trovati:")
    for riga, testo, motivo in violazioni:
        print(f"  - Riga {riga}: “{testo}”  → {motivo}")
else:
    print("Nessuna violazione riscontrata.")
