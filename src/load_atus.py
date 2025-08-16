# src/load_atus.py
from typing import Optional
from pathlib import Path
import pandas as pd


# project root = one level above src/
BASE_DIR = Path(__file__).resolve().parent.parent

def get_data_directory() -> Path:
    """Return the absolute path to the project's data directory."""
    return BASE_DIR / "data"

def load_atus_data(file_path: Path) -> Optional[pd.DataFrame]:
    """Load ATUS data from a tab-delimited file."""
    try:
        return pd.read_csv(file_path, sep="\t", engine="python")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None