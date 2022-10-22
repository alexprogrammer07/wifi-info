import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')  # Command to get information about all the saved wifi in a device

wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]  # Splits wifi profiles

for wifi in wifis:
    """
    For loop to run through all the stored wifi networks
    """
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]  # Splits username and password

    try:
        print(f'Name: {wifi}, Password: {results}')     #the try block to recieve an exception
    except Exception as e:
        print(f'Name: {wifi}, Password: {e}')       #the except block to hande an exception
