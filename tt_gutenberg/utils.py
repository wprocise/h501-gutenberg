# utils.py
import pandas as pd

def load_authors(path="data/gutenberg_authors.csv"):
    """
    Load the Gutenberg authors dataset as a pandas DataFrame.
    Path is relative to the package data folder.
    """
    return pd.read_csv(path)

def clean_aliases(df, alias_col="alias"):
    """
    Return a Series with only valid (non-empty) aliases.
    """
    return df[df[alias_col].notna()][alias_col]
