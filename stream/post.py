import requests

res = requests.post('http://localhost/analyzer/store', data = {'tmp' : '1111' })
print res.status_code
print res.text
