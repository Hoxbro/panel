import json
from pathlib import Path


def test_json_files():
    path = Path(__file__).parent.parent
    for json_file in path.rglob("*.json"):
        json.loads(json_file.read_bytes())
