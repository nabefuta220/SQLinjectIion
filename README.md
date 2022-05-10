# SQLinject

このレポジトリは、SQLインジェクションを使った不正ログインの例です。

## 実行環境

- python3
- sqlite3

(いずれも標準でインストールされています。)

## データベースの概要

init.pyによって作られるデータベースは次のとおりです。

- id : int
- user char[10]
- password[40]
