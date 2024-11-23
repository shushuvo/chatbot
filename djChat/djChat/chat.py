from django.http import HttpResponse
import os
import json
from difflib import get_close_matches

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'x.json')

try:
    with open(file_path, 'r') as file:
        content = json.load(file)
except FileNotFoundError as e:
    print(f"Error: {e}")
    content = {}

def reply(message):
    message = message.lower()
    # Find keys in content that match the message with 70% similarity or more
    matches = get_close_matches(message, content.keys(), n=1, cutoff=0.7)
    if matches:
        # Return the first best match
        return HttpResponse(content[matches[0]])
    else:
        return HttpResponse("No suitable response found")
