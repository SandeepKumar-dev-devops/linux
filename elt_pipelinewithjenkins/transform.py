import pandas as pd

def transform():
    df = pd.read_csv("data/raw_data.csv")
    df["age_plus_ten"] = df["age"] + 10
    df.to_csv("data/transformed_data.csv", index=False)
    print("Data transformed and saved to data/transformed_data.csv")

if __name__ == "__main__":
    transform()

