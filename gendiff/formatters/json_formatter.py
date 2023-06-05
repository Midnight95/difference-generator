import json


def format_json(diff: dict) -> str:
    """
    Converts a Python dictionary object into a JSON formatted string
    """
    return json.dumps(diff, indent=4)
