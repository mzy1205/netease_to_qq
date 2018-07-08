import json

cookie_json = {}
f = open("cookie_tmp.txt", 'r')
lines = f.readlines()
num = 0
for line in lines:
    lineArr = line.split()
    cookie_json[str(num)] = {"name": lineArr[0], "value": lineArr[1]}
    num += 1

# print(cookie_json)
f.close()
fw = open('cookie_json.py', 'w')
fw.write('cookie = ' + json.dumps(cookie_json))