import urllib.request
import json

# Google Cloud's public Pi Delivery API (fetching 100,000 digits)
url = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=100000"

print("Fetching 100,000 digits of Pi...")

try:
    # Ping the API and decode the JSON response
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    
    # Extract just the raw string of numbers (no decimals)
    pi_digits = data['content']
    
    # Generate the text file
    with open("pi.txt", "w") as file:
        file.write(pi_digits)
        
    print("Success! pi.txt has been generated in your folder.")

except Exception as e:
    print(f"Failed to fetch: {e}")
