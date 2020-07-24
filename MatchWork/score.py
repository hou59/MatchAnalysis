import json

def count(a):
    count=0
    for i in a:
        count=count+1
    return count

FileScore = open('test_data.json', encoding='utf-8')

TestData = json.loads(FileScore.read())
Filetime = open('testTime.json', encoding='utf-8')

Testtime = json.loads(Filetime.read())
Usuerscore = {}
for key in TestData:
    cases = TestData[key]['cases']
    user_id = str(TestData[key]['user_id'])
    if key not in Testtime:
        tt={}
    else:
        tt=Testtime[key]
    Cases = []
    print(user_id)
    print(cases)
    for case in cases:
        judge=True
        for i in tt:
            if i['case_id']==case['case_id']:
                judge=False
                Case = {"case_id": case["case_id"],
                        "case_type": str(case["case_type"]),
                        "score": case["final_score"],
                        "UploadNum": count(case["upload_records"]),
                        "Testtime":i['time']}
                Cases.append(Case)
                break
        if judge:
            Case = {"case_id": case["case_id"],
                    "case_type": str(case["case_type"]),
                    "score": case["final_score"],
                    "UploadNum": count(case["upload_records"]),
                    "Testtime": 0}
            Cases.append(Case)

    if len(Cases) != 0:
        Usuerscore[user_id] = {"cases": Cases}

NewjsonFile = json.dumps(Usuerscore, indent=4, ensure_ascii=False)

with open("JsonSet"+"/"+"score.json", 'w', encoding='utf-8') as json_file:
    json_file.write(NewjsonFile)
