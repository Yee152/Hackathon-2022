import requests
import pandas as pd
import openpyxl



#---COFFEE




#---DAIRY
cookies = {
    'visid_incap_1610353': 'h8dtO0bjQ7mEd7icuAm+QPJZQmMAAAAAQUIPAAAAAADSu5DwRS97Eh0w5OspBuQr',
    'nlbi_1610353': '9cvdIzb4ZHdURYJM6eNT2gAAAAB+POpjf5c+8Soul8QpdWle',
    'incap_ses_975_1610353': 'bQpbaWNckGlUooeMFOaHDfJZQmMAAAAAgvcCp9bfs5gFeZg72pk8mQ==',
    'ECommBanner': 'safeway',
    'abs_gsession': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
    'abs_previouslogin': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
    'SWY_SYND_USER_INFO': '%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D',
    'ECommSignInCount': '0',
    'at_check': 'true',
    'AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg': '1',
    'AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg': '-1124106680%7CMCIDTS%7C19275%7CMCMID%7C15951149247750483002893438902019755800%7CMCAAMLH-1665897589%7C9%7CMCAAMB-1665897589%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1665299989s%7CNONE%7CvVersion%7C5.2.0',
    'SAFEWAY_MODAL_LINK': '',
    'SWY_SHARED_SESSION_INFO': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D',
    'safeway_ga': 'GA1.2.426082052.1665292791',
    'safeway_ga_gid': 'GA1.2.1855502724.1665292791',
    's_vncm': '1667285999728%26vn%3D1',
    's_ivc': 'true',
    'reese84': '3:ltp5ejKfKEiggjXhZgejqw==:KfgNZDxlqE8ucUJbGF4/un2ticSx9RNsmzEGLKK+tUBrLk5BbU4TYZrB/jAr7nw08j8sfLD88MYu4+Ej++HkO8wH1WPPpvz2dD0XrH/anQWHx4LwQ0j0FXCBcqM8tqZEr01U1/OcTa03j9EfaeapgJX2Xqlvwin5hBtC77aeuqnNSfoGf8d9SlWJ26BS+scGodMHOZ8cQUO3baZ5UXAnKtjeUzsOCOVJTxCS4i1yEjDaqduxpHNJ3aASmqAgEERviEOxX6R+vKmglwxrj8f73dIiYYEzJGEzN3u8u7NMrMp9q/fAOKaR1ImWx9xheOzuYBJ+RVzTzbr2HT4rOuDwXCc9TzXGHppdyYAB2BBv9VbMluuZsWj9gqoysriVGLIBzs8ecFvCdyvWyFuq09GE9K6M+xEK+wCFBU9pd/t6JkxkSfVICR+57pEGRITZtX2sURPdIMQeKTMsHKqyxozc0dHwKoWlvSp3FHORKrBhfvVtew5dsw1w6EAbvIaM4uxHx2EWmn47nzXsn0bofBf+dw==:3lWcVFK4CHwuICpLiwLrr3YFHwNf1ilCIUnsg2Sgw/g=',
    's_cc': 'true',
    '_gcl_au': '1.1.13599361.1665292791',
    '_fbp': 'fb.1.1665292795914.888364532',
    'aam_uuid': '20554257657809015762486872184023500220',
    '_pin_unauth': 'dWlkPU5ETmpPVE0xTURBdE9ETmpOUzAwTVRoa0xXRmlNbUV0WXpFM05XWXdOemhsT0RBdw',
    '_clck': 'd7cji9|1|f5k|0',
    '_gid': 'GA1.2.1150958274.1665292803',
    '_gat_gtag_UA_172784514_2': '1',
    '_ga_LZL2CD3SX2': 'GS1.1.1665292802.1.0.1665293162.0.0.0',
    '_ga': 'GA1.1.426082052.1665292791',
    's_nr30': '1665293172184-New',
    'gpv_Page': 'safeway%3Adelivery%3Aaisles%3Adairy-eggs-cheese%3Amilk-cream',
    '_uetsid': '030d43d0479211edb3da1182b9205ed2',
    '_uetvid': '030d6d90479211edb3eb914c2f7acf20',
    's_sq': '%5B%5BB%5D%5D',
    '_br_uid_2': 'uid%3D7415811368740%3Av%3D12.0%3Ats%3D1665292796022%3Ahc%3D18',
    '_derived_epik': 'dj0yJnU9TW9OeFB3TzhJVWhETGVBTXlpU2piVGNScFRTbEp1SW4mbj1MMnNQeWJ4amZvMWRUVnE0LV9KYlJnJm09MSZ0PUFBQUFBR05DVzNZJnJtPTEmcnQ9QUFBQUFHTkNXM1k',
    '_clsk': '1xyxc59|1665293173657|13|1|m.clarity.ms/collect',
    'nlbi_1610353_2147483392': '0VP0V1Fv8jsR4cRN6eNT2gAAAADzwd4kmaFXA9UNi91bTlaR',
    'mbox': 'session#6a87d75100c94c3889029a902a374025#1665295064|PC#6a87d75100c94c3889029a902a374025.35_0#1728538004',
}

headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'visid_incap_1610353=h8dtO0bjQ7mEd7icuAm+QPJZQmMAAAAAQUIPAAAAAADSu5DwRS97Eh0w5OspBuQr; nlbi_1610353=9cvdIzb4ZHdURYJM6eNT2gAAAAB+POpjf5c+8Soul8QpdWle; incap_ses_975_1610353=bQpbaWNckGlUooeMFOaHDfJZQmMAAAAAgvcCp9bfs5gFeZg72pk8mQ==; ECommBanner=safeway; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; ECommSignInCount=0; at_check=true; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19275%7CMCMID%7C15951149247750483002893438902019755800%7CMCAAMLH-1665897589%7C9%7CMCAAMB-1665897589%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1665299989s%7CNONE%7CvVersion%7C5.2.0; SAFEWAY_MODAL_LINK=; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; safeway_ga=GA1.2.426082052.1665292791; safeway_ga_gid=GA1.2.1855502724.1665292791; s_vncm=1667285999728%26vn%3D1; s_ivc=true; reese84=3:ltp5ejKfKEiggjXhZgejqw==:KfgNZDxlqE8ucUJbGF4/un2ticSx9RNsmzEGLKK+tUBrLk5BbU4TYZrB/jAr7nw08j8sfLD88MYu4+Ej++HkO8wH1WPPpvz2dD0XrH/anQWHx4LwQ0j0FXCBcqM8tqZEr01U1/OcTa03j9EfaeapgJX2Xqlvwin5hBtC77aeuqnNSfoGf8d9SlWJ26BS+scGodMHOZ8cQUO3baZ5UXAnKtjeUzsOCOVJTxCS4i1yEjDaqduxpHNJ3aASmqAgEERviEOxX6R+vKmglwxrj8f73dIiYYEzJGEzN3u8u7NMrMp9q/fAOKaR1ImWx9xheOzuYBJ+RVzTzbr2HT4rOuDwXCc9TzXGHppdyYAB2BBv9VbMluuZsWj9gqoysriVGLIBzs8ecFvCdyvWyFuq09GE9K6M+xEK+wCFBU9pd/t6JkxkSfVICR+57pEGRITZtX2sURPdIMQeKTMsHKqyxozc0dHwKoWlvSp3FHORKrBhfvVtew5dsw1w6EAbvIaM4uxHx2EWmn47nzXsn0bofBf+dw==:3lWcVFK4CHwuICpLiwLrr3YFHwNf1ilCIUnsg2Sgw/g=; s_cc=true; _gcl_au=1.1.13599361.1665292791; _fbp=fb.1.1665292795914.888364532; aam_uuid=20554257657809015762486872184023500220; _pin_unauth=dWlkPU5ETmpPVE0xTURBdE9ETmpOUzAwTVRoa0xXRmlNbUV0WXpFM05XWXdOemhsT0RBdw; _clck=d7cji9|1|f5k|0; _gid=GA1.2.1150958274.1665292803; _gat_gtag_UA_172784514_2=1; _ga_LZL2CD3SX2=GS1.1.1665292802.1.0.1665293162.0.0.0; _ga=GA1.1.426082052.1665292791; s_nr30=1665293172184-New; gpv_Page=safeway%3Adelivery%3Aaisles%3Adairy-eggs-cheese%3Amilk-cream; _uetsid=030d43d0479211edb3da1182b9205ed2; _uetvid=030d6d90479211edb3eb914c2f7acf20; s_sq=%5B%5BB%5D%5D; _br_uid_2=uid%3D7415811368740%3Av%3D12.0%3Ats%3D1665292796022%3Ahc%3D18; _derived_epik=dj0yJnU9TW9OeFB3TzhJVWhETGVBTXlpU2piVGNScFRTbEp1SW4mbj1MMnNQeWJ4amZvMWRUVnE0LV9KYlJnJm09MSZ0PUFBQUFBR05DVzNZJnJtPTEmcnQ9QUFBQUFHTkNXM1k; _clsk=1xyxc59|1665293173657|13|1|m.clarity.ms/collect; nlbi_1610353_2147483392=0VP0V1Fv8jsR4cRN6eNT2gAAAADzwd4kmaFXA9UNi91bTlaR; mbox=session#6a87d75100c94c3889029a902a374025#1665295064|PC#6a87d75100c94c3889029a902a374025.35_0#1728538004',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/dairy-eggs-cheese/milk-cream.3132.html?sort=&page=1',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

response = requests.get('https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=3024759218040&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_11_4&storeid=3132&featured=true&search-uid=uid%253D7415811368740%253Av%253D12.0%253Ats%253D1665292796022%253Ahc%253D18&q=&sort=&userid=&featuredsessionid=&screenwidth=987&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway&variant=EOT_1660_true', cookies=cookies, headers=headers)

# check status code
print(response)
    # 200 is correct htp request

# store json file
result_json = response.json()

# find the data
result_items = result_json["response"]["docs"]

price_dairy = []
item_dairy = []

for result in result_items:
    item_dairy.append(result["name"])
    price_dairy.append(result["price"])

# pandas dataframe
safeway_df_beverages = pd.DataFrame({"item": item_dairy, "price": price_dairy})
safeway_df_beverages["category"] = "Dairy"
safeway_df_beverages["store"] = "Safeway"

print(safeway_df_beverages)

