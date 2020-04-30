import json
from src.model import Model


def load_use_cases(use_cases_file_path: str):
    with open(use_cases_file_path) as file:
        use_cases_data = json.load(file)
        
    use_cases = {
        key: Model(value) for key, value in use_cases_data.items()
    }

    return use_cases
