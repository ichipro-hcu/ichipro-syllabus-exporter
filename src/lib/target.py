import re

translateDict = {
    "、": ",",
    "，": ",",
    "・": ",",
    "一": "1",
    "二": "2",
    "三": "3",
    "四": "4",
    "１": "1",
    "２": "2",
    "３": "3",
    "４": "4",
    "(": "（",
    ")": "）",
}


def roleReturn(rawStr: str, res: dict, BaseRole: str, NoneAllTrue: bool = False):
    if "1" in rawStr:
        res[f"{BaseRole}1"] = True
    if "2" in rawStr:
        res[f"{BaseRole}2"] = True
    if "3" in rawStr:
        res[f"{BaseRole}3"] = True
    if "4" in rawStr:
        res[f"{BaseRole}4"] = True
    if "以上" in rawStr or "above" in rawStr:
        pass
    if "以下" in rawStr:
        pass
    if (
        res[f"{BaseRole}1"] == False
        and [f"{BaseRole}2"] == False
        and [f"{BaseRole}3"] == False
        and [f"{BaseRole}4"] == False
    ) and NoneAllTrue:
        res[f"{BaseRole}1"] = True
        res[f"{BaseRole}2"] = True
        res[f"{BaseRole}3"] = True
        res[f"{BaseRole}4"] = True
    return res


def unifyTargetArray(rawStr):
    success = False
    res = {
        "B1": False,
        "B2": False,
        "B3": False,
        "B4": False,
        "M1": False,
        "M2": False,
        "D1": False,
        "D2": False,
        "D3": False,
        "parseError": False,
    }
    description = ""

    # 1. 文字列辞書に沿って置換処理
    rawStr = (
        rawStr.translate(str.maketrans(translateDict))
        .replace("First", "1st")
        .replace("Second", "2nd")
        .replace("Third", "3rd")
        .replace("fourth", "4th")
        .replace("次", "")
        .replace("生", "")
    )

    # 2. "(前期|後期)博士" などの文字列を含むものは 数字を切り取って M1, D1 などに誘導
    # a. 修士
    if "修士" in rawStr:
        res = roleReturn(rawStr, res, "M", True)
        success = True
    # b. 前期
    if "前期" in rawStr:
        res = roleReturn(rawStr, res, "M", True)
        success = True
    # c. 後期
    if "後期" in rawStr:
        res = roleReturn(rawStr, res, "D", True)
        success = True
    # d. 院
    if "院" and not ("前期" in rawStr or "後期" in rawStr):
        res = roleReturn(rawStr, res, "D", True)
        res = roleReturn(rawStr, res, "M", True)
        success = True

    # 3. 特徴が数字のみのものは、パースして B1, B2 のみに直す
    if (
        "1" in rawStr or "2" in rawStr or "3" in rawStr or "4" in rawStr
    ) and success != True:
        res = roleReturn(rawStr, res, "B")
        success = True

    # 4. 1~3 の処理が正常に終了した場合、括弧を抜き出して、備考欄に括弧内のコメントを代入
    if success == True:
        reg = "(?<=（).+?(?=\）)"
        description = re.findall(reg, rawStr)[0]

    # 5. 全てが成功しなければ、parseError フラグを立てて、備考欄に文字列をそのまま代入し、終了。
    if success == False:
        res["parseError"] = True
        description = rawStr

    return res, description
