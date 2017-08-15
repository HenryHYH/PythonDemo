import requests

# req = requests.get("https://unsplash.com")
# print(req.text)

payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/'

req = requests.get(url + 'get', params=payload)
print(req.text)

req = requests.post(url + 'post', data=payload)
print(req.text)

req = requests.put(url + 'put')
print(req.text)

req = requests.delete(url + 'delete')
print(req.text)

req = requests.head(url + 'get')
print(req.text)

req = requests.options(url + 'get')
print(req.raw)
