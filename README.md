# Multi-Market Research Tool

このツールは、複数のオンラインマーケットプレイス（Yahooショッピング、楽天市場、eBay）から商品を検索し、結果をCSVファイルに保存するPythonスクリプトです。

## 🚀 特徴

*   Yahooショッピング、楽天市場、eBayから商品を検索
*   検索結果をCSVファイルに保存
*   設定ファイルによる柔軟なカスタマイズ
*   並行処理による高速化

---

## 🔧 セットアップ手順

1.  必要なライブラリをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

2.  設定ファイル`config.ini`を作成し、APIキーなどの必要な情報を入力します。`config template.ini`を参考にしてください。

---

## 実行方法

```bash
python main.py
```

## 🐳 Dockerでの実行方法

### ビルド

```bash
docker build -t multi-market-research .
```

### 実行

```bash
docker run -it --rm multi-market-research
```

実行後、検索結果がExcelファイルとして保存されます。

**注意**

実行前に、`config.ini`ファイルを作成し、APIキーなどの必要な情報を入力してください。`config template.ini`を参考にしてください。

## ファイル構成

```
├── .gitignore
├── config.ini             # 設定ファイル
├── config template.ini    # 設定ファイルのテンプレート
├── ebay_search_functions.py   # eBay検索機能
├── main.py                  # メインスクリプト
├── rakuten_search_functions.py # 楽天市場検索機能
├── utils.py                 # ユーティリティ関数
└── yahoo_search_functions.py  # Yahooショッピング検索機能
```

## 📦 依存ライブラリ（requirements.txt）

```
requests
beautifulsoup4
lxml
python-dotenv
```

## 🛡️ 利用

自由に使ってOKですが、自己責任でご利用ください
