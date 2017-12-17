import urllib

import requests


def testcoo():
    session = requests.Session()
    r1 = session.post('https://www.saavn.com/api.php?__call=user.login&_marker=0',
                      data={'username': 'rishabhnahil9264@mailinator.com', 'password': 'qwerty123', '(empty)': '',
                            'ct': '1646993133'})
    r = session.get(
        'https://www.saavn.com/p/playlist/0a7902f7c97de340759e91d2e8dcdd37/SaavnXBali/n8izEubmAJwwkg5tVhI3fw__')
    r2 = session.get(
        'https://www.saavn.com/api.php?__call=social.follow&_format=json&_marker=0&entity_id=111241563&type=playlist&ct=1646993133',
        cookies=r1.cookies.get_dict())
    print(r.cookies.get_dict())
    print(r1.cookies.get_dict())
    print(r2.text)


def get_cookie():
    file = open('data.txt', 'r')
    content = file.readlines()

    for values in content:
        con_array = values.split('|')
        email = con_array[2][:-1]
        print(email)
        url1 = "https://www.saavn.com/api.php"

        querystring1 = {"__call": "user.login", "_marker": "0"}
        # print urllib.urlencode(email)
        payload1 = "username=" + email + "&password=qwerty123&(empty)=&ct=1646993133"
        # print payload1
        headers1 = {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.8",
            'connection': "keep-alive",
            'content-length': "76",
            'content-type': "application/x-www-form-urlencoded",
            'host': "www.saavn.com",
            'origin': "https://www.saavn.com",
            'referer': "https://www.saavn.com/login.php?action=login",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url1, data=payload1, headers=headers1, params=querystring1)
        cookies_array = response.cookies.get_dict()
        print(cookies_array)
        url = "https://www.saavn.com/api.php"

        querystring = {"__call": "social.follow", "_format": "json", "_marker": "0", "entity_id": "111241563",
                       "type": "playlist", "ct": "1646993133"}
        print(urllib.unquote(cookies_array['B']).decode('utf8'))
        headers = {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.8",
            'connection': "keep-alive",
            'cookie': "B=" + urllib.unquote(cookies_array['B']).decode('utf8') + "; CT=" + urllib.unquote(
                cookies_array['CT']).decode('utf8') + "; CH=" + urllib.unquote(cookies_array['CH']).decode(
                'utf8') + "; I=" + cookies_array[
                          'I'] + "; app_install_banner=shown; geo=180.151.118.219%2CIN%2CKarnataka%2CBengaluru%2C; L=hindi; _fp=3f48514e3f11e6659eeb7a099f04c888; ATC=m3JU%2Fd0UC2y7scO8otprefiuDxmsZ1tVxVVBu7aMsIwcgBzUTXsqaKg%2B6gIjQVMm; __utmt=1; __gads=ID=27c3dfdcc1e69fa4:T=1503251196:S=ALNI_MZp4lyzNHrkbE39vTUq21gZysdqqw; jwplayer.volume=75; MyRT=; __utma=257722889.1877295748.1503242772.1503242772.1503251195.2; __utmb=257722889.9.10.1503251195; __utmc=257722889; __utmz=257722889.1503251195.2.2.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/UnK0ThBmbV",
            'host': "www.saavn.com",
            'referer': "https://www.saavn.com/p/playlist/0a7902f7c97de340759e91d2e8dcdd37/SaavnXBali/n8izEubmAJwwkg5tVhI3fw__",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
            'cache-control': "no-cache"
        }
        # print headers
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)


# get_cookie()
testcoo()
