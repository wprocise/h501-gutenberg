# authors.py
from .utils import load_authors, clean_aliases

def list_authors(by_languages=False, alias=True, path="data/gutenberg_authors.csv"):
    
    df = load_authors(path)
    authors = clean_aliases(df)

    if by_languages:
        return authors.value_counts().index.tolist()
    else:
        return authors.unique().tolist()