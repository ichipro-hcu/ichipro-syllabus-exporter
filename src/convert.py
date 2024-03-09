import scrap
import csv

scrapResult = scrap.summarizeSyllabus()


def unifyTargetArray(rawStr):
    res = []
    return res


def generateJSON(strpath):
    content = []
    with open(strpath, encoding="utf8", newline="") as raw:
        rows = csv.reader(raw)
        for row in rows[1:]:
            res = unifyTargetArray()
            dict = {
                "id": row[9][-13:-6],
                "year": row[9][-18:-15],
                "subject": row[0],
                "teacher": row[1],
                "role": row[2],
                "unit": row[3],
                "target": ["B1", "B2"],
                "require": row[4],
                "semester": row[6],
                "pw": row[7],
                "detail": row[9],
            }
            content.append(dict)
    return content
