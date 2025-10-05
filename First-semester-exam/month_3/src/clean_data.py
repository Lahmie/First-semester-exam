import pandas as pd

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    clean_df = df.copy()
    clean_df.timestamp = pd.to_datetime(clean_df.timestamp)
    clean_df.loc[clean_df.turbidity < 0, 'turbidity'] = 0
    return clean_df
