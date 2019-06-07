from bs4 import BeautifulSoup
import re
import requests
html_url="http://121.42.201.251/se/?switch=7"
params=[]
for i in list(range(1,37)):
    params.append({"sub":i})
 
with open('f:exercise.txt','w',encoding='utf-8') as f:
    for param in params:
        response= requests.get(html_url,param)

        soup=BeautifulSoup(response.text,"html.parser")
        s=soup.find(id="content")
        f.write(s.text)
        print("finish download ",response.url)