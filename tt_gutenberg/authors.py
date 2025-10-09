# tt_gutenberg/authors.py
from utils import load_data, clean_alias_data

def list_aliases_by_translation_count(csv_path: str) -> list: 
    """
    Return a list of author aliases ordered by translation count (descending).
    """
    df = load_data(csv_path)
    df = clean_alias_data(df)

    if 'n_translated' not in df.columns or 'alias' not in df.columns:
        raise ValueError("Dataset must contain 'alias' and 'n_translated' columns")

    sorted_aliases = (
        df.sort_values('n_translated', ascending=False)['alias'].tolist()
    )

    return sorted_aliases



