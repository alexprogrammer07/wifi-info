import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')  # Command to get information about all the saved wifi in a device

wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]  # Split the name and passwords

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]

    try:
        print(f'Name: {wifi}, Password: {results}')
    except Exception as e:
        print(f'Name: {wifi}, Password: {e}')