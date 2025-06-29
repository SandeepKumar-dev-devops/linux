import pandas as pd

def extract():
    # Simulate pulling from an API or DB
    data = {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/raw_data.csv", index=False)
    print("Data extracted to data/raw_data.csv")

if __name__ == "__main__":
    extract()

