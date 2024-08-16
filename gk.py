import requests
import random

while True:
    user = "".join(random.choice("qwert_yuio_pasdf_ghjk_lz_xcvb_nm12345_67890") for i in range(5))

    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=Z6e1_3JppHnIcecp_59tws; dpr=1.75; mid=Zr6YvAABAAG8fP97KJqvzukxrL8D; datr=vJi-ZsHRcX-SI48EoUQmruOm; ig_did=14B73A65-0ED7-45A8-A617-E6402B714A2E; ig_nrcb=1; wd=1143x113',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '"ELN-W09"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"13.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-csrftoken': 'Z6e1_3JppHnIcecp_59tws',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1015718097',
        'x-requested-with': 'XMLHttpRequest',
        'x-web-device-id': '14B73A65-0ED7-45A8-A617-E6402B714A2E',
    }

    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1723767118:AcNQAOTwcUCe9vN7DR16W9/AC4lT7n0NZ+/Nd/Ezp+UCqQoykvLi4IGJI+tdhg7Bt0RPciMGOSCoZSrIpHlSnibr8YyPCAEjgHe8BKku0B3BE4tAgYHwLiYzUU9TQVqkB5bTZuUCeVh8CuAGLQw=',
        'email': 'zodhokmgmgm4374gm@gmail.com',
        'first_name': 'zaid47rali',

        'username': user,

        'opt_into_one_tap': 'false',
    }

    res = requests.post(url, headers=headers, data=data).text

    if '"dryrun_passed":true,' in res:
        print(f"Username Good : {user}")

    else:
        print(f"Username Badd : {user}")
        print(res)
