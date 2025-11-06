# authors.py
from .utils import load_gutenberg_dataset, clean_aliases

def list_authors(by_languages=False, alias=True, path="data/gutenberg.csv"):
    """
    Return a list of author aliases sorted by translation count.
    """
    df = load_gutenberg_dataset(path)
    
    # Keep only aliases
    authors = clean_aliases(df)
    
    if by_languages:
        # Sort by translation count (descending)
        return authors.value_counts().index.tolist()
    else:
        return authors.unique().tolist()




