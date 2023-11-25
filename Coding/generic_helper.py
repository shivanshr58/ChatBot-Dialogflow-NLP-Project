# generic_helper.py

# Helper function to create a string representation from a food dictionary
def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

# Helper function to extract session ID from a session string
def extract_session_id(session_string: str):
    import re
    match = re.search('sessions\/(.*)\/contexts', session_string)
    if match:
        return match.group(1)
