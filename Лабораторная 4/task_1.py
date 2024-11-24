# TODO решите задачу

import json

def task() -> float:
    filename = "input.json"
    with open(filename) as file:
        data = json.load(file)

    sum_values = sum([item["score"] * item["weight"] for item in data])
    return round(sum_values, 3)


print(task())
