# utils.py
import pandas as pd
import os

"""
    Load the Gutenberg authors dataset as a pandas DataFrame.
    Path is relative to the project root.
"""
def load_authors(path=None):
    if path is None:
        path = "data/gutenberg_authors.csv"
    return pd.read_csv(path)

def clean_aliases(df, alias_col="alias"):
    """Return only valid, non-empty aliases."""
    return df[df[alias_col].notna()][alias_col]

