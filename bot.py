import urllib, json

print"\033[94m Chat Tools buat jomblo :p"
print"\033[94m Coded by Mr.Rm19"
print"\033[94m 008 ~ c4uR ~ Mrs.4ul14 ~ ./Serizawa"
while(True):
    pesan = raw_input("Kamu: ")
    url = "http://sandbox.api.simsimi.com/request.p?key=a2cfd850-5044-4614-9594-e0700b9a3c23&lc=id&ft=1.0&text=%s" % pesan
    link_json = urllib.urlopen(url)
    data = json.loads(link_json.read())

    print"\033[92m Bot: %s" % data['response']
