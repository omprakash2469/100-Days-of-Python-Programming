import requests

url = "https://codinglifes.com"
res = requests.get(url)

print(res.status_code) # Returns status code
print(res.ok) # Returns status
print(res.text) # Returns text