import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load sensor data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return pd.DataFrame()
