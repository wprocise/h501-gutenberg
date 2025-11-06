# utils.py
import pandas as pd

def load_gutenberg_dataset(path="data/gutenberg.csv"):
    """
    Load the TidyTuesday Gutenberg dataset.
    Returns a pandas DataFrame.
    """
    return pd.read_csv(path)

def clean_aliases(df, alias_col="alias"):
    """
    Keep only non-empty, non-NA aliases.
    """
    return df[df[alias_col].notna()][alias_col]


