test_settings = {
    'Theme': 'dark',
    'Notification':'enabled',
    'Volume': 'high'
}
def add_setting(setting,pair):
    key,value = pair
    key = key.lower()
    value = value.lower()

    if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    setting[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting,pair):
    key,value = pair
    key = key.lower()
    value = value.lower()
    

    if key in setting:
        setting[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(setting, key):
    key = key.lower()

    if key in setting:
        del setting[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(setting):
    if not setting:
        return "No settings available."
    result = "Current User Settings:\n"
    for key, value in setting.items():
        result += f"{key.capitalize()}: {value}\n"
    return result
print(view_settings(test_settings))