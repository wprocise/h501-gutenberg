# utils.py
import pandas as pd
import os

"""
    Load the Gutenberg authors dataset as a pandas DataFrame.
    Path is relative to the project root.
"""
def load_authors(path="data/gutenberg_authors.csv"):
    return pd.read_csv(path)

"""
    Return a Series with only valid (non-empty) aliases.
"""
def clean_aliases(df, alias_col="alias"):
    return df[df[alias_col].notna()][alias_col]

