import json

class Credentials:

    def __init__(self):
        pass

    def __get_credentials(self, id):
        with open('credentials.json', 'r') as file:
            data = json.load(file)
            credentials = data['credentials']
            return credentials[id]

    def get_username(self, id):
        return self.__get_credentials(id)["username"]

    def get_password(self, id):
        return self.__get_credentials(id)["password"]
