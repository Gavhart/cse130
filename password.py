import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = file.read()
        return json.loads(json_data)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON data in {file_path}")
        return None

def get_credentials():
    username = input("Username: ")
    password = input("Password: ")
    return username, password

def authenticate_user(username, password, usernames, passwords):
    try:
        index = usernames.index(username)
        if passwords[index] == password:
            return True
    except ValueError:
        pass
    return False

def main():
    file_path = 'Lab02.json'  
    data_dict = read_json_file(file_path)

    if data_dict:
        usernames = data_dict.get("username", [])
        passwords = data_dict.get("password", [])

        attempts = 3

        while attempts > 0:
            input_username, input_password = get_credentials()

            if authenticate_user(input_username, input_password, usernames, passwords):
                print("You are authenticated!")
                return True
            else:
                print("You are not authorized to use the system.")
                attempts -= 1

        print("Authentication failed. Exiting program.")
        return False

if __name__ == "__main__":
    main()

