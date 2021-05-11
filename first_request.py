import urllib.request

url = "https://google.com"

data = urllib.request.urlopen(url)
print(data)
print(data.read())
