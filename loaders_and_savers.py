import json

def _load_json(path):
    with open(path, 'r') as f:
        return json.load(f)