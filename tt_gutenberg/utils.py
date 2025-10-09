# tt_gutenberg/data_utils.py
import pandas as pd

def load_data(csv_path: str) -> pd.DataFrame:
    """Load the Project Gutenberg author dataset as a DataFrame."""
    return pd.read_csv(csv_path)

def clean_alias_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing or non-string aliases."""
    df = df.dropna(subset=['alias', 'n_translated'])
    df = df[df['alias'].apply(lambda x: isinstance(x, str) and x.strip() != "")]
    return df

