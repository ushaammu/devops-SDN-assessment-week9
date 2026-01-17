import requests
import json

# Ryu REST API endpoint
url = "http://localhost:8080/stats/flow/1"

# Send GET request
response = requests.get(url)

# Convert JSON response to Python dictionary
data = response.json()

print("Flow Statistics from Ryu Controller:\n")

# Parse and display selected data
for flow in data["1"]:
    print("Priority:", flow["priority"])
    print("Packet Count:", flow["packet_count"])
    print("Byte Count:", flow["byte_count"])
    print("Match Fields:", flow["match"])
    print("-" * 40)


