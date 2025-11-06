# authors.py
from .utils import load_authors, clean_aliases

def list_authors(by_languages=False, alias=True, path="data/gutenberg_authors.csv"):
    """
    Return a list of author aliases sorted by translation count.
    
    Parameters
    ----------
    by_languages : bool
        If True, sort aliases by number of translations (descending)
    alias : bool
        Placeholder; always True
    path : str, optional
        Path to the CSV file. Defaults to the relative data path.
        
    Returns
    -------
    list
        List of author aliases
    """
    df = load_authors(path)
    authors = clean_aliases(df)
    
    if by_languages:
        return authors.value_counts().index.tolist()
    else:
        return authors.unique().tolist()






