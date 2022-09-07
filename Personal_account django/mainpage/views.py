from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.views.generic import View
from django.shortcuts import redirect


def new_page(request):
    return render(request,"mainpage/job.html")

def solo(request):
    return render(request, 'mainpage/solo.html')

def lk(request):
    url_auth = 'https://solber.ru/api/driver/shipping'
    headers = {'Apikey': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJRCI6IjY2MCIsIkxPR0lOIjoiNzk2ODk0MTQyMDAiLCJpYXQiOjE2NTc1MjY5NTQsImV4cCI6MTY2NTMwMjk1NH0.R5iKRhVs1gclWOZ3A0DX108tDyyK8UwIV0kXM5RddNo'}
    res_auth = requests.get(url=url_auth, headers=headers).json()['ITEMS']
    return render(request,'mainpage/lk.html',{'response':res_auth})
    # i = 0
    # res_auth = requests.get(url=url_auth, headers=headers)
    # for i in range(i, len(res_auth.json()['ITEMS'])):
    #    return render(request,'mainpage/lk.html', {'response':res_auth})

def send_sms(request):

    if request.method == "GET":
        return render(request, "mainpage/index.html")
    if request.method == "POST":
        my_phone = request.POST.get('telephone', False)
        request.session['telephone'] = my_phone
        url = 'https://solber.ru/api/me/loginSendCodeSms'
        data = { "PHONE": my_phone,
                "TYPE": "driver"
                }
        res = requests.post(url=url, data=data)

        return redirect("/code")

def get_api(request):

    if request.method == "GET":
        return render(request, "mainpage/code_sms.html")
    if request.method == "POST":
        my_sms = request.POST.get('sms', False)
    mobile = request.session['telephone']

    url_code = 'https://solber.ru/api/me/loginByCodeSms'
    data = {
              "CODE": my_sms,
              "PHONE": mobile
            }

    res_api = requests.post(url=url_code, data=data)
    status = res_api.status_code
    api_key = res_api.json()['Apikey']

    if status == 200:
        url_auth = 'https://solber.ru/api/driver/shipping'
        headers = {'Apikey': api_key}
        res_auth = requests.get(url=url_auth, headers=headers)
        return redirect("/my_cabinet")
    else:
        return redirect('/test')



