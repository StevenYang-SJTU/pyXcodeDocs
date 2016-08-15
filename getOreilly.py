from pandas import DataFrame
import requests

#link ="http://www.oreilly.com/data/free/archive.html"
#link="http://www.oreilly.com/programming/free/"
#link="http://www.oreilly.com/web-platform/free/"
#link="http://www.oreilly.com/iot/free/"
link="http://www.oreilly.com/webops-perf/free/"

file = requests.get(link)
f0 = open('source.txt','w')
f0.write(file.text)
f0.close


names = []
links = []
result = ""
f1 = open('source.txt','r')
filedata = f1.read()
f1.close()
newdata = filedata.replace('href="' ,'\n')
tmpdata = newdata.replace('free/' ,'free/files/')
newerdata = tmpdata.replace('.csp' ,'.mobi\n')
f = open('newer.txt','w')
f.write(newerdata)
f.close()

f3 = open('newer.txt','r')
lines = f3.readlines()
templines=[]
 
for j in range(0, len(lines)):
    templines.append(lines[j].strip())
 
for i in range(0, len(templines)):
    if ".mobi" in templines[i]:
        names.append((templines[i]))
        result += (templines[i]) + "    ,"

df = DataFrame({'Item names': names})
df.to_excel('output.xlsx', sheet_name='sheet1', index=False)




