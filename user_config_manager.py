test_settings = {
    'Theme': 'Dark',
    'Brightness': 'High'
}

#1st param = dictionary to inspect
#2nd param = tuple ('key', 'value') to add/update settings dictionary, key and value extracted from tuple inside the function.

def add_setting(dictionary, input_tuple):

    #Extract key and value from input tuple
    key, value = input_tuple

    #Convert key and value to lower case
    key = key.lower()
    value = value.lower()

    #Iterate through the existing keys in the dictionary to check it doesn't already exist
    for dict_key in dictionary:
        if key == dict_key.lower():
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."
        else:
            dictionary[key] = value
            return f"Setting '{key}' added with value '{value}' successfully!"

#Same concept as add_setting but 'switched around'

def update_setting(dictionary, input_tuple):

    #Extraction of key,value from input tuple
    key, value = input_tuple

    #Conversion to lower case
    key = key.lower()
    value = value.lower()

    #Iteration through the existing keys in the dictionary
    for dict_key in dictionary:
        if key == dict_key.lower():
            dictionary[dict_key] = value
            return f"Setting '{key}' updated to '{value}' successfully!"
    
    #return not included inside 'else' in order for the function to wait untill all existing keys have been checked before determining if a key exists or not
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, key):
    #as we are deleting a key, the entire tuple isn't necessary, just the key
    #Convert key to lower case
    key = key.lower()

    #Iteration through the existing keys in the dictionary
    for dict_key in dictionary:
        if key == dict_key.lower():
            dictionary.pop(dict_key)
            return f"Setting '{key}' deleted successfully!"
    
    #return not included inside 'else' in order for the function to wait untill all existing keys have been checked before determining if a key exists or not
    return "Setting not found!"

def view_settings(dictionary):
    
    if len(dictionary) == 0:
        return "No settings available."
    #Use a for loop to iterate through each key-value pair and add it to the string
    settings_string = "Current User Settings:\n"
    for key, value in dictionary.items():
        settings_string += f"{key.capitalize()}: {value}\n"
    
    return settings_string
