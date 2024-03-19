from src.lib import target as t
import pytest

array = [
    "Second year and above",
    "3rd year students",
    "Graduate Students",
    "１・２年次",
    "博士前期課程１、２年",
    "2年次以上",
    "１年（情報科学部・芸術学部対象）",
    "💩",
]

print("> test_target.py")


# Target
def TestPattern0():
    assert t.unifyTargetArray(array[0]) == (
        {
            "B1": False,
            "B2": True,
            "B3": True,
            "B4": True,
            "M1": False,
            "M2": False,
            "D1": False,
            "D2": False,
            "D3": False,
            "parseError": False,
        },
        "",
    )


def TestPattern1():
    assert t.unifyTargetArray(array[1]) == (
        {
            "B1": False,
            "B2": False,
            "B3": True,
            "B4": False,
            "M1": False,
            "M2": False,
            "D1": False,
            "D2": False,
            "D3": False,
            "parseError": False,
        },
        "",
    )


def TestPattern2():
    assert t.unifyTargetArray(array[2]) == (
        {
            "B1": False,
            "B2": False,
            "B3": False,
            "B4": False,
            "M1": True,
            "M2": True,
            "D1": True,
            "D2": True,
            "D3": True,
            "parseError": False,
        },
        "",
    )


def TestPattern3():
    assert t.unifyTargetArray(array[3]) == (
        {
            "B1": True,
            "B2": True,
            "B3": False,
            "B4": False,
            "M1": False,
            "M2": False,
            "D1": False,
            "D2": False,
            "D3": False,
            "parseError": False,
        },
        "",
    )


def TestPattern4():
    assert t.unifyTargetArray(array[4]) == (
        {
            "B1": True,
            "B2": True,
            "B3": False,
            "B4": False,
            "M1": True,
            "M2": True,
            "D1": False,
            "D2": False,
            "D3": False,
            "parseError": False,
        },
        "",
    )


def TestPattern5():
    assert t.unifyTargetArray(array[5]) == (
        {
            "B1": False,
            "B2": True,
            "B3": True,
            "B4": True,
            "M1": False,
            "M2": False,
            "D1": False,
            "D2": False,
            "D3": False,
            "parseError": False,
        },
        "",
    )


def TestPattern6():
    assert t.unifyTargetArray(array[6]) == (
        {
            "B1": True,
            "B2": False,
            "B3": False,
            "B4": False,
            "M1": False,
            "M2": False,
            "D1": False,
            "D2": False,
            "D3": False,
            "parseError": False,
        },
        "情報科学部・芸術学部対象",
    )


def TestPattern7():
    assert t.unifyTargetArray(array[7]) == (
        {
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
        },
        "💩",
    )
