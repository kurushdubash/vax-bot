import requests
from datetime import datetime
import util

cookies = {
    'USER_LOC': '2%2BsKJSc9HtLIBK6tQMVIpTufCKUgUi6APmrftRJdC69BfBetdGRYxijceCJLpGDs',
    'liveagent_oref': 'https://www.walgreens.com/login.jsp',
    'liveagent_ptid': '35c475fc-9c37-4c25-a060-fe2b33483c70',
    'cm.BgPHTQB9cCaVB9ptUaBYnv0k.B9cCaV5ohacctlog': '1615824515',
    'Adaptive': 'true',
    'liveagent_vc': '4',
    'FirstName': 'Kurush',
    '3s': 'dsSJXcW+MMWNxaTDvMWUxLAywrs=',
    'meHshId': 'hVJDRz9sBz3Sg+JurOrv+trRvpWGuAh7lXxQkhxT2eg=',
    'cm.BgQrL-B9bKQHB9zfIXAPjcY0.B9bKQHjWhhero': '1615825358',
    'ak_bmsc': 'F68243FBAFC804797EF1AEA6388C357E17C5330465290000253955606661DF34~pl9EoXEARbJXecWq0MxrRQw0LXNtIFD3zMsCAV4jJ1sdvgcqjVFyeymDYNr1ljUhYTpF9R8EsKD0dAHrpx6n5Q/NMwDb2mErRX+RSqvM2UkZ1fenuMIlm+PtEke4qqKyEqaYdaqeMHYlDbviIp9p5VpN7Kws3GT864OZDJSTvBi+a7GIaogwuuZv6dvEAHRhHzmztjFjPv5q9DqGvpa3xlIkTDd3Ao6Z6x0WaZ7t0mZZQ=',
    'bm_sz': '45887EC44AC7C9F25004382A4BF494CA~YAAQBDPFF3q76jx4AQAA0TvnTAsYjb/Z3swxhOKNofs3KlISUXpulZCXhGAqtWvIsGo/9m8cub/66rTVipnctU38cFAkaRsiOZypGy3+xWgZL4Av8rLZFlnA+c4qveuisiFpHLcBSLW7M/zOuJBbNbdJZ4nDOuoyVOdm7ynsKmyrP5GnljnPARkIvXHSiFenHB17',
    'wag_sid': '292iwgdnzb6yhofx3xmdnaos',
    'uts': '1616197926334',
    'at_check': 'true',
    'XSRF-TOKEN': 'adpzdN7tgLco3w==.BkNQNWNNswaWUyHYFhTe/ZWk2dkBFuxbvgzr93nMA3I=',
    'session_id': 'a245b749-dc34-49c0-9fa8-4845dc747917',
    'dtCookie': '3$9E7790E2BCDCE7C33EAA6B48888B9522|0eed2717dafcc06d|1',
    'AMCVS_5E16123F5245B2970A490D45%40AdobeOrg': '1',
    'gRxAlDis': 'N',
    'mbox': 'PC#a88d1c15e0354b9d9ef73bd0a8940f8c.35_0#1679442728|session#5211f425083542a0abf81b8b0fe8455a#1616199787',
    'bm_mi': '1B6EA6BC1DCC80C03418CEC7B37A7BDC~MWahbcSPNVykrcceShH1dk1xTfMrgmFcjh0Z1Z/q0ks6OJPEGXf6PY5AaI7vZBqvgM41tK0GI9JkBLhRIf+uCFCd/28iefRCr9XqMrVzZkshpSuIHrHZeSNGWlt6P4/Xb5G8lz38G75vFzKz+2JeEWfMplhoYNz7gj2xlWy3bQ5rP6aG7kKp/Rea9M7SoCJ0ZR19ozGFPHsVRbtPNX0CS2h6GbbQbxkCzWq6QsQVMdzXzgY9oOOzg2RvcAtlKq17WhgRa2BHhtnnbM52+r8qNw==',
    'fc_vnum': '3',
    'fc_vexp': 'true',
    'firstVisit': 'fc_fVisit',
    'AMCV_5E16123F5245B2970A490D45%40AdobeOrg': '-1124106680%7CMCIDTS%7C18706%7CMCMID%7C54534039545645161936131838830965741612%7CMCOPTOUT-1616205131s%7CNONE%7CvVersion%7C5.2.0%7CMCAID%7CNONE',
    'bm_sv': '293950D27AA4CB1970BA35F5C07A267D~xqUA0xUzLqYpvd5gAVoYbO6+Hz1q1sA+1t6crOA/HZIw4Gz4d/z2eCfKB1itTxstfrCD6MMCISyn6gTl02+t4DT15/W91oY4YwG2/O/UYkpjnMYZxwLFkUpWxJbX/v/OzdSYK05/MV78sqFzezMjoPmd0Zf5L04pLNYp2qy5FpU=',
    'akavpau_walgreens': '1616198614~id=c1b9279e2a952a448b7b010685ed8c81',
    '_abck': '6F73BEEB317C48D0682BB33043CA3909~0~YAAQDTPFF24aykV4AQAA5yvtTAWCi5YLWDykY+K167TcJpyB495h0+uKJ37dN8V7aMz0iZ4afa/6TE+tE4w+KnJduuOLB3EpWFL38mH7tiFR633rMzbIdZYn4O7cKkGGrCTcr2tMG4tIyUpki6svI2uYtkJ4IBDdS8s87F4UMbrfzyoBelPsqaffoR090klhZolWUgfmgKQ1ZmnrjwlSMgqaPmedbvtFxd3805XUpS47a7bpws4QureuY+KWP6LnW60/lMOe6PVcnce1ffVx5fnwOGyG9BA/xLeSAEBYiEA9Y7C1JvWW/uuHtP9m4i2RxLF30J1io4LYalwP8WPeJ3sYRApfeGha+EDrDdooP47T+4TLOSMlf8Hyp0QYKGTAX7wzahY/PefpLeblHBGr57OPht2seNNbATH/~-1~-1~-1',
}

headers = {
    'authority': 'www.walgreens.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'x-xsrf-token': 'StZadBK5Ddc64A==.o7nv9P4HKOytTHpSLpTHQtYJ6BY+t2sXx3aCahAdk8s=',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.walgreens.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening',
    'accept-language': 'en-US,en;q=0.9',
}

data = '{"serviceId":"99","position":{"latitude":37.72254909999999,"longitude":-122.4410618},"appointmentAvailability":{"startDateTime":"' + str(datetime.now().date()) + '"},"radius":25}'

WALGREENS_RESOURCE = "https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability"
RESEND_WINDOW = 60 * 60 * 3

last_sent_time = {"Wallgreens": None}

def should_send_text_for_city():
    if last_sent_time["Wallgreens"] == None:
        return True
    return (datetime.now() - last_sent_time["Wallgreens"]).seconds > RESEND_WINDOW

def check_walgreens():
    print("Checking Walgreens @ {}".format(datetime.now()))
    response = requests.post(WALGREENS_RESOURCE, headers=headers, cookies=cookies, data=data).json()
    if response["appointmentsAvailable"] and should_send_text_for_city():
        last_sent_time["Wallgreens"] = datetime.now()
        util.send_text("San Francisco", "Wallgreens", "https://www.walgreens.com/findcare/vaccination/covid-19/appointment/next-available")
