from urllib.request import urlopen, Request
import re
import json

url = "https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&format=json&page=Mount_Tambora"

req = Request(
    url,
    headers={
        "User-Agent": "QuickStartGuides/1.0 (support@quickstartguides.com)"
    }
)

# Request the page
response = urlopen(req)

# Properly decode the bytes
data = response.read().decode("utf-8")

# Parse the JSON
json_data = json.loads(data)

# Extract only the wikitext
wikitext = json_data["parse"]["wikitext"]["*"]

# Regex to find elevation in wikitext
regex = r"elevation_m\s*=\s*(\d+)"

match = re.search(regex, wikitext)

if match:
    elevation = match.group(1)
    print("The elevation of Mt. Tambora is " + elevation + ".")
else:
    print("Elevation not found.")
