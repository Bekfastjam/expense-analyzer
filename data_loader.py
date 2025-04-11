import pandas as pd

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df.drop_duplicates(inplace=True)
    return df