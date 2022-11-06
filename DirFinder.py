import requests

print("--------------------------")
print("DirFinder V0.0.1")
print("Author: RedNeutron")
print("--------------------------")
print("")
url = input('Target URL: ')
ArWordlist = []
wordlist = open(input('Wordlist: '),'r')
read = wordlist.readlines()
for line in read:
    ArWordlist.append(line.strip())
    a = requests.get(url+'/'+line.strip())
    print(a.status_code, ':', url,'/', line.strip())
# Big respect for Mr Net0
