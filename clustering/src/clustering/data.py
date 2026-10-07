from pathlib import Path
import pandas as pd


def load_data(path: str | Path) -> pd.DataFrame:
    """Load the Pokémon dataset from a CSV file."""
    return pd.read_csv(path)