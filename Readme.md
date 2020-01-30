# DiarySummarizer

## 概要

- 指定されたディレクトリ配下に存在するテキストファイルのサマリを発行

## 使い方

- SimDiaryが存在するディレクトリに移動 (or ソース指定ディレクトリ)
- diarySummarizer.exe を実行 (or diarySummarizer.py を実行)
- Mydiaryにサマリが発行されていることを確認 (or サマリ出力指定ディレクトリ)

## その他

- 以下のようなディレクトリ構造による入力に対応

```txt
SimDiary
├── 2010
│   ├── 3
│   │   ├── 25.txt
│   │   ├── 26.txt
│   │   └── 29.txt
│   └── 4
│       ├── 1.txt
│       └── 3.txt
└── 2011
    ├── 1
    │   └── 5.txt
    └── 2
        ├── 14.txt
        └── 3.txt

```

- サマリは以下のように発行される

```txt
MyDiary
├── 201003.txt
├── 201004.txt
├── 201101.txt
└── 201102.txt
```

- pythonはじめてだったけど結構いい
