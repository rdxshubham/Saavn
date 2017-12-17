import requests, random


# https://www.saavn.com/api.php?__call=user.createV2

def account_maker(firstname, lastname, mail_id):


    url = "https://www.saavn.com/api.php"

    querystring = {"__call": "user.createV2"}

    payload = "_marker=0&username=" + mail_id + "&email=" + mail_id + "&password=qwerty123&(empty)=&ct=1608730414"
    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'connection': "keep-alive",
        'content-length': "110",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "geo=42.109.218.217%2CIN%2CKarnataka%2CBengaluru%2C; B=fc34fd98201f6df9a92734da7862e37d; CT=MTYwODc1NTE4Mw==; CH=G03%2CA07%2CO00%2CL03; __utmt=1; __utma=257722889.1877295748.1503242772.1503242772.1503242772.1; __utmb=257722889.4.10.1503242772; __utmc=257722889; __utmz=257722889.1503242772.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); MyRT=",
        'host': "www.saavn.com",
        'origin': "https://www.saavn.com",
        'referer': "https://www.saavn.com/login.php?action=create",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'cache-control': "no-cache",
        'postman-token': "7d71ae60-a9d7-ef8f-c5d2-3213e0807843"
    }
    file = open('data.txt', 'a')
    file.write(firstname + "|" + lastname + "|" + mail_id + "\n")
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


firstname_list = ['Shubham', 'Rishabh', 'Sumanyu', 'Soubhik', 'Vikas', 'Avinash', 'Bishal', 'Subhash', 'Aman', 'Aditya',
                  'Sahil', 'Sushil', 'Rajeev', 'Ravi']
lastname_list = ['Gupta', 'Nahil', 'Soniwal', 'Sharma', 'Handa', 'Topani', 'Roy', 'Hardaha', 'Saini', 'Gupta', 'Maggu',
                 'Sanjiv', 'Jatt', 'Jain']

while 1:
    index = random.randrange(0, 14)
    firstname = firstname_list[index]
    lastname = lastname_list[index]
    mail_id = firstname.lower() + lastname.lower() + str(random.randrange(1111, 9999)) + '@mailinator.com'
    account_maker(firstname, lastname, mail_id)
