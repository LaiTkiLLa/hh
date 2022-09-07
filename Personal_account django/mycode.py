import requests
import csv

def send_sms():

    url = 'https://solber.ru/api/me/loginSendCodeSms'
    data = { "PHONE": '+7 (968) 9414200',
            "TYPE": "driver"
            }
    res = requests.post(url=url, data=data)

# send_sms()

def get_api():

    url_code = 'https://solber.ru/api/me/loginByCodeSms'
    data = {
              "CODE": '93778',
              "PHONE": '+7 (968) 9414200'
            }

    res_api = requests.post(url=url_code, data=data)
    status = res_api.status_code
    api_key = res_api.json()['Apikey']
    return api_key

# print(get_api())

def auth():
    url_auth = 'https://solber.ru/api/driver/shipping'
    headers = {'Apikey': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJRCI6IjY2MCIsIkxPR0lOIjoiNzk2ODk0MTQyMDAiLCJpYXQiOjE2NTc1MjY5NTQsImV4cCI6MTY2NTMwMjk1NH0.R5iKRhVs1gclWOZ3A0DX108tDyyK8UwIV0kXM5RddNo'}
    res_auth = requests.get(url=url_auth, headers=headers)
    # with open('C:\\Users\\f.burov\PycharmProjects\BOOTSTRAP2\\datas.csv', 'w') as file:
    #     file.write(res_auth.text)
    i = 0
    for i in range(i, len(res_auth.json()['ITEMS'])):
        print(requests.get(url=url_auth, headers=headers).json()['ITEMS'][i]['NUMBER'])


print(auth())