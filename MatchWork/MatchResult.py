import json

import os


json_path = os.path.dirname(os.path.abspath("JsonSet/combination.json"))
json_file = open(os.path.join(json_path, "combination.json"),encoding='utf-8')
CombinationData = json.load(json_file)

res = {}

print("请输入你的id：")
id = input()
print("请问你需要多少编码小伙伴?")
num= int(input())

partners = CombinationData[id]["partners"]
for i in partners:
    res.update(dict(i))
print(sorted(res, key=lambda x: res[x])[-num:])

