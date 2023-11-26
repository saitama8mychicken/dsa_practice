"""

"""
import json

with open("response.json", "r") as fp:
    json_data = json.load(fp)

# Parse the JSON data
data = json_data

# Create a dictionary to group users
grouped_users = {}

# Iterate over each user in the JSON data
for user_id, user_data in data.items():
    # Convert the user data to a JSON string to use it as the grouping key
    json_string = json.dumps(user_data)

    # Check if the JSON string already exists as a key in the grouped_users dictionary
    if json_string in grouped_users:
        # Append the user ID to the existing list of users with the same JSON value
        grouped_users[json_string].append(user_id)
    else:
        # Create a new list with the current user ID as the first element
        grouped_users[json_string] = [user_id]

# Print the grouped users
for json_string, user_ids in grouped_users.items():
    print(f"Users with JSON value {json_string}: {user_ids}")
