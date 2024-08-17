import json

def file(x='a'):
    try:
        with open('userDetail.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        print('File not found, starting with a new file.')
    
    if x == 'a':  # Sign Up
        username = input('Enter username: ')
        password = input('Enter password: ')
        phonenum = input('Enter phone number:')
        if username in data:
            print("Username already exists!")
        else:
            data[username] = {'password': password, 'phonenum': phonenum}
            with open('userDetail.json', 'w') as f:
                json.dump(data, f)
            print("Successfully Signed in!")
    
    elif x == 'r':  # Sign In
        username = input('Enter username: ')
        password = input('Enter password: ')
        if username in data and data[username]['password'] == password:
            print(f'Welcome to the device!')
            print(f'Your phone number is: {data[username]["phonenum"]}')
        else:
            print('Sign in failed, invalid credentials!')

print('1. Sign Up')
print('2. Sign in')
print('3. Exit')

while True:
    a = int(input('Enter your choice: '))
    if a == 1:
        file()
    elif a == 2:
        file(x='r')
    elif a == 3:
        break
    else:
        print('Invalid choice. Please enter 1,2 or 3.')
