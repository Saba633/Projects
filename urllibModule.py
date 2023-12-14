import urllib.request
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))

try:
    url = 'https://www.google.com/search?q=test'
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML Like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=header)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('Urllib_File.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print("Error : ", str(e))
