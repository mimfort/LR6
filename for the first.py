#import requests

cookies = {
    '_ga': 'GA1.1.160932825.1728847457',
    'accessToken': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUxNTczMDQ3In0.eyJfaWQiOiI2NjdlOTZlMzUzZjQ1NDAwMTJkZDhlMGUiLCJ0ZWxlZ3JhbUlkIjoiNTM5OTc0NzcyMiIsInVzZXJOYW1lIjoibmVsb2gwNzQiLCJhZGRyZXNzIjoiMHhjZDliMWY4M2YyZDUwNzllMzU0MjBjNzdjY2RiNDVhM2Q0MmVjZjExIiwiY3JlYXRlZEF0IjoiMjAyNC0wNi0yOFQxMDo1NjozNS43NTFaIiwidXBkYXRlZEF0IjoiMjAyNC0xMC0xM1QxOTozNjo0OS4zNjlaIiwiX192IjowLCJ0b25BZGRyZXNzIjoiMDpiZDMzZTkzMzI4OWNlNTU5NTFlYTJhYmNhNGMxNWU4MjE5YWQ1NWExZTE5ZjhkMjM1YzRkMjZlZmFjZTk5N2JhIiwiaWF0IjoxNzI4ODQ4NDUxLCJleHAiOjE3Mjg4NTIwNTEsImlzcyI6InRvbnN0YXRpb24ifQ.tLxxP9um_87rZpmY_16oRVBjF0yvWQR5HNw9KR9T5aAOBVjFm-yNOlo1PjmctPFxK689RN8Kr63hix0uSZvXBRaYiqqluDAHuNCrwnlMBKDFBrEiomzO1IxZLRFfq2OUquSGEf2x_s17Jghsk8attCP0hTnJ3eG3Ab1qjzVQ8aV-qoLYmusw4g8jQxaEaKgADKmCh_pt7ODtfEphk0foY4D1TmcC4S6KB4-4wPCm0x9Eh_qyk32iJQDLjak7X_w9aZP3LUH-mPN6YLX9dHYtfCoaE5hV4xztj9pMPo8e1cbINa_OFX9DEstWXMo4kE60dbkeekGtc1PqQmiYIy24XIep2XpZRvyCmTuds_2Xfe--wMh6ZprxH1Hi-3VwVovQdOflAzAdQ3wqzmIaCuNQBChk1pbW3eJQSHaFRYQ1ax_D3S-7t5KXv2UqQH8IbcGzfv7G6xa8UNAYfLR2vPXstp0y4ZRm25QIBrlesJjwhMgQUebAAVj3FEsNf-1fabOuUgPjAeazjxek50nrItHnuf1T8NivynYbkl7LMhIZf1Ghcd_2rn1ySkM985odnx7ZmsZcUrslu4Z6F3FujGSc9wlvWpzs5pazJD9BUb8KsVUNyRdGcy1Nld1b-99uLRNzs0NHLSceaDWBg5Vo9e1OI1SpkFKl8om73G5m2tGPqkM',
    'refresh_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUxNTczMDQ3In0.eyJ0ZWxlZ3JhbUlkIjoiNTM5OTc0NzcyMiIsImlhdCI6MTcyODg0ODQ1MSwiZXhwIjoxNzI4OTM0ODUxLCJpc3MiOiJ0b25zdGF0aW9uIn0.PBzfERNHDo56jV89coyb6qCYmYbfDXbGGU7cGMWUIJjeoXXsyHH3pO8L1g9JHv7iwh67lOEOyDb3-7sJOqt_EMzqcGU-X390dpb22PUBs2cvWiYls5aS81IPVrF28ydrrV6_W3PtChsZeUN3PxrGHwvPf0ffNDjAN3N817qISIieoCKxuS8jIzXL6AOw2Np6xutmEw-2bVimKz9OZE9kJwldtkpW11Q20zdUrGXHpVtebMy-4tZjgSGrApDrZjMJQO2Zn-l65rOxAheWNcmsZeBIRVvqmfFMwLoeBjQrijSOR2BlGiH0tjK6c4LnH5e5GxATEYzBuQ258y7rxC4BR3YrSULuThGjM2K6qHWBle_VldPWVHgzdcVOk59KoQqOS2r8JDSfKTfsLrqXtLcs3Hg3ODdaD-k2HaWXkhB9tdkp5QZl2TV9Chig4KEAbmCPZTL2YuY2LPMapkxGho7b10vFwLNeLaUbNmZxXtFmeMconJOeR_KNE9yF_7SeUrEyjkisQ-l8f8k9V5saUNoib-E77Rn5gnhKAVck-0QmfLGjdJy7yNSsnM6Fo9mm8zMJb4laS_U5NxCZrmc9wrwhi-j4yYxIGM4LTMaixyl8YI5-miT_yj-Vcqn4z7StA_hkTI4xT7GpJL-LvZkYcD1MXkWX8ZQyOuF5tV-FLGaJ-rY',
    '_ga_TDW94HCJN6': 'GS1.1.1728847456.1.1.1728848459.52.1.1939804033',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.160932825.1728847457; accessToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUxNTczMDQ3In0.eyJfaWQiOiI2NjdlOTZlMzUzZjQ1NDAwMTJkZDhlMGUiLCJ0ZWxlZ3JhbUlkIjoiNTM5OTc0NzcyMiIsInVzZXJOYW1lIjoibmVsb2gwNzQiLCJhZGRyZXNzIjoiMHhjZDliMWY4M2YyZDUwNzllMzU0MjBjNzdjY2RiNDVhM2Q0MmVjZjExIiwiY3JlYXRlZEF0IjoiMjAyNC0wNi0yOFQxMDo1NjozNS43NTFaIiwidXBkYXRlZEF0IjoiMjAyNC0xMC0xM1QxOTozNjo0OS4zNjlaIiwiX192IjowLCJ0b25BZGRyZXNzIjoiMDpiZDMzZTkzMzI4OWNlNTU5NTFlYTJhYmNhNGMxNWU4MjE5YWQ1NWExZTE5ZjhkMjM1YzRkMjZlZmFjZTk5N2JhIiwiaWF0IjoxNzI4ODQ4NDUxLCJleHAiOjE3Mjg4NTIwNTEsImlzcyI6InRvbnN0YXRpb24ifQ.tLxxP9um_87rZpmY_16oRVBjF0yvWQR5HNw9KR9T5aAOBVjFm-yNOlo1PjmctPFxK689RN8Kr63hix0uSZvXBRaYiqqluDAHuNCrwnlMBKDFBrEiomzO1IxZLRFfq2OUquSGEf2x_s17Jghsk8attCP0hTnJ3eG3Ab1qjzVQ8aV-qoLYmusw4g8jQxaEaKgADKmCh_pt7ODtfEphk0foY4D1TmcC4S6KB4-4wPCm0x9Eh_qyk32iJQDLjak7X_w9aZP3LUH-mPN6YLX9dHYtfCoaE5hV4xztj9pMPo8e1cbINa_OFX9DEstWXMo4kE60dbkeekGtc1PqQmiYIy24XIep2XpZRvyCmTuds_2Xfe--wMh6ZprxH1Hi-3VwVovQdOflAzAdQ3wqzmIaCuNQBChk1pbW3eJQSHaFRYQ1ax_D3S-7t5KXv2UqQH8IbcGzfv7G6xa8UNAYfLR2vPXstp0y4ZRm25QIBrlesJjwhMgQUebAAVj3FEsNf-1fabOuUgPjAeazjxek50nrItHnuf1T8NivynYbkl7LMhIZf1Ghcd_2rn1ySkM985odnx7ZmsZcUrslu4Z6F3FujGSc9wlvWpzs5pazJD9BUb8KsVUNyRdGcy1Nld1b-99uLRNzs0NHLSceaDWBg5Vo9e1OI1SpkFKl8om73G5m2tGPqkM; refresh_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUxNTczMDQ3In0.eyJ0ZWxlZ3JhbUlkIjoiNTM5OTc0NzcyMiIsImlhdCI6MTcyODg0ODQ1MSwiZXhwIjoxNzI4OTM0ODUxLCJpc3MiOiJ0b25zdGF0aW9uIn0.PBzfERNHDo56jV89coyb6qCYmYbfDXbGGU7cGMWUIJjeoXXsyHH3pO8L1g9JHv7iwh67lOEOyDb3-7sJOqt_EMzqcGU-X390dpb22PUBs2cvWiYls5aS81IPVrF28ydrrV6_W3PtChsZeUN3PxrGHwvPf0ffNDjAN3N817qISIieoCKxuS8jIzXL6AOw2Np6xutmEw-2bVimKz9OZE9kJwldtkpW11Q20zdUrGXHpVtebMy-4tZjgSGrApDrZjMJQO2Zn-l65rOxAheWNcmsZeBIRVvqmfFMwLoeBjQrijSOR2BlGiH0tjK6c4LnH5e5GxATEYzBuQ258y7rxC4BR3YrSULuThGjM2K6qHWBle_VldPWVHgzdcVOk59KoQqOS2r8JDSfKTfsLrqXtLcs3Hg3ODdaD-k2HaWXkhB9tdkp5QZl2TV9Chig4KEAbmCPZTL2YuY2LPMapkxGho7b10vFwLNeLaUbNmZxXtFmeMconJOeR_KNE9yF_7SeUrEyjkisQ-l8f8k9V5saUNoib-E77Rn5gnhKAVck-0QmfLGjdJy7yNSsnM6Fo9mm8zMJb4laS_U5NxCZrmc9wrwhi-j4yYxIGM4LTMaixyl8YI5-miT_yj-Vcqn4z7StA_hkTI4xT7GpJL-LvZkYcD1MXkWX8ZQyOuF5tV-FLGaJ-rY; _ga_TDW94HCJN6=GS1.1.1728847456.1.1.1728848459.52.1.1939804033',
    'origin': 'https://tonstation.app',
    'priority': 'u=1, i',
    'referer': 'https://tonstation.app/app/?tgWebAppStartParam=ref_public',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'initData': 'user=%7B%22id%22%3A5399747722%2C%22first_name%22%3A%22074_neloh%F0%9F%86%93durov%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22neloh074%22%2C%22language_code%22%3A%22ru%22%2C%22is_premium%22%3Atrue%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=5378485468735948456&chat_type=sender&start_param=ref_public&auth_date=1728847268&hash=5c32ffc53f15b758b5521d7631008abc53b5d469be3538c59968c6b63b72faee',
}

response = requests.post('https://tonstation.app/userprofile/api/v1/users/auth',  headers=headers, json=json_data)
print(response.json())
