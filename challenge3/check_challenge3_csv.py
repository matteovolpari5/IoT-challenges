import pandas as pd
import json 

df = pd.read_csv("challenge3.csv")

# filter MQTT PUBLISH messages 
publish_df = df[df['Info'].str.contains('Publish Message', na=False)]

# filter ACK messages 
ack_df = df[df['Info'].str.contains("Connect Ack", na=False)] + df[df['Info'].str.contains("Publish Ack", na=False)] + df[df['Info'].str.contains("Subscribe Ack", na=False)]

invalid_rows_publish = []
invalid_rows_ack = []

# find invalid PUBLISH messages
for idx, raw_payload in zip(publish_df.index, publish_df['Payload']):
    payload_str = raw_payload if isinstance(raw_payload, str) else ''
    if not payload_str.strip():
        continue
    try:
        json.loads(f'[{payload_str}]')
    except json.JSONDecodeError as e:
        print(f"Errow No. {idx+1}: {e}")
        invalid_rows_publish.append(idx + 1)
print("No. invalid rows publish:", invalid_rows_publish)

# find invalid ACK messages
for idx, raw_payload in zip(ack_df.index, ack_df['Payload']):
    payload_str = raw_payload if isinstance(raw_payload, str) else ''
    if not payload_str.strip():
        continue
    try:
        json.loads(f'[{payload_str}]')
    except json.JSONDecodeError as e:
        print(f"Errow No. {idx+1}: {e}")
        invalid_rows_ack.append(idx + 1)
print("No. invalid rows ack:", invalid_rows_ack)