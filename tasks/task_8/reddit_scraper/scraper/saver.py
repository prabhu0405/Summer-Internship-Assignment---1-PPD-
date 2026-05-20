import pandas as pd
import json


def save_csv(data, filename):
    """
    Save data to CSV.
    """

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    print(f"CSV saved: {filename}")


def save_json(data, filename):
    """
    Save data to JSON.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"JSON saved: {filename}")