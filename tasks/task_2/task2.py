

import json
from collections import Counter

#reading text file
with open("text_file.txt", "r") as file:
    lines = file.readlines()

#counting occurances
log_count = Counter()

for line in lines:
    log_type = line.split()[0]
    log_count[log_type] += 1

#result in JSON file
with open("log_summary.json", "w") as json_file:
    json.dump(log_count, json_file, indent=4)

#frequent log type
most_frequent = max(log_count, key=log_count.get)

#output
print("\n--- Log Summary ---")

for key, value in log_count.items():
    print(f"{key}: {value}")

print(f"\nMost Frequent Log Type: {most_frequent}")