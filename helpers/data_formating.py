def jsonify_data(db) -> dict:
    """
    This function jsonify DataBase queries.
    ---
    Args:
        db () :
    Returns:
        payload (dict) : formatted dictionary
    """
    data = db.get_data()
    payload = {'ID': data[0],
               'Recipe Name': data[1],
               'Cook Time (Minutes)': data[2],
               'Ingredients': data[3],
               'Directions': data[4]
               }
    return payload
