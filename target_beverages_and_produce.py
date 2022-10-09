import requests
import pandas as pd
import openpyxl

cookies = {
    'TealeafAkaSid': '_D40b8P9bwjz1NGBYurAQiT0X1ZM_ey7',
    'visitorId': '01838B04BB3002018A04FB01CE23FAD4',
    'sapphire': '1',
    'UserLocation': '94587|37.590|-122.060|CA|US',
    '__gads': 'ID=82813f042185e1d1:T=1664484689:S=ALNI_MbnTY6vWu5SmF6LK6MFBGHt1VOzsA',
    'fiatsCookie': 'DSI_1472|DSN_Hayward|DSZ_94544',
    'ci_pixmgr': 'dcs',
    'ci_engine': 'google',
    'ci_afid': 'google_pla_df',
    '_gcl_aw': 'GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE',
    '_gcl_dc': 'GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE',
    '_gcl_au': '1.1.1630112894.1664484691',
    'crl8.fpcuid': 'ed485473-4f3f-4309-8119-257b48b25f82',
    '__gpi': 'UID=000008cb527e50b3:T=1664484689:RT=1665269888:S=ALNI_MbCD9hUxdVBXhxPy1kPEKOKFXqfTQ',
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwianRpIjoiVEdULjg1ZjkyMTA1NGQ3ZTQ3MGQ4MTFjZjk2Zjc4MTdjYmM0LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImUxNDE3OWE0NjMzNTQ1NmZlYjg2N2ViNGUwNGU2M2JmMmY1OWNkMjg2MTJkMjNjNzZlNWJlYjVlODljOTI2OWEiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.mGCDaNNXkOQ5mm3hdfA9Yd8jGcjy9yiKvlQiiZpqEOt7YxfP3n4UttSuZmaVUYBNBZq328fb5NSFdyspvgDgXT1u_0KKia6HpoOX4Iz_hMPqb1YzRhA_4cjRcmUaQRukYA2SupdA1lqH0bFl9IpGO7sQC7ihnTTgfFcZptamnAqj_6U9TlNKPuuEr7x0d8EFGiQgX2gHPH8cir1ND3C4vMZ9NC05QlIwOpRzBmlMm-DORayQGBe41iatcB6fhUi5CmpNAVRBi4_u-SwLpZWtgDrtls6u4oPQEFG7fahI0vrAUDPrpWURGCcwAvCY2ai8qlatleeyRxmLsL8srJXxtQ',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.',
    'refreshToken': 'WpC1XYXBP5Ix8FmU-7DIS5eW8NYGfE4xw8hBrkWTvziRVwhUih1fXM7P2hKAyvHHOoRL-bezrWFMGDzozZuS5g',
    '_mitata': 'MTg5ZDYxZGU2ZGU4MGEyNDU0M2Y4ODY3NzNjM2NlOTA4ZmEzYmJmNGJiNzM1YzJmZTViOTg0MzRmMWE3ODlkZQ==_/@#/1665273946_/@#/cofAoQ808EKq39UQ_/@#/ZjU2NWQ2OTM3YmI2YzU0M2ZhYjQxZmY0MmExZGE2ODRiYjY2ZmIzODEyNjdiNGZmM2MxOWJhN2M5ZmFkNDBjMw==_/@#/000',
    'ffsession': '{%22sessionHash%22:%221b2125de40174e1665272244303%22%2C%22prevPageName%22:%22top%20deals:%20grocery%20deals%22%2C%22prevPageType%22:%22level%202%22%2C%22prevPageUrl%22:%22https://www.target.com/c/grocery-deals/-/N-k4uyq%22%2C%22sessionHit%22:66%2C%22prevSearchTerm%22:%22non-search%22}',
    '_uetsid': 'acdfb700475c11ed8c8161c92f83798c',
    '_uetvid': '7f482370403811ed8b8e877e2e5ac6ab',
}
headers = {
    'authority': 'redsky.target.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'TealeafAkaSid=_D40b8P9bwjz1NGBYurAQiT0X1ZM_ey7; visitorId=01838B04BB3002018A04FB01CE23FAD4; sapphire=1; UserLocation=94587|37.590|-122.060|CA|US; __gads=ID=82813f042185e1d1:T=1664484689:S=ALNI_MbnTY6vWu5SmF6LK6MFBGHt1VOzsA; fiatsCookie=DSI_1472|DSN_Hayward|DSZ_94544; ci_pixmgr=dcs; ci_engine=google; ci_afid=google_pla_df; _gcl_aw=GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE; _gcl_dc=GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE; _gcl_au=1.1.1630112894.1664484691; crl8.fpcuid=ed485473-4f3f-4309-8119-257b48b25f82; __gpi=UID=000008cb527e50b3:T=1664484689:RT=1665269888:S=ALNI_MbCD9hUxdVBXhxPy1kPEKOKFXqfTQ; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwianRpIjoiVEdULjg1ZjkyMTA1NGQ3ZTQ3MGQ4MTFjZjk2Zjc4MTdjYmM0LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImUxNDE3OWE0NjMzNTQ1NmZlYjg2N2ViNGUwNGU2M2JmMmY1OWNkMjg2MTJkMjNjNzZlNWJlYjVlODljOTI2OWEiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.mGCDaNNXkOQ5mm3hdfA9Yd8jGcjy9yiKvlQiiZpqEOt7YxfP3n4UttSuZmaVUYBNBZq328fb5NSFdyspvgDgXT1u_0KKia6HpoOX4Iz_hMPqb1YzRhA_4cjRcmUaQRukYA2SupdA1lqH0bFl9IpGO7sQC7ihnTTgfFcZptamnAqj_6U9TlNKPuuEr7x0d8EFGiQgX2gHPH8cir1ND3C4vMZ9NC05QlIwOpRzBmlMm-DORayQGBe41iatcB6fhUi5CmpNAVRBi4_u-SwLpZWtgDrtls6u4oPQEFG7fahI0vrAUDPrpWURGCcwAvCY2ai8qlatleeyRxmLsL8srJXxtQ; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=WpC1XYXBP5Ix8FmU-7DIS5eW8NYGfE4xw8hBrkWTvziRVwhUih1fXM7P2hKAyvHHOoRL-bezrWFMGDzozZuS5g; _mitata=MTg5ZDYxZGU2ZGU4MGEyNDU0M2Y4ODY3NzNjM2NlOTA4ZmEzYmJmNGJiNzM1YzJmZTViOTg0MzRmMWE3ODlkZQ==_/@#/1665273946_/@#/cofAoQ808EKq39UQ_/@#/ZjU2NWQ2OTM3YmI2YzU0M2ZhYjQxZmY0MmExZGE2ODRiYjY2ZmIzODEyNjdiNGZmM2MxOWJhN2M5ZmFkNDBjMw==_/@#/000; ffsession={%22sessionHash%22:%221b2125de40174e1665272244303%22%2C%22prevPageName%22:%22top%20deals:%20grocery%20deals%22%2C%22prevPageType%22:%22level%202%22%2C%22prevPageUrl%22:%22https://www.target.com/c/grocery-deals/-/N-k4uyq%22%2C%22sessionHit%22:66%2C%22prevSearchTerm%22:%22non-search%22}; _uetsid=acdfb700475c11ed8c8161c92f83798c; _uetvid=7f482370403811ed8b8e877e2e5ac6ab',
    'origin': 'https://www.target.com',
    'referer': 'https://www.target.com/c/coffee-beverages-grocery/all-deals/-/N-4yi5pZakkos',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

params = {
    'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
    'category': '4yi5p',
    'channel': 'WEB',
    'count': '24',
    'default_purchasability_filter': 'true',
    'faceted_value': 'akkos',
    'include_sponsored': 'true',
    'offset': '0',
    'page': '/c/4yi5p',
    'platform': 'desktop',
    'pricing_store_id': '1472',
    'scheduled_delivery_store_id': '1472',
    'store_ids': '1472,2185,1428,1422,328',
    'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'visitor_id': '01838B04BB3002018A04FB01CE23FAD4',
    'zip': '94587',
}

response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2', params=params, cookies=cookies, headers=headers)

# check status code
#print(response)
    # 200 is correct htp request

# create Json Object
response.json()
    # dictionary with key and value elements, where data is stored

# store json file
result_json = response.json()


# find the data
result_items = result_json["data"]["search"]["products"]

price_target = []
title_target = []

for result in result_items:
    # product title
    title_target.append(result["item"]["product_description"]["title"])

    # price
    price_target.append(result["price"]["formatted_current_price"])

# dictionary with the beverages item and price
beverage_dictionary = {"beverage": title_target, "price": price_target}

# pandas dataframe
target_df_beverages = pd.DataFrame({"item": title_target, "price": price_target})
target_df_beverages["category"] = "Beverages"
target_df_beverages["store"] = "Target"
#print(target_df_beverages)

cookies = {
    'TealeafAkaSid': '_D40b8P9bwjz1NGBYurAQiT0X1ZM_ey7',
    'visitorId': '01838B04BB3002018A04FB01CE23FAD4',
    'sapphire': '1',
    'UserLocation': '94587|37.590|-122.060|CA|US',
    '__gads': 'ID=82813f042185e1d1:T=1664484689:S=ALNI_MbnTY6vWu5SmF6LK6MFBGHt1VOzsA',
    'fiatsCookie': 'DSI_1472|DSN_Hayward|DSZ_94544',
    'ci_pixmgr': 'dcs',
    'ci_engine': 'google',
    'ci_afid': 'google_pla_df',
    '_gcl_aw': 'GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE',
    '_gcl_dc': 'GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE',
    '_gcl_au': '1.1.1630112894.1664484691',
    'crl8.fpcuid': 'ed485473-4f3f-4309-8119-257b48b25f82',
    '__gpi': 'UID=000008cb527e50b3:T=1664484689:RT=1665269888:S=ALNI_MbCD9hUxdVBXhxPy1kPEKOKFXqfTQ',
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwianRpIjoiVEdULjg1ZjkyMTA1NGQ3ZTQ3MGQ4MTFjZjk2Zjc4MTdjYmM0LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImUxNDE3OWE0NjMzNTQ1NmZlYjg2N2ViNGUwNGU2M2JmMmY1OWNkMjg2MTJkMjNjNzZlNWJlYjVlODljOTI2OWEiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.mGCDaNNXkOQ5mm3hdfA9Yd8jGcjy9yiKvlQiiZpqEOt7YxfP3n4UttSuZmaVUYBNBZq328fb5NSFdyspvgDgXT1u_0KKia6HpoOX4Iz_hMPqb1YzRhA_4cjRcmUaQRukYA2SupdA1lqH0bFl9IpGO7sQC7ihnTTgfFcZptamnAqj_6U9TlNKPuuEr7x0d8EFGiQgX2gHPH8cir1ND3C4vMZ9NC05QlIwOpRzBmlMm-DORayQGBe41iatcB6fhUi5CmpNAVRBi4_u-SwLpZWtgDrtls6u4oPQEFG7fahI0vrAUDPrpWURGCcwAvCY2ai8qlatleeyRxmLsL8srJXxtQ',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.',
    'refreshToken': 'WpC1XYXBP5Ix8FmU-7DIS5eW8NYGfE4xw8hBrkWTvziRVwhUih1fXM7P2hKAyvHHOoRL-bezrWFMGDzozZuS5g',
    '_mitata': 'MTlmMTc5YmIxYzJmOWVjNTVmZTdjYmI1ZmY2ZGJhZWRjYjQzNzNmY2RmMzg4YjBiZjlhZTUyMDY0NzM5MWY5ZA==_/@#/1665277826_/@#/cofAoQ808EKq39UQ_/@#/ZDhkYTdjNjQ3NjUzMTY2NDdhZWJhNzljNjUyNjI1Yzg3OGQyZmU4NGZhZTFhOGE3ZWM4Njg0ODM0ZDUxYWRiZQ==_/@#/000',
    'ffsession': '{%22sessionHash%22:%221b2125de40174e1665272244303%22%2C%22prevPageName%22:%22grocery:%20produce%22%2C%22prevPageType%22:%22level%202%22%2C%22prevPageUrl%22:%22https://www.target.com/c/produce-grocery/-/N-u7fty%22%2C%22sessionHit%22:70%2C%22prevSearchTerm%22:%22non-search%22}',
    '_uetsid': 'acdfb700475c11ed8c8161c92f83798c',
    '_uetvid': '7f482370403811ed8b8e877e2e5ac6ab',
}

headers = {
    'authority': 'redsky.target.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'TealeafAkaSid=_D40b8P9bwjz1NGBYurAQiT0X1ZM_ey7; visitorId=01838B04BB3002018A04FB01CE23FAD4; sapphire=1; UserLocation=94587|37.590|-122.060|CA|US; __gads=ID=82813f042185e1d1:T=1664484689:S=ALNI_MbnTY6vWu5SmF6LK6MFBGHt1VOzsA; fiatsCookie=DSI_1472|DSN_Hayward|DSZ_94544; ci_pixmgr=dcs; ci_engine=google; ci_afid=google_pla_df; _gcl_aw=GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE; _gcl_dc=GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE; _gcl_au=1.1.1630112894.1664484691; crl8.fpcuid=ed485473-4f3f-4309-8119-257b48b25f82; __gpi=UID=000008cb527e50b3:T=1664484689:RT=1665269888:S=ALNI_MbCD9hUxdVBXhxPy1kPEKOKFXqfTQ; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwianRpIjoiVEdULjg1ZjkyMTA1NGQ3ZTQ3MGQ4MTFjZjk2Zjc4MTdjYmM0LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImUxNDE3OWE0NjMzNTQ1NmZlYjg2N2ViNGUwNGU2M2JmMmY1OWNkMjg2MTJkMjNjNzZlNWJlYjVlODljOTI2OWEiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.mGCDaNNXkOQ5mm3hdfA9Yd8jGcjy9yiKvlQiiZpqEOt7YxfP3n4UttSuZmaVUYBNBZq328fb5NSFdyspvgDgXT1u_0KKia6HpoOX4Iz_hMPqb1YzRhA_4cjRcmUaQRukYA2SupdA1lqH0bFl9IpGO7sQC7ihnTTgfFcZptamnAqj_6U9TlNKPuuEr7x0d8EFGiQgX2gHPH8cir1ND3C4vMZ9NC05QlIwOpRzBmlMm-DORayQGBe41iatcB6fhUi5CmpNAVRBi4_u-SwLpZWtgDrtls6u4oPQEFG7fahI0vrAUDPrpWURGCcwAvCY2ai8qlatleeyRxmLsL8srJXxtQ; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=WpC1XYXBP5Ix8FmU-7DIS5eW8NYGfE4xw8hBrkWTvziRVwhUih1fXM7P2hKAyvHHOoRL-bezrWFMGDzozZuS5g; _mitata=MTlmMTc5YmIxYzJmOWVjNTVmZTdjYmI1ZmY2ZGJhZWRjYjQzNzNmY2RmMzg4YjBiZjlhZTUyMDY0NzM5MWY5ZA==_/@#/1665277826_/@#/cofAoQ808EKq39UQ_/@#/ZDhkYTdjNjQ3NjUzMTY2NDdhZWJhNzljNjUyNjI1Yzg3OGQyZmU4NGZhZTFhOGE3ZWM4Njg0ODM0ZDUxYWRiZQ==_/@#/000; ffsession={%22sessionHash%22:%221b2125de40174e1665272244303%22%2C%22prevPageName%22:%22grocery:%20produce%22%2C%22prevPageType%22:%22level%202%22%2C%22prevPageUrl%22:%22https://www.target.com/c/produce-grocery/-/N-u7fty%22%2C%22sessionHit%22:70%2C%22prevSearchTerm%22:%22non-search%22}; _uetsid=acdfb700475c11ed8c8161c92f83798c; _uetvid=7f482370403811ed8b8e877e2e5ac6ab',
    'origin': 'https://www.target.com',
    'referer': 'https://www.target.com/c/fresh-fruit-produce-grocery/-/N-4tglt',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

params = {
    'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
    'category': '4tglt',
    'channel': 'WEB',
    'count': '24',
    'default_purchasability_filter': 'true',
    'include_sponsored': 'true',
    'offset': '0',
    'page': '/c/4tglt',
    'platform': 'desktop',
    'pricing_store_id': '1472',
    'scheduled_delivery_store_id': '1472',
    'store_ids': '1472,2185,1428,1422,328',
    'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'visitor_id': '01838B04BB3002018A04FB01CE23FAD4',
    'zip': '94587',
}

response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2', params=params, cookies=cookies, headers=headers)


# create Json Object
# dictionary with key and value elements, where data is stored

# store json file
result_json = response.json()

# find the data
result_items = result_json["data"]["search"]["products"]

price_produce = []
title_produce = []

for result in result_items:
    # product title
    title_produce.append(result["item"]["product_description"]["title"])

    # price
    price_produce.append(result["price"]["formatted_current_price"])

# dictionary with the produce name and price
produce_dictionary = {"produce": title_produce, "price": price_produce}

# list with everything
target = [produce_dictionary, beverage_dictionary ]
dictionary_of_all_stores = {"target": target}


# pandas datafram
target_df_produce = pd.DataFrame({"item": title_produce, "price": price_produce})
target_df_produce["category"] = "Produce"
target_df_produce["store"] = "Target"


# combine data frames
frames = [target_df_beverages, target_df_produce]

target_df = pd.concat(frames)

target_df.to_excel('target_multiple_pages.xlsx', index = False)