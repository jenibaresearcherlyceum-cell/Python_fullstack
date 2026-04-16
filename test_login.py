import urllib.request
import json

url = "http://localhost:5000/login"
data = json.dumps({"username": "admin", "password": "admin"}).encode("utf-8")
headers = {"Content-Type": "application/json"}

req = urllib.request.Request(url, data=data, headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as response:
        print("Status:", response.status)
        print("Body:", response.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)
    if hasattr(e, 'read'):
        print("Error Body:", e.read().decode("utf-8"))
