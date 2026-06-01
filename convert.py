import gzip
import pandas as pd

records = []
current = {}

with gzip.open('data/finefoods.txt.gz', 'rt', encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.strip()
        if line == '':
            if current:
                records.append(current)
                current = {}
        elif ': ' in line:
            key, val = line.split(': ', 1)
            current[key] = val

print(f"Total records: {len(records)}")
df = pd.DataFrame(records[:100000])
df.to_csv('data/finefoods.csv', index=False)
print("Done! CSV saved!")