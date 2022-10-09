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

raleys_df.to_excel('raleys_data.xlsx', index = False)
