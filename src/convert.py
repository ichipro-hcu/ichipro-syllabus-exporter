import json
import datetime
import scrap
import csv
from lib import target as t


def generateJSON(path="../public/csv/sample.csv"):
    content = []
    with open(path, encoding="utf8", newline="") as raw:
        rows = csv.reader(raw)
        next(rows)
        for row in rows:
            target, detail = t.unifyTargetArray(rawStr=row[5])
            dict = {
                "id": row[9][-13:-5],
                "year": row[9][-18:-14],
                "subject": row[0],
                "teacher": row[1],
                "role": row[2],
                "unit": row[3],
                "target": target,
                "require": row[4],
                "semester": row[6],
                "pw": row[7],
                "detail": detail,
            }
            content.append(dict)
    return content


if __name__ == "__main__":
    scrapResult = scrap.summarizeSyllabus()
    path = "../public/ichipiro-syllabus.json"
    with open(path, "w") as f:
        json.dump(
            {"date": str(datetime.date.today()), "contents": generateJSON(scrapResult)},
            f,
            indent=2,
            ensure_ascii=False,
        )
