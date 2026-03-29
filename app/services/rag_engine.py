import json
import os 

DATA_PATH = os.path.join(os.getcwd(), "data", "schemes.json")

def load_schemes():
    with open(DATA_PATH,"r") as f:
        return json.load(f)


def filter_by_state(schemes, state):
    return [
        s for s in schemes
        if s["state"] == state or s["state"] == "All"
    ]

def filter_by_category(schemes, category):
    if not category:
        return schemes

    return [
        s for s in schemes
        if s["category"] == category
    ]


def fetch_relevant_schemes(user_profile):
    schemes = load_schemes()

    state = user_profile.get("state")
    category = user_profile.get("category")

    filtered = filter_by_state(schemes, state)
    filtered = filter_by_category(filtered, category)

    return filtered[:3]  # limit results