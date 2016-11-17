import requests

f = open('out.txt')
while True:
	line = f.readline()
	if not line :
		break
	print line
	res =  requests.post('http://localhost/analyzer/store', data = {'tmp' : line })
