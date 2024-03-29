import json

def get_credentials():
    username = input('Type username: ')
    password = input('Type password: ')
    return username, password

def authenticate(username, password, pwdb):
    auth = False
    if username in pwdb:
        if password == pwdb[username]:
            print('Authentication successful!')
            auth = True
        else:
            print('Wrong password!')
    else:
        print('User not known!')
    return auth

def add_user(username, password, pwdb):
    """This is how you comment a function"""
    pwdb[username] = password

def write_pwdb(pwdb):
    #when with context is exited, the file is written and closed
    with open('pwdb.json', 'wt') as pwdb_file:
        json.dump(pwdb, pwdb_file)
    print('Pwdb written')

def read_pwdb():
    with open('pwdb.json', 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb

username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)
