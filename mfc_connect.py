import requests
import re

url = "http://192.168.2.155/mfc.js" #connect mfc via ethernet cable, in this port
response = requests.get(url)

if response.status_code == 200:
    # Extract `flow_value` using regex
    match = re.search(r"mfc\.flow_value\s*=\s*([\d\.]+);", response.text)
    if match:
        flow_value = float(match.group(1))
        print(f"Flow rate: {flow_value}")
    else:
        print("Flow value not found in the JavaScript file.")
else:
    print(f"Failed to fetch mfc.js, status code: {response.status_code}")
