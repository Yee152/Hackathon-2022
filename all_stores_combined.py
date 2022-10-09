import requests
import pandas as pd
import openpyxl


#-----------COFFEE-------------------------------------
cookies = {
    '_gcl_au': '1.1.87654026.1665297822',
    '_gid': 'GA1.2.177344093.1665297823',
    'gig_bootstrap_3_GKrrAPXlGczVrnHfPGZmmUeR7ANOjp5s_fPs142vSSeUf_SVNfdAA11jS5mhdWKo': 'login_ver4',
    'notice_behavior': 'implied,eu',
    '_fbp': 'fb.1.1665297823153.910562219',
    '_clck': '1dp0rco|1|f5k|0',
    '_clsk': '4xof05|1665297825402|2|1|m.clarity.ms/collect',
    'ajs_anonymous_id': 'c6fcd1e3-efef-4dd7-adf5-15daeac1e898',
    '_dd_r': '1',
    '_dd': '1e400c5c-44b8-42c0-a6b1-4533ecd6e293',
    'gig_canary': 'false',
    'gig_canary_ver': '13406-3-27754950',
    'gig_bootstrap_3_Tikef4yXIbKNr4dyPwM27hHXXPJDmg2vn3kJgkBOG8WpYu9P_rGd6tz883airYyj': 'login_ver4',
    '__adroll_fpc': '8de4041ed9d1b366fedfa0e7b1fead57-1665297843979',
    'liveagent_oref': 'https://www.raleys.com/',
    'liveagent_ptid': '5c10e8f9-11c3-4177-bf9f-c7438213dd13',
    '_gat': '1',
    '_dc_gtm_UA-72342337-4': '1',
    '_gat_UA-72342337-4': '1',
    '_uetsid': 'b91138c0479d11eda3954d504bf0a6eb',
    '_uetvid': 'b91161a0479d11ed8bcd6b4fa07fee19',
    '__ar_v4': 'DB6KNLYDXVASPHFNWFWEX3%3A20221008%3A4%7CAA4HHHFBZVHRNCRWD6UMK2%3A20221008%3A4%7CFARJQKXGQ5FMVA2Y5EDNQ7%3A20221008%3A4',
    'session-ray': '.eJxNjMtygjAARf8la3V4CBV2HZSatIGRwaJuMkBCCe8hgAan_1463XRxN-eee5-AZD0TObCzuBJsBUjH-jpuWDMAe-jHhQgmBG8bMrQla4ANmER58pZynyN4nqHqcWRtFqim2qdcMqdaNSWV1d0caOIC6jg8PXDxKj-cP-eiVSUsWhXv09krDorn3Pk1CoY4Mv713Uijh1g2eVJbI4vUiV4w95tA0ugsYF3l9Pc_vGpeCA1v_pL-Udnsk-DovrNEwWtj4johu_WpdLOdMA8Ux0jqt85FSFh9cAcrMArWE06BbSgvuqlut98__PhbNQ.FiQD_g.wtzrG4HukbkfgP4wq-HmBBQQxrg',
    'TS01363ad3': '01bcf4b49f635d7c004c07e36c5b0076384a962df3602bd4c6c6f83d816071f89e17cc349c9b1313c1ccba113b33e3d9b1f3ffe284',
    'TS014dd9f8': '01bcf4b49f3d040e87c2d9e796c88bc81ddbdfbe4f602bd4c6c6f83d816071f89e17cc349c68f6640065a316dbb8bf1ec634dc5e8afbd94c730694e6fbfd71e13639a3ce56',
    'liveagent_sid': '71a6521c-7b94-4bb9-879c-89221501fe3a',
    'liveagent_vc': '5',
    '_ga': 'GA1.2.130287041.1665297823',
    '_br_uid_2': 'uid%3D3895371532489%3Av%3D15.0%3Ats%3D1665297852426%3Ahc%3D17',
    '_ga_MXYSWRDLRL': 'GS1.1.1665297851.1.1.1665299082.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gcl_au=1.1.87654026.1665297822; _gid=GA1.2.177344093.1665297823; gig_bootstrap_3_GKrrAPXlGczVrnHfPGZmmUeR7ANOjp5s_fPs142vSSeUf_SVNfdAA11jS5mhdWKo=login_ver4; notice_behavior=implied,eu; _fbp=fb.1.1665297823153.910562219; _clck=1dp0rco|1|f5k|0; _clsk=4xof05|1665297825402|2|1|m.clarity.ms/collect; ajs_anonymous_id=c6fcd1e3-efef-4dd7-adf5-15daeac1e898; _dd_r=1; _dd=1e400c5c-44b8-42c0-a6b1-4533ecd6e293; gig_canary=false; gig_canary_ver=13406-3-27754950; gig_bootstrap_3_Tikef4yXIbKNr4dyPwM27hHXXPJDmg2vn3kJgkBOG8WpYu9P_rGd6tz883airYyj=login_ver4; __adroll_fpc=8de4041ed9d1b366fedfa0e7b1fead57-1665297843979; liveagent_oref=https://www.raleys.com/; liveagent_ptid=5c10e8f9-11c3-4177-bf9f-c7438213dd13; _gat=1; _dc_gtm_UA-72342337-4=1; _gat_UA-72342337-4=1; _uetsid=b91138c0479d11eda3954d504bf0a6eb; _uetvid=b91161a0479d11ed8bcd6b4fa07fee19; __ar_v4=DB6KNLYDXVASPHFNWFWEX3%3A20221008%3A4%7CAA4HHHFBZVHRNCRWD6UMK2%3A20221008%3A4%7CFARJQKXGQ5FMVA2Y5EDNQ7%3A20221008%3A4; session-ray=.eJxNjMtygjAARf8la3V4CBV2HZSatIGRwaJuMkBCCe8hgAan_1463XRxN-eee5-AZD0TObCzuBJsBUjH-jpuWDMAe-jHhQgmBG8bMrQla4ANmER58pZynyN4nqHqcWRtFqim2qdcMqdaNSWV1d0caOIC6jg8PXDxKj-cP-eiVSUsWhXv09krDorn3Pk1CoY4Mv713Uijh1g2eVJbI4vUiV4w95tA0ugsYF3l9Pc_vGpeCA1v_pL-Udnsk-DovrNEwWtj4johu_WpdLOdMA8Ux0jqt85FSFh9cAcrMArWE06BbSgvuqlut98__PhbNQ.FiQD_g.wtzrG4HukbkfgP4wq-HmBBQQxrg; TS01363ad3=01bcf4b49f635d7c004c07e36c5b0076384a962df3602bd4c6c6f83d816071f89e17cc349c9b1313c1ccba113b33e3d9b1f3ffe284; TS014dd9f8=01bcf4b49f3d040e87c2d9e796c88bc81ddbdfbe4f602bd4c6c6f83d816071f89e17cc349c68f6640065a316dbb8bf1ec634dc5e8afbd94c730694e6fbfd71e13639a3ce56; liveagent_sid=71a6521c-7b94-4bb9-879c-89221501fe3a; liveagent_vc=5; _ga=GA1.2.130287041.1665297823; _br_uid_2=uid%3D3895371532489%3Av%3D15.0%3Ats%3D1665297852426%3Ahc%3D17; _ga_MXYSWRDLRL=GS1.1.1665297851.1.1.1665299082.0.0.0',
    'Referer': 'https://shop.raleys.com/shop/categories/141?page=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'User-Context': 'eyJTdG9yZUlkIjoiMTI4IiwiRnVsZmlsbG1lbnRUeXBlIjoicGlja3VwIn0=',
    'X-Unata-Mode': 'grocery',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'category_id': '141',
    'category_ids': '141',
    'limit': '60',
    'offset': '0',
    'page': '2',
    'sort': 'popular',
}

response_c = requests.get('https://shop.raleys.com/api/v2/store_products', params=params, cookies=cookies, headers=headers)

# store json file
result_json = response_c.json()

# find the data
result_items_c = result_json["items"]

price_coffee = []
title_coffee = []

for result in result_items_c:
    # product title
    title_coffee.append(result["name"])
    # price
    price_coffee.append(result["base_price"])

# pandas dataframe
raleys_df_beverage = pd.DataFrame({"item": title_coffee, "price": price_coffee})
raleys_df_beverage["category"] = "Beverage"
raleys_df_beverage["store"] = "Raleys"

#-----------PRODUCE------------------------------------
cookies = {
    '_gcl_au': '1.1.87654026.1665297822',
    '_gid': 'GA1.2.177344093.1665297823',
    'gig_bootstrap_3_GKrrAPXlGczVrnHfPGZmmUeR7ANOjp5s_fPs142vSSeUf_SVNfdAA11jS5mhdWKo': 'login_ver4',
    'notice_behavior': 'implied,eu',
    '_fbp': 'fb.1.1665297823153.910562219',
    '_clck': '1dp0rco|1|f5k|0',
    '_clsk': '4xof05|1665297825402|2|1|m.clarity.ms/collect',
    'TS01363ad3': '01c609ed7b9c23e1b6cd7450d0b01ff24709276b36b35288323cfca27d4fe89b72c37632a5390eb749e8098cdd007c7315d20444de',
    'ajs_anonymous_id': 'c6fcd1e3-efef-4dd7-adf5-15daeac1e898',
    '_dd_r': '1',
    '_dd': '1e400c5c-44b8-42c0-a6b1-4533ecd6e293',
    'gig_canary': 'false',
    'gig_canary_ver': '13406-3-27754950',
    'gig_bootstrap_3_Tikef4yXIbKNr4dyPwM27hHXXPJDmg2vn3kJgkBOG8WpYu9P_rGd6tz883airYyj': 'login_ver4',
    '__adroll_fpc': '8de4041ed9d1b366fedfa0e7b1fead57-1665297843979',
    'liveagent_oref': 'https://www.raleys.com/',
    'liveagent_ptid': '5c10e8f9-11c3-4177-bf9f-c7438213dd13',
    'session-ray': '.eJxNjMtygjAARf8la3V4CBV2HZSatIGRwaJuMkBCCe8hgAan_1463XRxN-eee5-AZD0TObCzuBJsBUjH-jpuWDMAe-jHhQgmBG8bMrQla4ANmER58pZynyN4nqHqcWRtFqim2qdcMqdaNSWV1d0caOIC6jg8PXDxKj-cP-eiVSUsWhXv09krDorn3Pk1CoY4Mv713Uijh1g2eVJbI4vUiV4w95tA0ugsYF3l9Pc_vGpeCA1v_pL-Udnsk-DovrNEwWtj4johu_WpdLOdMA8Ux0jqt85FSFh9cAcrMArWE06BbSgvuqlut98__PhbNQ.FiP_VQ.1DDvF4PngDs4JoCizDZM61-fsTI',
    'TS014dd9f8': '01c609ed7b6dfc9f43f0e2dbaf5d5daa21a151fa11b35288323cfca27d4fe89b72c37632a5dce4577fb1bf98f0bb538548f5400594692676909cea6481dd0cfccb0ecff52e',
    '_uetsid': 'b91138c0479d11eda3954d504bf0a6eb',
    '_uetvid': 'b91161a0479d11ed8bcd6b4fa07fee19',
    '__ar_v4': 'FARJQKXGQ5FMVA2Y5EDNQ7%3A20221008%3A3%7CAA4HHHFBZVHRNCRWD6UMK2%3A20221008%3A3%7CDB6KNLYDXVASPHFNWFWEX3%3A20221008%3A3',
    'liveagent_sid': 'e65f54f0-7bf4-40a6-bc2e-e50d308f6880',
    'liveagent_vc': '4',
    '_ga': 'GA1.2.130287041.1665297823',
    '_gat': '1',
    '_gat_UA-72342337-4': '1',
    '_br_uid_2': 'uid%3D3895371532489%3Av%3D15.0%3Ats%3D1665297852426%3Ahc%3D12',
    '_ga_MXYSWRDLRL': 'GS1.1.1665297851.1.1.1665297950.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gcl_au=1.1.87654026.1665297822; _gid=GA1.2.177344093.1665297823; gig_bootstrap_3_GKrrAPXlGczVrnHfPGZmmUeR7ANOjp5s_fPs142vSSeUf_SVNfdAA11jS5mhdWKo=login_ver4; notice_behavior=implied,eu; _fbp=fb.1.1665297823153.910562219; _clck=1dp0rco|1|f5k|0; _clsk=4xof05|1665297825402|2|1|m.clarity.ms/collect; TS01363ad3=01c609ed7b9c23e1b6cd7450d0b01ff24709276b36b35288323cfca27d4fe89b72c37632a5390eb749e8098cdd007c7315d20444de; ajs_anonymous_id=c6fcd1e3-efef-4dd7-adf5-15daeac1e898; _dd_r=1; _dd=1e400c5c-44b8-42c0-a6b1-4533ecd6e293; gig_canary=false; gig_canary_ver=13406-3-27754950; gig_bootstrap_3_Tikef4yXIbKNr4dyPwM27hHXXPJDmg2vn3kJgkBOG8WpYu9P_rGd6tz883airYyj=login_ver4; __adroll_fpc=8de4041ed9d1b366fedfa0e7b1fead57-1665297843979; liveagent_oref=https://www.raleys.com/; liveagent_ptid=5c10e8f9-11c3-4177-bf9f-c7438213dd13; session-ray=.eJxNjMtygjAARf8la3V4CBV2HZSatIGRwaJuMkBCCe8hgAan_1463XRxN-eee5-AZD0TObCzuBJsBUjH-jpuWDMAe-jHhQgmBG8bMrQla4ANmER58pZynyN4nqHqcWRtFqim2qdcMqdaNSWV1d0caOIC6jg8PXDxKj-cP-eiVSUsWhXv09krDorn3Pk1CoY4Mv713Uijh1g2eVJbI4vUiV4w95tA0ugsYF3l9Pc_vGpeCA1v_pL-Udnsk-DovrNEwWtj4johu_WpdLOdMA8Ux0jqt85FSFh9cAcrMArWE06BbSgvuqlut98__PhbNQ.FiP_VQ.1DDvF4PngDs4JoCizDZM61-fsTI; TS014dd9f8=01c609ed7b6dfc9f43f0e2dbaf5d5daa21a151fa11b35288323cfca27d4fe89b72c37632a5dce4577fb1bf98f0bb538548f5400594692676909cea6481dd0cfccb0ecff52e; _uetsid=b91138c0479d11eda3954d504bf0a6eb; _uetvid=b91161a0479d11ed8bcd6b4fa07fee19; __ar_v4=FARJQKXGQ5FMVA2Y5EDNQ7%3A20221008%3A3%7CAA4HHHFBZVHRNCRWD6UMK2%3A20221008%3A3%7CDB6KNLYDXVASPHFNWFWEX3%3A20221008%3A3; liveagent_sid=e65f54f0-7bf4-40a6-bc2e-e50d308f6880; liveagent_vc=4; _ga=GA1.2.130287041.1665297823; _gat=1; _gat_UA-72342337-4=1; _br_uid_2=uid%3D3895371532489%3Av%3D15.0%3Ats%3D1665297852426%3Ahc%3D12; _ga_MXYSWRDLRL=GS1.1.1665297851.1.1.1665297950.0.0.0',
    'Referer': 'https://shop.raleys.com/shop/categories/2?page=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'User-Context': 'eyJTdG9yZUlkIjoiMTI4IiwiRnVsZmlsbG1lbnRUeXBlIjoicGlja3VwIn0=',
    'X-Unata-Mode': 'grocery',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'category_id': '2',
    'category_ids': '2',
    'limit': '60',
    'offset': '0',
    'page': '2',
    'sort': 'popular',
}

response = requests.get('https://shop.raleys.com/api/v2/store_products', params=params, cookies=cookies, headers=headers)

# store json file
result_json = response.json()

# find the data
result_items = result_json["items"]

price_produce = []
title_produce = []

for result in result_items:
    # product title
    title_produce.append(result["name"])
    # price
    price_produce.append(result["base_price"])

# pandas dataframe
raleys_df_produce = pd.DataFrame({"item": title_produce, "price": price_produce})
raleys_df_produce["category"] = "Produce"
raleys_df_produce["store"] = "Raleys"

#--------------------DAIRY-------------------------
cookies = {
    '_gcl_au': '1.1.87654026.1665297822',
    '_gid': 'GA1.2.177344093.1665297823',
    'gig_bootstrap_3_GKrrAPXlGczVrnHfPGZmmUeR7ANOjp5s_fPs142vSSeUf_SVNfdAA11jS5mhdWKo': 'login_ver4',
    'notice_behavior': 'implied,eu',
    '_fbp': 'fb.1.1665297823153.910562219',
    '_clck': '1dp0rco|1|f5k|0',
    '_clsk': '4xof05|1665297825402|2|1|m.clarity.ms/collect',
    'ajs_anonymous_id': 'c6fcd1e3-efef-4dd7-adf5-15daeac1e898',
    '_dd_r': '1',
    '_dd': '1e400c5c-44b8-42c0-a6b1-4533ecd6e293',
    'gig_canary': 'false',
    'gig_canary_ver': '13406-3-27754950',
    'gig_bootstrap_3_Tikef4yXIbKNr4dyPwM27hHXXPJDmg2vn3kJgkBOG8WpYu9P_rGd6tz883airYyj': 'login_ver4',
    '__adroll_fpc': '8de4041ed9d1b366fedfa0e7b1fead57-1665297843979',
    'liveagent_oref': 'https://www.raleys.com/',
    'liveagent_ptid': '5c10e8f9-11c3-4177-bf9f-c7438213dd13',
    '_uetsid': 'b91138c0479d11eda3954d504bf0a6eb',
    '_uetvid': 'b91161a0479d11ed8bcd6b4fa07fee19',
    '__ar_v4': 'DB6KNLYDXVASPHFNWFWEX3%3A20221008%3A4%7CAA4HHHFBZVHRNCRWD6UMK2%3A20221008%3A4%7CFARJQKXGQ5FMVA2Y5EDNQ7%3A20221008%3A4',
    'session-ray': '.eJxNjMtygjAARf8la3V4CBV2HZSatIGRwaJuMkBCCe8hgAan_1463XRxN-eee5-AZD0TObCzuBJsBUjH-jpuWDMAe-jHhQgmBG8bMrQla4ANmER58pZynyN4nqHqcWRtFqim2qdcMqdaNSWV1d0caOIC6jg8PXDxKj-cP-eiVSUsWhXv09krDorn3Pk1CoY4Mv713Uijh1g2eVJbI4vUiV4w95tA0ugsYF3l9Pc_vGpeCA1v_pL-Udnsk-DovrNEwWtj4johu_WpdLOdMA8Ux0jqt85FSFh9cAcrMArWE06BbSgvuqlut98__PhbNQ.FiQD_g.wtzrG4HukbkfgP4wq-HmBBQQxrg',
    'TS01363ad3': '01bcf4b49f635d7c004c07e36c5b0076384a962df3602bd4c6c6f83d816071f89e17cc349c9b1313c1ccba113b33e3d9b1f3ffe284',
    'TS014dd9f8': '01bcf4b49f3d040e87c2d9e796c88bc81ddbdfbe4f602bd4c6c6f83d816071f89e17cc349c68f6640065a316dbb8bf1ec634dc5e8afbd94c730694e6fbfd71e13639a3ce56',
    'liveagent_sid': '71a6521c-7b94-4bb9-879c-89221501fe3a',
    'liveagent_vc': '5',
    '_ga': 'GA1.2.130287041.1665297823',
    '_gat': '1',
    '_dc_gtm_UA-72342337-4': '1',
    '_gat_UA-72342337-4': '1',
    '_br_uid_2': 'uid%3D3895371532489%3Av%3D15.0%3Ats%3D1665297852426%3Ahc%3D21',
    '_ga_MXYSWRDLRL': 'GS1.1.1665297851.1.1.1665299321.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gcl_au=1.1.87654026.1665297822; _gid=GA1.2.177344093.1665297823; gig_bootstrap_3_GKrrAPXlGczVrnHfPGZmmUeR7ANOjp5s_fPs142vSSeUf_SVNfdAA11jS5mhdWKo=login_ver4; notice_behavior=implied,eu; _fbp=fb.1.1665297823153.910562219; _clck=1dp0rco|1|f5k|0; _clsk=4xof05|1665297825402|2|1|m.clarity.ms/collect; ajs_anonymous_id=c6fcd1e3-efef-4dd7-adf5-15daeac1e898; _dd_r=1; _dd=1e400c5c-44b8-42c0-a6b1-4533ecd6e293; gig_canary=false; gig_canary_ver=13406-3-27754950; gig_bootstrap_3_Tikef4yXIbKNr4dyPwM27hHXXPJDmg2vn3kJgkBOG8WpYu9P_rGd6tz883airYyj=login_ver4; __adroll_fpc=8de4041ed9d1b366fedfa0e7b1fead57-1665297843979; liveagent_oref=https://www.raleys.com/; liveagent_ptid=5c10e8f9-11c3-4177-bf9f-c7438213dd13; _uetsid=b91138c0479d11eda3954d504bf0a6eb; _uetvid=b91161a0479d11ed8bcd6b4fa07fee19; __ar_v4=DB6KNLYDXVASPHFNWFWEX3%3A20221008%3A4%7CAA4HHHFBZVHRNCRWD6UMK2%3A20221008%3A4%7CFARJQKXGQ5FMVA2Y5EDNQ7%3A20221008%3A4; session-ray=.eJxNjMtygjAARf8la3V4CBV2HZSatIGRwaJuMkBCCe8hgAan_1463XRxN-eee5-AZD0TObCzuBJsBUjH-jpuWDMAe-jHhQgmBG8bMrQla4ANmER58pZynyN4nqHqcWRtFqim2qdcMqdaNSWV1d0caOIC6jg8PXDxKj-cP-eiVSUsWhXv09krDorn3Pk1CoY4Mv713Uijh1g2eVJbI4vUiV4w95tA0ugsYF3l9Pc_vGpeCA1v_pL-Udnsk-DovrNEwWtj4johu_WpdLOdMA8Ux0jqt85FSFh9cAcrMArWE06BbSgvuqlut98__PhbNQ.FiQD_g.wtzrG4HukbkfgP4wq-HmBBQQxrg; TS01363ad3=01bcf4b49f635d7c004c07e36c5b0076384a962df3602bd4c6c6f83d816071f89e17cc349c9b1313c1ccba113b33e3d9b1f3ffe284; TS014dd9f8=01bcf4b49f3d040e87c2d9e796c88bc81ddbdfbe4f602bd4c6c6f83d816071f89e17cc349c68f6640065a316dbb8bf1ec634dc5e8afbd94c730694e6fbfd71e13639a3ce56; liveagent_sid=71a6521c-7b94-4bb9-879c-89221501fe3a; liveagent_vc=5; _ga=GA1.2.130287041.1665297823; _gat=1; _dc_gtm_UA-72342337-4=1; _gat_UA-72342337-4=1; _br_uid_2=uid%3D3895371532489%3Av%3D15.0%3Ats%3D1665297852426%3Ahc%3D21; _ga_MXYSWRDLRL=GS1.1.1665297851.1.1.1665299321.0.0.0',
    'Referer': 'https://shop.raleys.com/shop/categories/129?page=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'User-Context': 'eyJTdG9yZUlkIjoiMTI4IiwiRnVsZmlsbG1lbnRUeXBlIjoicGlja3VwIn0=',
    'X-Unata-Mode': 'grocery',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'category_id': '129',
    'category_ids': '129',
    'limit': '60',
    'offset': '0',
    'page': '2',
    'sort': 'popular',
}

response_d = requests.get('https://shop.raleys.com/api/v2/store_products', params=params, cookies=cookies, headers=headers)

# store json file
result_json_d = response_d.json()

# find the data
result_items_d = result_json_d["items"]

price_milk = []
title_milk = []

for result in result_items_d:
    # product title
    title_milk.append(result["name"])
    # price
    price_milk.append(result["base_price"])

# pandas dataframe
raleys_df_dairy = pd.DataFrame({"item": title_milk, "price": price_milk})
raleys_df_dairy["category"] = "Dairy"
raleys_df_dairy["store"] = "Raleys"

# combine data frames
frames = [raleys_df_beverage, raleys_df_produce, raleys_df_dairy]

raleys_df = pd.concat(frames)



#----------------------------------------------------------------safeway----------------------------------------------------------------
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



#-------------------------------------------------------------------Target-----------------------------------------------------------------------------------------------
#-----------COFFEE
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
target_df_beverages["category"] = "Coffee"
target_df_beverages["store"] = "Target"

#PRODUCE--------------------------------------------------------------
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


#DAIRY---------------------------------------------
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
    '_mitata': 'YmY2ZDlmNmViOGExNTczOWNlMzRmOTZlZDEwZDAxNDFjMzAxY2U3NjkyZWYzOWFhZTA2YWQ3NGMxMjM3NzllNw==_/@#/1665283815_/@#/cofAoQ808EKq39UQ_/@#/ZmNmYjgzMjZhYTllNTYxMWUwMmVmOGQzMjNhOTU1MTRhYTBkN2YwNzU3YzhkMDk1ZmMzNzdjOWJkODI5NjFkMA==_/@#/000',
    'ffsession': '{%22sessionHash%22:%221b2125de40174e1665272244303%22%2C%22prevPageName%22:%22grocery:%20dairy:%20milk%22%2C%22prevPageType%22:%22level%203%22%2C%22prevPageUrl%22:%22https://www.target.com/c/milk-dairy-grocery/-/N-5xszh%22%2C%22sessionHit%22:75%2C%22prevSearchTerm%22:%22non-search%22}',
    '_uetsid': 'acdfb700475c11ed8c8161c92f83798c',
    '_uetvid': '7f482370403811ed8b8e877e2e5ac6ab',
}

headers = {
    'authority': 'redsky.target.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'TealeafAkaSid=_D40b8P9bwjz1NGBYurAQiT0X1ZM_ey7; visitorId=01838B04BB3002018A04FB01CE23FAD4; sapphire=1; UserLocation=94587|37.590|-122.060|CA|US; __gads=ID=82813f042185e1d1:T=1664484689:S=ALNI_MbnTY6vWu5SmF6LK6MFBGHt1VOzsA; fiatsCookie=DSI_1472|DSN_Hayward|DSZ_94544; ci_pixmgr=dcs; ci_engine=google; ci_afid=google_pla_df; _gcl_aw=GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE; _gcl_dc=GCL.1664484691.CjwKCAjwhNWZBhB_EiwAPzlhNt666NKEszKmnCZmYSga1cbMMy9f51zIBYFhTjUBxDmqa8K5VZAyCxoC0S0QAvD_BwE; _gcl_au=1.1.1630112894.1664484691; crl8.fpcuid=ed485473-4f3f-4309-8119-257b48b25f82; __gpi=UID=000008cb527e50b3:T=1664484689:RT=1665269888:S=ALNI_MbCD9hUxdVBXhxPy1kPEKOKFXqfTQ; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwianRpIjoiVEdULjg1ZjkyMTA1NGQ3ZTQ3MGQ4MTFjZjk2Zjc4MTdjYmM0LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImUxNDE3OWE0NjMzNTQ1NmZlYjg2N2ViNGUwNGU2M2JmMmY1OWNkMjg2MTJkMjNjNzZlNWJlYjVlODljOTI2OWEiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.mGCDaNNXkOQ5mm3hdfA9Yd8jGcjy9yiKvlQiiZpqEOt7YxfP3n4UttSuZmaVUYBNBZq328fb5NSFdyspvgDgXT1u_0KKia6HpoOX4Iz_hMPqb1YzRhA_4cjRcmUaQRukYA2SupdA1lqH0bFl9IpGO7sQC7ihnTTgfFcZptamnAqj_6U9TlNKPuuEr7x0d8EFGiQgX2gHPH8cir1ND3C4vMZ9NC05QlIwOpRzBmlMm-DORayQGBe41iatcB6fhUi5CmpNAVRBi4_u-SwLpZWtgDrtls6u4oPQEFG7fahI0vrAUDPrpWURGCcwAvCY2ai8qlatleeyRxmLsL8srJXxtQ; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIxZWE5MDk0ZS0yYzE1LTQyNjgtOWZjMC1iNzQ0NmUyOTEwMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjUzNTg2NDUsImlhdCI6MTY2NTI3MjI0NSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=WpC1XYXBP5Ix8FmU-7DIS5eW8NYGfE4xw8hBrkWTvziRVwhUih1fXM7P2hKAyvHHOoRL-bezrWFMGDzozZuS5g; _mitata=YmY2ZDlmNmViOGExNTczOWNlMzRmOTZlZDEwZDAxNDFjMzAxY2U3NjkyZWYzOWFhZTA2YWQ3NGMxMjM3NzllNw==_/@#/1665283815_/@#/cofAoQ808EKq39UQ_/@#/ZmNmYjgzMjZhYTllNTYxMWUwMmVmOGQzMjNhOTU1MTRhYTBkN2YwNzU3YzhkMDk1ZmMzNzdjOWJkODI5NjFkMA==_/@#/000; ffsession={%22sessionHash%22:%221b2125de40174e1665272244303%22%2C%22prevPageName%22:%22grocery:%20dairy:%20milk%22%2C%22prevPageType%22:%22level%203%22%2C%22prevPageUrl%22:%22https://www.target.com/c/milk-dairy-grocery/-/N-5xszh%22%2C%22sessionHit%22:75%2C%22prevSearchTerm%22:%22non-search%22}; _uetsid=acdfb700475c11ed8c8161c92f83798c; _uetvid=7f482370403811ed8b8e877e2e5ac6ab',
    'origin': 'https://www.target.com',
    'referer': 'https://www.target.com/c/milk-dairy-grocery/-/N-5xszh',
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
    'category': '5xszh',
    'channel': 'WEB',
    'count': '24',
    'default_purchasability_filter': 'true',
    'include_sponsored': 'true',
    'offset': '0',
    'page': '/c/5xszh',
    'platform': 'desktop',
    'pricing_store_id': '1472',
    'scheduled_delivery_store_id': '1472',
    'store_ids': '1472,2185,1428,1422,328',
    'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'visitor_id': '01838B04BB3002018A04FB01CE23FAD4',
    'zip': '94587',
}

response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2', params=params, cookies=cookies, headers=headers)

result_json_milk = response.json()

result_items = result_json_milk["data"]["search"]["products"]

price_milk = []
title_milk = []

for result in result_items:
    # product title
    title_milk.append(result["item"]["product_description"]["title"])

    # price
    price_milk.append(result["price"]["formatted_current_price"])

target_df_dairy = pd.DataFrame({"item": title_milk, "price": price_milk})
target_df_dairy["category"] = "Dairy"
target_df_dairy["store"] = "Target"


# combine data frames
frames = [target_df_beverages, target_df_produce, target_df_dairy]
target_df = pd.concat(frames)

#combine data frames from all stores
all_stores = [target_df, raleys_df, safeway_df]
all_stores_df = pd.concat(all_stores)
all_stores_df.to_excel('all_stores_data.xlsx', index = False)



