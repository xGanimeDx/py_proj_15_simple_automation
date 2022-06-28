import json

class Credentials:

    def __init__(self, id):
        self.id = id

    def __get_credentials(self):
        with open('credentials.json', 'r') as file:
            data = json.load(file)
            credentials = data['credentials']
            return credentials[self.id]

    def get_username(self):
        return self.__get_credentials()["username"]

    def get_password(self):
        return self.__get_credentials()["password"]




