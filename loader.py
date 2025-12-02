import json

records = []
with open("examples/decision_sample.jsonl") as f:
    for line in f:
        records.append(json.loads(line))

print(records[0]["title"])
print(records[0]["reasoning_steps"])
