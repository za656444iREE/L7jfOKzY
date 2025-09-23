# 代码生成时间: 2025-09-23 20:50:23
import json
def convert_json(input_json_str):    """Converts a JSON string into a Python dictionary.

    Args:
        input_json_str (str): A string representation of a JSON object.

    Returns:
        dict: A Python dictionary representing the JSON object.
        None: If the input string is not a valid JSON.
    """    try:        # Attempt to parse the JSON string into a dictionary        return json.loads(input_json_str)    except json.JSONDecodeError as e:        # Handle JSON decoding errors        print(f"Error decoding JSON: {e}")        return None
def print_json_data(data):    """Prints the JSON data in a readable format.

    Args:
        data (dict): A Python dictionary representing the JSON object.    """    try:        # Attempt to print the JSON data using json.dumps        print(json.dumps(data, indent=4))    except TypeError as e:        # Handle cases where data is not serializable to JSON        print(f"Error printing JSON: {e}")
def main():    # Example JSON string    input_json_str = '{"name": "John", "age": 30, "city": "New York"}'    # Convert JSON string to Python dictionary    json_data = convert_json(input_json_str)    # Check if conversion was successful    if json_data is not None:        # Print the JSON data in a readable format        print_json_data(json_data)    else:        print("Failed to convert JSON string.")if __name__ == "__main__":    main()