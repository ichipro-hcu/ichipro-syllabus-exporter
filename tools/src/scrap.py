import requests
import urllib
from bs4 import BeautifulSoup
import argparse
import csv
import datetime

baseDomain = "http://rsw.office.hiroshima-cu.ac.jp"
now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def __init__():
    pass

def summarizeSyllabus():
    response = requestSyllabusList()
    tableArray = convertSyllabusList(response)
    createCSVFile(tableArray)

def requestSyllabusList():
    url = "/scripts/Syllabussearch/sel.php"
    data = {
        "fcl_cd": "@",
        "sbj_ast_cd": "@",
        "trm_cd": "@",
        "grd_cd": "@",
        "jitsumu_cd": "@",
        "sbj_name": "",
        "tch_name": ""
        }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url = baseDomain + url, data = urllib.parse.urlencode(data), headers=headers)
    if response.status_code != 200:
        raise ValueError('System Failure on rsw.office.hiroshima-cu.ac.jp')
    if response.text == "":
        raise ValueError('Response from rsw.office.hiroshima-cu.ac.jp is empty')
    return response
    
def convertSyllabusList(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.findAll("tr")[1:]
    tableArray = []
    for row in rows:
        soup2 = BeautifulSoup(str(row), 'html.parser')
        scrapRow = soup2.findAll("td")
        rowArray = []
        for column in scrapRow:
            rowArray.append(column.getText().replace('　', ' '))
        scrapAnchor = soup2.find("a")
        href = scrapAnchor.get("href")
        rowArray.append(href)
        tableArray.append(rowArray[1:])
    return tableArray

def createCSVFile(tableArray, outputPath = "./csv/" + now + ".csv"):
    subjectrow = [
        "授業科目名",
        "担当教員",
        "役職",
        "単位数",
        "必修・選択・自由",
        "開講年次",
        "開講学期",
        "実務経験",
        "備考",
        "シラバスURL"
    ]
    try:
        with open(outputPath, "w") as f:
            writer = csv.writer(f)
            writer.writerow(subjectrow)
            writer.writerows(tableArray)
    except Exception as e:
        raise ValueError(f"File Creation Error - {e}")
    
if __name__ == "__main__":
    res = summarizeSyllabus()