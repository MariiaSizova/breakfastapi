import sqlite3
import json
from typing import Union

DB: str = "db/recipes.db"


def fetch_random_recipe() -> dict:
    """
    Returns a recipe dict.
    """
    with sqlite3.connect(DB, check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items ORDER BY RANDOM() LIMIT 1")
        data = cursor.fetchone()
        return {
            "id": data[0],
            "name": normalize_string(data[1]),
            "total_duration": data[2],
            "ingredients": json.loads(
                data[3].replace("'", '"')
            ),  # convert string list to python list
            "directions": data[4],
        }


def fetch_recipe_by_id(id: int) -> Union[dict, None]:
    """
    Returns a single recipe dict or None if id not found
    """
    with sqlite3.connect(DB, check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id = ?", (id,))
        data = cursor.fetchone()
        if data is not None:
            return {
                "id": data[0],
                "name": normalize_string(data[1]),
                "total_duration": data[2],
                "ingredients": json.loads(
                    data[3].replace("'", '"')
                ),  # convert string list to python list
                "directions": data[4],
            }
        else:
            return None


def normalize_string(s: str) -> str:
    """
    function to normalize strings by removing extra quotes and trailing spaces
    """
    if s.startswith("'") and s.endswith("'"):
        return s.replace("'", "", 2).rstrip("'").strip()
    return s.rstrip()
