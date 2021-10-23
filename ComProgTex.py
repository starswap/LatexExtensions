import sys
import json
import requests
import bs4 #Beautiful soup - html parser library

service = sys.argv[1]
username = sys.argv[2]

if service == "UVa Online Judge":
        uID = requests.get("https://uhunt.onlinejudge.org/api/uname2uid/" + username).text
        problems = requests.get("https://uhunt.onlinejudge.org/api/ranklist/"+uID+"/0/0").json()[0]["ac"]
        with open(service+username+".tex","w") as f:
                f.write("\\textbf{"+service+"}: Solved \href{"+"https://uhunt.onlinejudge.org/id/"+uID+"}{"+str(problems)+" problems}.") 
elif service == "Kattis":
        usernameS = username.lower()
        usernameS = usernameS.replace(" ","-")
        soup = bs4.BeautifulSoup(requests.get("https://open.kattis.com/users/"+usernameS).text)
        divs = soup.find_all("div",class_="rank clearfix")
        rank = int(divs[0].findChildren()[-2].text)
        points = float(divs[0].findChildren()[-1].text)
        with open(service+username+".tex","w") as f:        
                f.write("\\textbf{"+service+"}: Ranked \href{"+"https://open.kattis.com/users/"+usernameS+"}{"+str(rank)+"} with "+str(points)+" points.")         
