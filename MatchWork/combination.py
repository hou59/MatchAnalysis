import json
import os

def count(a):
    re=0
    for i in a:
        re=re+i
    return re
json_path = os.path.dirname(os.path.abspath("JsonSet/grade.json"))
json_file = open(os.path.join(json_path, "grade.json"))
GradeData = json.load(json_file)
Res = {}

for key1 in GradeData:
    res1 = []
    gradedata1 = GradeData[key1]
    for key2 in GradeData:
        res2 = []
        gradedata2 = GradeData[key2]
        for i in range(len(gradedata1)):
            temp = gradedata1[i] - gradedata2[i]
            res2.append(temp if temp > 0 else -1 * temp)
        ComprehensiveScore = {key2: count(res2)}
        res1.append(ComprehensiveScore)
    Res[key1] = {"partners": res1}

NewjsonFile = json.dumps(Res, indent=4, ensure_ascii=False)

with open("JsonSet"+"/"+"combination.json", 'w', encoding='utf-8') as json_file:
    json_file.write(NewjsonFile)