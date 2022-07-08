
from utilities.credentials import Credentials

username = Credentials().get_username(0)
password = Credentials().get_password(0)

print(password)