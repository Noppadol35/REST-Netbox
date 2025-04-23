import csv
import requests
from dotenv import dotenv_values


NETBOX_URL = dotenv_values(".env")["NETBOX_URL"] + "/api/dcim/interfaces/"

headers = {
    "Authorization": "Token " + dotenv_values(".env")["NETBOX_TOKEN"],
    "Content-Type": "application/json",
    "Accept": "application/json"
}


with open("interface.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        interface_id = row["id"]
        description = row["description"]

        url = f"{NETBOX_URL}/{interface_id}/"
        data = {
            "description": description
        }

        response = requests.patch(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"✅ Updated interface {interface_id} - {row['name']}")
        else:
            print(f"❌ Failed to update {interface_id}: {response.status_code} - {response.text}")
