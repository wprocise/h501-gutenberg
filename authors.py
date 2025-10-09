# authors.py file
from utils import clean_name 

gutenberg_authors = [
    {"name": "Mark Twain", "alias": "Samuel Clemens", "language": "English"},
    {"name": "J.K. Rowling", "alias": "Robert Galbraith", "language": "English"},
    {"name": "Victor Hugo", "alias": None, "language": "French"},
]

def list_authors(gutenberg_languages=False, alias=False):
    """
    List authors, optionally grouped by language or showing aliases.
    """
    results = []

    for a in gutenberg_authors:
        if alias and a.get("alias"):
            results.append(clean_name(a["alias"]))
        else:
            results.append(clean_name(a["name"]))

    if gutenberg_authors:
        grouped = {}
        for a in gutenberg_authors:
            lang = a["language"]
            grouped.setdefault(lang, []).append(
                clean_name(a["alias"]) if alias and a.get("alias") else clean_name(a["name"])
            )
        return grouped
    
    return results

