# ebay_search_functions.py
import requests
import base64
import configparser
import os

EBAY_CONFIG_FILE = "config.ini"

def load_or_ask_ebay_credentials():
    config = configparser.ConfigParser()

    if os.path.exists(EBAY_CONFIG_FILE):
        config.read(EBAY_CONFIG_FILE)
        if "EBAY" in config and "client_id" in config["EBAY"] and "client_secret" in config["EBAY"]:
            return config["EBAY"]["client_id"], config["EBAY"]["client_secret"]

    client_id = input("eBay Client IDを入力してください：").strip()
    client_secret = input("eBay Client Secretを入力してください：").strip()

    config["EBAY"] = {
        "client_id": client_id,
        "client_secret": client_secret
    }

    with open(EBAY_CONFIG_FILE, "w") as configfile:
        config.write(configfile)
    print("eBay認証情報をconfig.iniに保存しました。")

    return client_id, client_secret

def get_ebay_production_oauth_token():
    client_id, client_secret = load_or_ask_ebay_credentials()
    url = "https://api.ebay.com/identity/v1/oauth2/token"
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def search_ebay_items(query="", limit=10):
    token = get_ebay_production_oauth_token()
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
    params = {
        "q": query,
        "limit": limit
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("itemSummaries", [])
