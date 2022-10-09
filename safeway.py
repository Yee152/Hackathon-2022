import requests
import pandas as pd
import openpyxl
import json



#---COFFEE
cookies = {
    'visid_incap_1610353': 'h8dtO0bjQ7mEd7icuAm+QPJZQmMAAAAAQUIPAAAAAADSu5DwRS97Eh0w5OspBuQr',
    'nlbi_1610353': '9cvdIzb4ZHdURYJM6eNT2gAAAAB+POpjf5c+8Soul8QpdWle',
    'incap_ses_975_1610353': 'bQpbaWNckGlUooeMFOaHDfJZQmMAAAAAgvcCp9bfs5gFeZg72pk8mQ==',
    'ECommBanner': 'safeway',
    'abs_gsession': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
    'abs_previouslogin': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
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
    's_cc': 'true',
    '_gcl_au': '1.1.13599361.1665292791',
    '_fbp': 'fb.1.1665292795914.888364532',
    'aam_uuid': '20554257657809015762486872184023500220',
    '_pin_unauth': 'dWlkPU5ETmpPVE0xTURBdE9ETmpOUzAwTVRoa0xXRmlNbUV0WXpFM05XWXdOemhsT0RBdw',
    '_clck': 'd7cji9|1|f5k|0',
    '_gid': 'GA1.2.1150958274.1665292803',
    '_ga_LZL2CD3SX2': 'GS1.1.1665292802.1.0.1665293162.0.0.0',
    '_ga': 'GA1.1.426082052.1665292791',
    'reese84': '3:TzbkZ+fio/IGneP3/oNsUg==:PxN54+qAaKtJexsi1OqWvXb+9eBufcAGWJhrERWf+kz+UGtwdRS7kvEWA3xfhjxXWOIvggTX6j8b0haj2OgM9WP/v2RBAlRCBW760/dqEOlGVlHlfYVo+qfsJKQ0k35vYvTyWTpa+SfSux+9HnMOPxA9Scg5+QGd9a6VK3N3Ofrv95aZJz1spStSlzYDuKFk8WENPV++nluf+X9Of4w4C1ygDCtNhz0Tk/89buT9NggiXW85hEKMrKv3G/RjomgnmnJa/EtRd4hTr7LtKOSDyttyosYYY4j+4HkoreHOD1PJ/B8zgrTSP2zZcJD2UB7JnyrHJg3aD1I48GpAg6SaSNZ/mjs3yn5uCSaQiALQdURmntuQCqUe4MimX9XODybPkfCFxe/N/R191vvBBxtGLgcBrXdPyAbfHW4cBEZrSC7iSkX+P/G4s2+GSTASyHzLmdZJoHilmRubmr2nXhccqT3mVn+nldAvIkTEpiGGACPviof5dU0Pr78ivD9DxRE6hrE1mPkrwTEmDreubPyguw==:r2yTHef9KAfAKlRzR1aRBsXE1sTCFfw7ZzyaFbJhu/s=',
    'gpv_Page': 'safeway%3Adelivery%3Aaisles%3Abeverages%3Acoffee',
    's_sq': '%5B%5BB%5D%5D',
    '_derived_epik': 'dj0yJnU9akZoM2pvOTRhYVVrUk9SZ1BRSUR4WUExa1Z3QThWb1ombj1nQ2lJNDBSM3BxVWlHWXJqUTV5X0pnJm09MSZ0PUFBQUFBR05DWnZRJnJtPTEmcnQ9QUFBQUFHTkNadlE',
    '_clsk': '1xyxc59|1665296116367|20|1|m.clarity.ms/collect',
    'nlbi_1610353_2147483392': 'ItmbEpOkFyUdRcH86eNT2gAAAABBWYPlSyCJtru4obBRnMIr',
    '_gat_gtag_UA_172784514_2': '1',
    '_uetsid': '030d43d0479211edb3da1182b9205ed2',
    '_uetvid': '030d6d90479211edb3eb914c2f7acf20',
    '_br_uid_2': 'uid%3D7415811368740%3Av%3D12.0%3Ats%3D1665292796022%3Ahc%3D34',
    'mbox': 'session#6a87d75100c94c3889029a902a374025#1665298038|PC#6a87d75100c94c3889029a902a374025.35_0#1728540978',
    's_nr30': '1665296177909-New',
}

headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'visid_incap_1610353=h8dtO0bjQ7mEd7icuAm+QPJZQmMAAAAAQUIPAAAAAADSu5DwRS97Eh0w5OspBuQr; nlbi_1610353=9cvdIzb4ZHdURYJM6eNT2gAAAAB+POpjf5c+8Soul8QpdWle; incap_ses_975_1610353=bQpbaWNckGlUooeMFOaHDfJZQmMAAAAAgvcCp9bfs5gFeZg72pk8mQ==; ECommBanner=safeway; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommSignInCount=0; at_check=true; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19275%7CMCMID%7C15951149247750483002893438902019755800%7CMCAAMLH-1665897589%7C9%7CMCAAMB-1665897589%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1665299989s%7CNONE%7CvVersion%7C5.2.0; SAFEWAY_MODAL_LINK=; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; safeway_ga=GA1.2.426082052.1665292791; safeway_ga_gid=GA1.2.1855502724.1665292791; s_vncm=1667285999728%26vn%3D1; s_ivc=true; s_cc=true; _gcl_au=1.1.13599361.1665292791; _fbp=fb.1.1665292795914.888364532; aam_uuid=20554257657809015762486872184023500220; _pin_unauth=dWlkPU5ETmpPVE0xTURBdE9ETmpOUzAwTVRoa0xXRmlNbUV0WXpFM05XWXdOemhsT0RBdw; _clck=d7cji9|1|f5k|0; _gid=GA1.2.1150958274.1665292803; _ga_LZL2CD3SX2=GS1.1.1665292802.1.0.1665293162.0.0.0; _ga=GA1.1.426082052.1665292791; reese84=3:TzbkZ+fio/IGneP3/oNsUg==:PxN54+qAaKtJexsi1OqWvXb+9eBufcAGWJhrERWf+kz+UGtwdRS7kvEWA3xfhjxXWOIvggTX6j8b0haj2OgM9WP/v2RBAlRCBW760/dqEOlGVlHlfYVo+qfsJKQ0k35vYvTyWTpa+SfSux+9HnMOPxA9Scg5+QGd9a6VK3N3Ofrv95aZJz1spStSlzYDuKFk8WENPV++nluf+X9Of4w4C1ygDCtNhz0Tk/89buT9NggiXW85hEKMrKv3G/RjomgnmnJa/EtRd4hTr7LtKOSDyttyosYYY4j+4HkoreHOD1PJ/B8zgrTSP2zZcJD2UB7JnyrHJg3aD1I48GpAg6SaSNZ/mjs3yn5uCSaQiALQdURmntuQCqUe4MimX9XODybPkfCFxe/N/R191vvBBxtGLgcBrXdPyAbfHW4cBEZrSC7iSkX+P/G4s2+GSTASyHzLmdZJoHilmRubmr2nXhccqT3mVn+nldAvIkTEpiGGACPviof5dU0Pr78ivD9DxRE6hrE1mPkrwTEmDreubPyguw==:r2yTHef9KAfAKlRzR1aRBsXE1sTCFfw7ZzyaFbJhu/s=; gpv_Page=safeway%3Adelivery%3Aaisles%3Abeverages%3Acoffee; s_sq=%5B%5BB%5D%5D; _derived_epik=dj0yJnU9akZoM2pvOTRhYVVrUk9SZ1BRSUR4WUExa1Z3QThWb1ombj1nQ2lJNDBSM3BxVWlHWXJqUTV5X0pnJm09MSZ0PUFBQUFBR05DWnZRJnJtPTEmcnQ9QUFBQUFHTkNadlE; _clsk=1xyxc59|1665296116367|20|1|m.clarity.ms/collect; nlbi_1610353_2147483392=ItmbEpOkFyUdRcH86eNT2gAAAABBWYPlSyCJtru4obBRnMIr; _gat_gtag_UA_172784514_2=1; _uetsid=030d43d0479211edb3da1182b9205ed2; _uetvid=030d6d90479211edb3eb914c2f7acf20; _br_uid_2=uid%3D7415811368740%3Av%3D12.0%3Ats%3D1665292796022%3Ahc%3D34; mbox=session#6a87d75100c94c3889029a902a374025#1665298038|PC#6a87d75100c94c3889029a902a374025.35_0#1728540978; s_nr30=1665296177909-New',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/beverages/coffee.3132.html?sort=&page=1',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

response_c = requests.get('https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4299198628805&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_5_3&storeid=3132&featured=true&search-uid=uid%253D7415811368740%253Av%253D12.0%253Ats%253D1665292796022%253Ahc%253D32&q=&sort=&userid=&featuredsessionid=&screenwidth=1065&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway&variant=EOT_1660_true', cookies=cookies, headers=headers)


# check status code
print(response_c)

# store json file
result_json_c = response_c.json()

# find the data
result_items = result_json_c["response"]["docs"]

price_coffee = []
item_coffee = []

for result in result_items:
    item_coffee.append(result["name"])
    price_coffee.append(result["price"])

# pandas dataframe
safeway_df_beverages = pd.DataFrame({"item": item_coffee, "price": price_coffee})
safeway_df_beverages["category"] = "Coffee"
safeway_df_beverages["store"] = "Safeway"

print(safeway_df_beverages)

#-------------------------PRODUCE-------------------------------------------------------

cookies = {
    'visid_incap_1610353': 'h8dtO0bjQ7mEd7icuAm+QPJZQmMAAAAAQUIPAAAAAADSu5DwRS97Eh0w5OspBuQr',
    'nlbi_1610353': '9cvdIzb4ZHdURYJM6eNT2gAAAAB+POpjf5c+8Soul8QpdWle',
    'incap_ses_975_1610353': 'bQpbaWNckGlUooeMFOaHDfJZQmMAAAAAgvcCp9bfs5gFeZg72pk8mQ==',
    'ECommBanner': 'safeway',
    'abs_gsession': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
    'abs_previouslogin': '%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D',
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
    's_cc': 'true',
    '_gcl_au': '1.1.13599361.1665292791',
    '_fbp': 'fb.1.1665292795914.888364532',
    'aam_uuid': '20554257657809015762486872184023500220',
    '_pin_unauth': 'dWlkPU5ETmpPVE0xTURBdE9ETmpOUzAwTVRoa0xXRmlNbUV0WXpFM05XWXdOemhsT0RBdw',
    '_clck': 'd7cji9|1|f5k|0',
    '_gid': 'GA1.2.1150958274.1665292803',
    '_ga_LZL2CD3SX2': 'GS1.1.1665292802.1.0.1665293162.0.0.0',
    '_ga': 'GA1.1.426082052.1665292791',
    'reese84': '3:TzbkZ+fio/IGneP3/oNsUg==:PxN54+qAaKtJexsi1OqWvXb+9eBufcAGWJhrERWf+kz+UGtwdRS7kvEWA3xfhjxXWOIvggTX6j8b0haj2OgM9WP/v2RBAlRCBW760/dqEOlGVlHlfYVo+qfsJKQ0k35vYvTyWTpa+SfSux+9HnMOPxA9Scg5+QGd9a6VK3N3Ofrv95aZJz1spStSlzYDuKFk8WENPV++nluf+X9Of4w4C1ygDCtNhz0Tk/89buT9NggiXW85hEKMrKv3G/RjomgnmnJa/EtRd4hTr7LtKOSDyttyosYYY4j+4HkoreHOD1PJ/B8zgrTSP2zZcJD2UB7JnyrHJg3aD1I48GpAg6SaSNZ/mjs3yn5uCSaQiALQdURmntuQCqUe4MimX9XODybPkfCFxe/N/R191vvBBxtGLgcBrXdPyAbfHW4cBEZrSC7iSkX+P/G4s2+GSTASyHzLmdZJoHilmRubmr2nXhccqT3mVn+nldAvIkTEpiGGACPviof5dU0Pr78ivD9DxRE6hrE1mPkrwTEmDreubPyguw==:r2yTHef9KAfAKlRzR1aRBsXE1sTCFfw7ZzyaFbJhu/s=',
    '_gat_gtag_UA_172784514_2': '1',
    's_nr30': '1665296414609-New',
    'gpv_Page': 'safeway%3Adelivery%3Aaisles%3Afruits-vegetables',
    '_uetsid': '030d43d0479211edb3da1182b9205ed2',
    '_uetvid': '030d6d90479211edb3eb914c2f7acf20',
    '_br_uid_2': 'uid%3D7415811368740%3Av%3D12.0%3Ats%3D1665292796022%3Ahc%3D38',
    '_derived_epik': 'dj0yJnU9ZzViT2RyUlJPOFJBcUJuNDZwWjRFMFVxU1l4RE9pUDcmbj03SnJ6M2FHMnJjdVJQNzdBS3p4bFNnJm09MSZ0PUFBQUFBR05DYUI4JnJtPTEmcnQ9QUFBQUFHTkNhQjg',
    '_clsk': '1xyxc59|1665296415576|23|1|m.clarity.ms/collect',
    'nlbi_1610353_2147483392': 'BdCff2f24h0B1vlU6eNT2gAAAADeYAmSS8MLViGV+9OdkcTn',
    's_sq': 'sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%2526link%253DView%252520All%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Ffruits-vegetables%25252Ffresh-fruits.3132.html%25253Fsort%25253D%252526page%25253D1%2526ot%253DA',
    'mbox': 'session#6a87d75100c94c3889029a902a374025#1665298308|PC#6a87d75100c94c3889029a902a374025.35_0#1728541248',
}

headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'visid_incap_1610353=h8dtO0bjQ7mEd7icuAm+QPJZQmMAAAAAQUIPAAAAAADSu5DwRS97Eh0w5OspBuQr; nlbi_1610353=9cvdIzb4ZHdURYJM6eNT2gAAAAB+POpjf5c+8Soul8QpdWle; incap_ses_975_1610353=bQpbaWNckGlUooeMFOaHDfJZQmMAAAAAgvcCp9bfs5gFeZg72pk8mQ==; ECommBanner=safeway; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommSignInCount=0; at_check=true; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19275%7CMCMID%7C15951149247750483002893438902019755800%7CMCAAMLH-1665897589%7C9%7CMCAAMB-1665897589%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1665299989s%7CNONE%7CvVersion%7C5.2.0; SAFEWAY_MODAL_LINK=; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; safeway_ga=GA1.2.426082052.1665292791; safeway_ga_gid=GA1.2.1855502724.1665292791; s_vncm=1667285999728%26vn%3D1; s_ivc=true; s_cc=true; _gcl_au=1.1.13599361.1665292791; _fbp=fb.1.1665292795914.888364532; aam_uuid=20554257657809015762486872184023500220; _pin_unauth=dWlkPU5ETmpPVE0xTURBdE9ETmpOUzAwTVRoa0xXRmlNbUV0WXpFM05XWXdOemhsT0RBdw; _clck=d7cji9|1|f5k|0; _gid=GA1.2.1150958274.1665292803; _ga_LZL2CD3SX2=GS1.1.1665292802.1.0.1665293162.0.0.0; _ga=GA1.1.426082052.1665292791; reese84=3:TzbkZ+fio/IGneP3/oNsUg==:PxN54+qAaKtJexsi1OqWvXb+9eBufcAGWJhrERWf+kz+UGtwdRS7kvEWA3xfhjxXWOIvggTX6j8b0haj2OgM9WP/v2RBAlRCBW760/dqEOlGVlHlfYVo+qfsJKQ0k35vYvTyWTpa+SfSux+9HnMOPxA9Scg5+QGd9a6VK3N3Ofrv95aZJz1spStSlzYDuKFk8WENPV++nluf+X9Of4w4C1ygDCtNhz0Tk/89buT9NggiXW85hEKMrKv3G/RjomgnmnJa/EtRd4hTr7LtKOSDyttyosYYY4j+4HkoreHOD1PJ/B8zgrTSP2zZcJD2UB7JnyrHJg3aD1I48GpAg6SaSNZ/mjs3yn5uCSaQiALQdURmntuQCqUe4MimX9XODybPkfCFxe/N/R191vvBBxtGLgcBrXdPyAbfHW4cBEZrSC7iSkX+P/G4s2+GSTASyHzLmdZJoHilmRubmr2nXhccqT3mVn+nldAvIkTEpiGGACPviof5dU0Pr78ivD9DxRE6hrE1mPkrwTEmDreubPyguw==:r2yTHef9KAfAKlRzR1aRBsXE1sTCFfw7ZzyaFbJhu/s=; _gat_gtag_UA_172784514_2=1; s_nr30=1665296414609-New; gpv_Page=safeway%3Adelivery%3Aaisles%3Afruits-vegetables; _uetsid=030d43d0479211edb3da1182b9205ed2; _uetvid=030d6d90479211edb3eb914c2f7acf20; _br_uid_2=uid%3D7415811368740%3Av%3D12.0%3Ats%3D1665292796022%3Ahc%3D38; _derived_epik=dj0yJnU9ZzViT2RyUlJPOFJBcUJuNDZwWjRFMFVxU1l4RE9pUDcmbj03SnJ6M2FHMnJjdVJQNzdBS3p4bFNnJm09MSZ0PUFBQUFBR05DYUI4JnJtPTEmcnQ9QUFBQUFHTkNhQjg; _clsk=1xyxc59|1665296415576|23|1|m.clarity.ms/collect; nlbi_1610353_2147483392=BdCff2f24h0B1vlU6eNT2gAAAADeYAmSS8MLViGV+9OdkcTn; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%2526link%253DView%252520All%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Ffruits-vegetables%25252Ffresh-fruits.3132.html%25253Fsort%25253D%252526page%25253D1%2526ot%253DA; mbox=session#6a87d75100c94c3889029a902a374025#1665298308|PC#6a87d75100c94c3889029a902a374025.35_0#1728541248',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/fruits-vegetables/fresh-fruits.3132.html?sort=&page=1',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

response_p = requests.get('https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=2604348646304&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_23_1&storeid=3132&featured=true&search-uid=uid%253D7415811368740%253Av%253D12.0%253Ats%253D1665292796022%253Ahc%253D38&q=&sort=&userid=&featuredsessionid=&screenwidth=1065&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway&variant=EOT_1660_true', cookies=cookies, headers=headers)

# store json file
result_json_p = response_p.json()

# find the data
result_items = result_json_p["response"]["docs"]

price_produce = []
item_produce = []

for result in result_items:
    item_produce.append(result["name"])
    price_produce.append(result["price"])

# pandas dataframe
safeway_df_produce = pd.DataFrame({"item": item_produce, "price": price_produce})
safeway_df_produce["category"] = "Produce"
safeway_df_produce["store"] = "Safeway"

print(safeway_df_produce)

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
safeway_df_dairy = pd.DataFrame({"item": item_dairy, "price": price_dairy})
safeway_df_dairy["category"] = "Dairy"
safeway_df_dairy["store"] = "Safeway"

print(safeway_df_dairy)

# combine data frames
frames = [safeway_df_beverages, safeway_df_produce, safeway_df_dairy]

safeway_df = pd.concat(frames)

safeway_df.to_excel('safeway_data.xlsx', index = False)
