import json
import os


json_path = os.path.dirname(os.path.abspath("JsonSet/score.json"))
json_file = open(os.path.join(json_path, "score.json"),encoding='utf-8')
FileData = json.load(json_file)

Cases = []
Sample = {}

for key in FileData:
    cases = FileData[key]['cases']

    for case in cases:
        if case['case_id'] not in Cases:
            Cases.append(case['case_id'])

for i in range(0, len(Cases)):
    Sample[Cases[i]] = 0

NewjsonFile = json.dumps(Sample, indent=4, ensure_ascii=False)

with open("JsonSet"+"/"+"sample.json", 'w', encoding='utf-8') as json_file:
    json_file.write(NewjsonFile)