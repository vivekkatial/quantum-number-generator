import requests
import json

API_URL = "https://qrng.anu.edu.au/API/jsonI.php?length=10&type=uint8"

def main():
    print("Connecting to Quantum Device ....")
    r = requests.get(API_URL)
    print("Connected and randomness generated between 1-255")
    raw_json = r.json()
    data = raw_json["data"]
    print(json.dumps(data, indent=4))
    

if __name__ == "__main__":
    main()