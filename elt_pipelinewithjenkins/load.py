import pandas as pd

def load():
    df = pd.read_csv("data/transformed_data.csv")
    # Simulate load into DB — here we just print
    print("Loaded data:")
    print(df)

if __name__ == "__main__":
    load()

