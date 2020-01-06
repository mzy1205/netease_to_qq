import json

cookie_json = {}
f = open("cookie_tmp.txt", 'r')
lines = f.readlines()
num = 0
for line in lines:
    lineList = line.split()
    cookie_json[lineList[0]] = lineList[1]
    num += 1

f.close()
fw = open('cookie_json.py', 'w')
fw.write('cookies = ' + json.dumps(cookie_json))