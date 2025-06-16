# yahoo_search_functions.py
import requests
import configparser
import os

YAHOO_CONFIG_FILE = "config.ini"

# YahooアプリケーションIDを読み込むまたは尋ねる
def load_or_ask_yahoo_application_id():
    config = configparser.ConfigParser()

    if os.path.exists(YAHOO_CONFIG_FILE):
        config.read(YAHOO_CONFIG_FILE)
        if "YAHOO" in config and "application_id" in config["YAHOO"]:
            return config["YAHOO"]["application_id"]

    app_id = input("Yahooショッピング アプリケーションIDを入力してください：").strip()
    config["YAHOO"] = {"application_id": app_id}
    with open(YAHOO_CONFIG_FILE, "w") as configfile:
        config.write(configfile)
    print("Yahooショッピング アプリケーションIDをconfig.iniに保存しました。")
    return app_id

# Yahooショッピングで商品検索
def search_yahoo_items(keyword, application_id, hits=30):
    url = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"
    params = {
        "appid": application_id,
        "query": keyword,
        "hits": hits,
        "output": "json"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    items = data.get("hits", [])
    results = []

    for item in items:
        name = item.get("name", "N/A")
        price = item.get("price", 0)
        if isinstance(price, dict):
            price = price.get("_value", 0)
        results.append({
            "商品名": name,
            "価格": price,
            "商品URL": item.get("url", "")
        })

    return results
