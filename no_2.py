import re

regex_user = '(?=.*^[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{5,9}'
username = input("input username:")
print(bool(re.search(regex_user, username)))

regex_pass = '(?=(?:.*[a-z]))(?=.*[$=_]{1})(?=.*[A-Z]{1})(?=.*[0-9]{1})(?=.*[$=_])[a-zA-Z0-9$=_$=_]{8,}'
password = input("input password:")
print(bool(re.search(regex_pass, password)))