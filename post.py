import requests
import csv
from dotenv import dotenv_values

url = dotenv_values(".env")["NETBOX_URL"] + "/api/ipam/vlans/"

headers = {
    "Authorization": "Token " + dotenv_values(".env")["NETBOX_TOKEN"],
    "Content-Type": "application/json",
    "Accept": "application/json"
}



with open('vlan.csv', mode='r') as file:
    csvfile = csv.DictReader(file)
    
    for row in csvfile:
        data = {
            "name" : row['name'],
            "vid" : int(row['vid']),
            "site" : int(row['site']),
            "status" : row['status'],
        }
        
        response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("✅ VLAN ถูกสร้างเรียบร้อย!")
    print(response.json())
else:
    print("❌ สร้างไม่สำเร็จ:", response.status_code)
    print(response.text)
