import os
from datetime import datetime
from rakuten_search_functions import load_or_ask_rakuten_application_id, search_rakuten_items
from ebay_search_functions import search_ebay_items
from yahoo_search_functions import load_or_ask_yahoo_application_id, search_yahoo_items
from utils import (
    load_or_ask_exchangerate_api_key,
    get_usd_to_jpy_rate,
    extract_price_info,
    save_comparison_to_excel,
    save_all_results_to_excel,
)

if __name__ == "__main__":
    try:
        keyword = input("🔍 検索キーワードを入力してください: ").strip()
        if not keyword:
            raise ValueError("検索キーワードが空です。")

        exchange_api_key = load_or_ask_exchangerate_api_key()
        exchange_rate = get_usd_to_jpy_rate(exchange_api_key)

        # 楽天検索
        rakuten_app_id = load_or_ask_rakuten_application_id()
        rakuten_items = search_rakuten_items(keyword, rakuten_app_id)
        rakuten_info = extract_price_info(rakuten_items, name_key="商品名", price_key="価格", url_key="商品URL")

        # eBay検索
        ebay_items_raw = search_ebay_items(query=keyword, limit=20)
        ebay_items = []
        for item in ebay_items_raw:
            if item.get("price"):
                try:
                    price_jpy = float(item['price']['value']) * exchange_rate
                    ebay_items.append({
                        "商品名": item.get("title", "N/A"),
                        "価格": round(price_jpy, 2),
                        "商品URL": item.get("itemWebUrl", "")
                    })
                except:
                    continue
        ebay_info = extract_price_info(ebay_items, name_key="商品名", price_key="価格", url_key="商品URL")

        # Yahoo検索
        yahoo_app_id = load_or_ask_yahoo_application_id()
        yahoo_items = search_yahoo_items(keyword, yahoo_app_id)
        yahoo_info = extract_price_info(yahoo_items, name_key="商品名", price_key="価格", url_key="商品URL")

        # 結果保存
        today_str = datetime.today().strftime("%Y%m%d")
        output_filename = f"search_results_{today_str}.xlsx"

        save_comparison_to_excel(output_filename, exchange_rate, rakuten_info, ebay_info, yahoo_info)
        save_all_results_to_excel(output_filename, rakuten_items, ebay_items, yahoo_items)

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
