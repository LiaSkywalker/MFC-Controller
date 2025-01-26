import requests
import re

def find_flow_rate():
    # Extract `flow_value` using regex
    match = re.search(r"mfc\.flow_value\s*=\s*([\d\.]+);", response.text)
    if match:
        flow_value = float(match.group(1))
        print(f"Flow rate: {flow_value}")
    else:
        print("Flow value not found in the JavaScript file.")

def find_pressure_value():
    # Extract `pressure_value` using regex
    match = re.search(r"mfc\.pressure_value\s*=\s*([\d\.]+);", response.text)
    if match:
        pressure_value = float(match.group(1))
        print(f"pressure value: {pressure_value}")
        print(f"pressure value in mbar: {pressure_value/1.333}")
    else:
        print("pressure value not found in the JavaScript file.")

if __name__ == '__main__':
    url = "http://192.168.2.155/mfc.js"
    response = requests.get(url)

    if response.status_code == 200:
        find_flow_rate()
        find_pressure_value()
    else:
        print(f"Failed to fetch mfc.js, status code: {response.status_code}")
