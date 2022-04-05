import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data = meta_data.decode('utf-8', errors = 'backslashreplace')
data = data.split('\n')

print(data)