import requests

# Make an API call and check response

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:start:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status.code}")

# Convert the response object to a dictionary
response_dict = r.json()

# Process results
print(response_dict.keys())