# Syllabus Exporter

Syllabus Exporter は、シラバスを JSON ファイルで出力します。

## データ出力

- 取得元
  - [広島市立大学　シラバス公開情報　検索](http://rsw.office.hiroshima-cu.ac.jp/scripts/Syllabussearch/index.php)
- 取得方法
  - 空の POST リクエストを送信し、すべての科目をスクレイピングする
- 取得データ
  - [x] `/public/csv/` 内に `yyyymmddhhmmss.csv` として記録
  - [ ] CSV ファイルを正規化（例: 履修対象学年の英語を日本語に、など）
  - [ ] `/public/ichipiro-syllabus.json` を保存
- 自動化
  - [ ] GitHub Actions が `public` フォルダを自動公開
  - [ ] `ichipro.sasakulab.com/syllabus/` に Cloudflared Pages を通す

## `ichipiro-syllabus.json`

例示: [システム工学実験 Ⅰ(システム工学専攻: 桑田精一先生)](http://rsw.office.hiroshima-cu.ac.jp/OpenSyllabus/2023_28431801.html)

```json
{
  "updated": "2024/01/01",
  "subject": [
    {
      "id": 28341801,
      "year": 2023,
      "subject": "システム工学実験Ⅰ",
      "teacher": "桑田精一", // 代表教員を指す（運用はシラバス検索ページにリストされる担当教員カラムの氏名）
      "role": "准教授",
      "unit": 3,
      "target": ["B3"],
      "require": "必修", // 受講要件
      "semester": "前期",
      "pw": "有",
      "description": "",
      "url": "http://rsw...."
    }
  ]
}
```

なお、[API 側の型定義](https://github.com/ichipro-hcu/ichipro-syllabus-api/blob/main/src/interface/interfaces.ts)が存在し、基本的にそれに準拠する

## License

- すべてのプログラムは MIT LICENSE でライセンスされます
- シラバスデータはライセンス**されません**。すべてのデータに対する権利は[公立大学法人 広島市立大学](https://www.hiroshima-cu.ac.jp/)に帰属します
