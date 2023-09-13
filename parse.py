import json
import pandas as pd

def flatten_dict(dictionary, separator='_'):
    items = []
    stack = [((), dictionary)]

    while stack:
        parent_key, current_dict = stack.pop()
        for key, value in current_dict.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            if isinstance(value, dict):
                stack.append((new_key, value))
            else:
                items.append((new_key, value))
    
    return dict(items)

with open('./sample-username-query.json', 'r') as json_username:
    username_dict = json.load(json_username)
    print(flatten_dict(username_dict))
