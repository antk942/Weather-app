# get gps coordinates from geopy
import json

# import urlopen from urllib.request
from urllib.request import urlopen


def get_data_from_file(file_name):
    # Open the JSON file for reading
    with open(file_name, 'r') as f:
        # Load the JSON data into a list of dictionaries
        data = json.load(f)
    f.close()
    return data


def get_coordinatess():
    # open following url to get ipaddress
    urlopen("http://ipinfo.io/json")

    # load data into array
    data = json.load(urlopen("http://ipinfo.io/json"))

    return f"lat={data['loc'].split(',')[0]}&lon={data['loc'].split(',')[1]}"


def get_user_preference(file_name: str) -> str:
    option_data = get_data_from_file(file_name)
    print('Choose one of the options:')
    for option_name in option_data:
        print(option_name)

    chosen_option = get_chosen_option(option_data)

    if chosen_option == "default":
        if file_name == "Languages.json":
            return "en"
        else:
            return "metric"
    else:
        return chosen_option


def get_chosen_option(option_data: dict) -> str:
    while True:
        user_input = input("Enter your preference or press 0 to default: ")
        if user_input in option_data:
            return option_data[user_input]
        elif user_input == "0":
            return "default"
        else:
            print("Try one of the options.\n")
