# Syllabus Exporter

Syllabus Exporter は、シラバスを JSON ファイルで出力します。

## データ出力

- 取得元
    - [広島市立大学　シラバス公開情報　検索](http://rsw.office.hiroshima-cu.ac.jp/scripts/Syllabussearch/index.php)
- 取得方法
    - 空の POST リクエストを送信し、すべての科目をスクレイピングする
- 取得データ
    - [ ] `/data` 内に `ichipiro-YYYYMMDD.csv` として記録
    - [ ] CSV ファイルを正規化（例: 履修対象学年の英語を日本語に、など）
    - [ ] ルートフォルダに `ichipiro-syllabus.json` を保存 

## `ichipiro-syllabus.json`

例示: [システム工学実験Ⅰ(システム工学専攻: 桑田精一先生)](http://rsw.office.hiroshima-cu.ac.jp/OpenSyllabus/2023_28431801.html)

```json
{
    "updated": "2024/01/01",
    "subject": [
        {
            "id": 28341801,
            "year": 2023,
            "subject": "システム工学実験Ⅰ",
            "unit": 3.0,
            "mainTeacher": "桑田精一", // 代表教員を指す（運用はシラバス検索ページにリストされる担当教員カラムの氏名）
            "allTeachers": "システム工学専攻 准教授 桑田精一（代表教員）, 准教授 池田徹志，准教授 脇田航，准教授 島和之，准教授 双紙正和，准教授 中山仁史，准教授 福島勝，准教授 村田佳洋，准教授 神尾武司，助教 厚海慶太，助教 川本佳代，助教 小作敏晴，助教 齊藤充行，助教 佐藤康臣，助教 高井博之，助教 高橋雄三，助教 辻勝弘", // 全リスト（運用はシラバス詳細ページの一覧）。シラバス入力者によって入力方式がまちまちすぎるため、正規化は行わない。
            "target": "３年",
            "type": "実験",
            "require": "特になし", // 受講要件
            "cancel": true, // どの履修ページでも、ここは譲らず可否で書いてあるため、正規化
            "exam": "実施しない", // 期末試験実施の有無
            "keyword": "自立移動ロボット，ディジタル，アナログ，プロセス間通信，グラフィカルユーザインタフェース" // 検索用
        }
]
}
```

## License

- `/data`, `` 以外のすべてのプログラムは MIT LICENSE でライセンスされます。
- `/data`