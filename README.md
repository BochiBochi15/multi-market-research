🛒 Multi-Market Research Tool
このツールは、Yahooショッピング・楽天市場・eBay など複数のオンラインマーケットから商品情報を検索・収集し、CSV（Excel）形式で保存するPythonアプリケーションです。商品比較・市場調査・価格分析に活用できます。

🚀 主な特徴
複数マーケット（Yahoo・楽天・eBay）に対応した商品検索(APIを使用)

為替レートAPIを使用した通貨換算

検索結果はCSV形式で出力され、Excelで直接利用可能

Docker対応（環境構築不要で実行可能）

🔧 セットアップ手順
1. 必要ライブラリのインストール
bash
コピーする
編集する
pip install -r requirements.txt
2. APIキーの設定
config.ini をプロジェクトルートに作成し、各APIキーを入力します。config template.ini を参考にしてください。

ini
コピーする
編集する
[RAKUTEN]
application_id = YOUR_RAKUTEN_APP_ID

[EBAY]
client_id = YOUR_EBAY_CLIENT_ID
client_secret = YOUR_EBAY_CLIENT_SECRET

[exchangerate]
exchangerate_api_key = YOUR_EXCHANGERATE_API_KEY

[YAHOO]
application_id = YOUR_YAHOO_APP_ID
🔑 APIキー取得方法（詳細）
🔷 楽天アプリケーションID（Rakuten Application ID）
楽天ウェブサービス にアクセス

楽天会員でログイン（無料アカウント可）

マイページ > アプリIDの発行

表示された「アプリID（applicationId）」を config.ini の [RAKUTEN] セクションに貼り付け

🔷 eBay API（Client ID / Client Secret）
eBay Developers Program にアクセスし、eBayアカウントでログイン

Dashboard にアクセスし「Create an Application」を選択

アプリケーション名を入力して作成

「Production」環境用の Client ID（App ID）と Client Secret を取得し、config.ini の [EBAY] セクションに設定

⚠️ eBay APIではOAuth2認証が必要な場合があるため、APIごとの仕様に注意してください。

🔷 為替レートAPI（ExchangeRate API Key）
https://www.exchangerate-api.com/ にアクセス

無料プランに登録し、APIキーを取得

ダッシュボードに表示されるAPIキーを config.ini の [exchangerate] セクションに記載

🔷 Yahooショッピング API（Application ID）
Yahoo!デベロッパーネットワーク にアクセス

Yahooアカウントでログインし、アプリケーションを新規作成

アプリケーション種別で「ショッピングAPI（商品検索など）」を選択

発行された「アプリケーションID（Client ID）」を config.ini の [YAHOO] セクションに記載

▶️ 実行方法
bash
コピーする
編集する
python main.py
設定ファイルで指定した各条件に基づいて検索が実行されます。

結果はCSVファイルとして保存されます。

🐳 Dockerでの実行方法
ビルド
bash
コピーする
編集する
docker build -t multi-market-research .
実行（設定ファイルをマウント）
bash
コピーする
編集する
docker run -it --rm -v $(pwd)/config.ini:/app/config.ini multi-market-research
📁 ファイル構成
bash
コピーする
編集する
.
├── config.ini                 # 各種APIキーや設定値
├── config template.ini        # テンプレート（サンプル）
├── main.py                    # メイン実行スクリプト
├── yahoo_search_functions.py # Yahooショッピング検索機能
├── rakuten_search_functions.py # 楽天市場検索機能
├── ebay_search_functions.py  # eBay検索機能
├── utils.py                   # 共通関数
├── requirements.txt
└── Dockerfile
📦 必要ライブラリ
nginx
コピーする
編集する
requests  
beautifulsoup4  
lxml  
python-dotenv
⚠️ 注意事項
APIキーは機密情報のため、Gitなどで公開しないでください。

利用は自己責任でお願いします。スクレイピングやAPI利用には各サービスの規約を遵守してください。