import json

# Load the input JSON file containing geometry data
with open('geometry.json', 'r') as file:
    data = json.load(file)

# Function to remove unwanted arrays from the JSON data
# Specifically removes: "ambientOcclusions", "textureCoordinates", and "normals"
def remove_unwanted_arrays(data):
    if isinstance(data, dict):
        return {k: remove_unwanted_arrays(v) for k, v in data.items() 
                if k not in ['ambientOcclusions', 'textureCoordinates', 'normals'] or not isinstance(v, list)}
    elif isinstance(data, list):
        return [remove_unwanted_arrays(item) for item in data]
    else:
        return data

# Step 1: If the "geometries" key exists, clean its contents and save the result
if 'geometries' in data:
    geometries_data = remove_unwanted_arrays(data['geometries'])
    # Save intermediate file without unwanted arrays
    with open('geometry.geometries.json', 'w') as new_file:
        json.dump(geometries_data, new_file, indent=4)

# Load the intermediate file for further filtering
with open('geometry.geometries.json', 'r') as file:
    geometries_data = json.load(file)

# Function to remove dictionary keys that are numeric strings greater than 6
def remove_large_number_keys(data):
    if isinstance(data, dict):
        return {k: remove_large_number_keys(v) for k, v in data.items() if not (k.isdigit() and int(k) > 6)}
    elif isinstance(data, list):
        return [remove_large_number_keys(item) for item in data]
    else:
        return data

# Step 2: Filter the data by removing numeric keys > 6
filtered_geometries = remove_large_number_keys(geometries_data)

# Save the fully processed file
with open('geometry.geometries.filtered.json', 'w') as filtered_file:
    json.dump(filtered_geometries, filtered_file, indent=4)
