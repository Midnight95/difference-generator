import json


def format_json(_dict: dict) -> str:
    """
    Converts a Python dictionary object into a JSON formatted string
    """
    return json.dumps(_dict, indent=4)
