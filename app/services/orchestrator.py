import re 

STATE_KEYWORDS = {
    "uttar pradesh": "Uttar Pradesh",
    "bihar": "Bihar",
    "delhi": "Delhi",
    "madhya pradesh": "Madhya Pradesh"
}

OCCUPATION_KEYWORDS = {
    "kisan": "farmer",
    "farmer": "farmer",
    "student": "student",
    "vidyarthi": "student"
}

CATEGORY_MAP = {
    "farmer": "agriculture",
    "student": "education"
}


def normalize_text(text):
    return text.lower().strip()



def extract_state(text):
    for key in STATE_KEYWORDS:
        if key in text:
            return STATE_KEYWORDS[key]
    return None 


def extract_occupation(text):
    for key in OCCUPATION_KEYWORDS:
        if key in text:
            return OCCUPATION_KEYWORDS[key]
    return None


def extract_user_info(text):
    text = normalize_text(text)

    state = extract_state(text)
    occupation = extract_occupation(text)

    category = CATEGORY_MAP.get(occupation)

    return {
        "state": state,
        "occupation": occupation,
        "category": category
    }