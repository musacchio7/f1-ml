# src/utils/scoring.py

from typing import List
import pandas as pd

# 🎯 Define points system by year
POINTS_SYSTEMS = {
    (1950, 1959): [8, 6, 4, 3, 2],                       # +1 FL not included
    (1960, 1990): [9, 6, 4, 3, 2, 1],
    (1991, 2002): [10, 6, 4, 3, 2, 1],
    (2003, 2009): [10, 8, 6, 5, 4, 3, 2, 1],
    (2010, 2999): [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
}

def get_scoring_system(year: int) -> List[int]:
    """Return the list of points per position for a given year."""
    for (start, end), system in POINTS_SYSTEMS.items():
        if start <= year <= end:
            return system
    raise ValueError(f"No scoring system defined for year {year}")

def normalize_points(df: pd.DataFrame, year_col: str = "year", points_col: str = "points") -> pd.Series:
    """
    Normalize points by year based on the maximum possible points system that year.
    Returns a new Series with normalized values between 0 and 1.
    """
    def get_max_points(year):
        system = get_scoring_system(year)
        return system[0]  # max points for 1st place

    max_points_per_year = df[year_col].apply(get_max_points)
    return df[points_col] / max_points_per_year