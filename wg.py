import requests
from datetime import datetime
import util

cookies = {
    'USER_LOC': '2%2BsKJSc9HtLIBK6tQMVIpTufCKUgUi6APmrftRJdC69BfBetdGRYxijceCJLpGDs',
    'liveagent_oref': 'https://www.walgreens.com/login.jsp',
    'liveagent_ptid': '35c475fc-9c37-4c25-a060-fe2b33483c70',
    'cm.BgPHTQB9cCaVB9ptUaBYnv0k.B9cCaV5ohacctlog': '1615824515',
    'cm.BgQrL-B9bKQHB9zfIXAPjcY0.B9bKQHjWhhero': '1615825358',
    'liveagent_vc': '6',
    '3s': 'xaHDj8SXZV3FvnfCvsSNxYDDqWQ=',
    'FirstName': 'Kurush',
    'cm.BgVLDpB9cCaVB93WsFBYnv0k.B9cCaVGThform': '1616373367',
    'cm.BgVLDqB9cCaVB938SABYnv0k.B9cCaVO5hpdf': '1616566496',
    'cm.BgVLDqB9cCaVB938SABYnv0k.B9cCaVO5hform': '1616566510',
    'ak_bmsc': '064ECE7C661ADC958EB428DD101642191735221CF92D000018246D6000A7F614~pl3ThCr2JtaI6DE1zq6iidXvtSqR3WBP3LzVhAyiMeSP4YK3Ie4et0cgEPFgDgtHPp/XkqIPGvQy5iqmyjwzVRicJruN6vxRaqBAzKmuruTH+tEF/7UShaFSYrDJ4ogGRQZdn/LPDY4yQc1PNb0aUMCW5Mzvof8/3LL51pPK8sAkRTh3N1hJQPWgoWHSeWs1usWpf+Bva67gG3VgmqS9zuT6nbazKyIF8XNF/3ob00Y8c=',
    'bm_sz': 'AC1D92EA0B4BC135DF5006F3D73A9184~YAAQHCI1F2OxwIF4AQAAPf5UqgvlIFzFLeNZNGxREBkPmrfcNM84h8XDIFZTIvVMrq5SjHnWeYT7kX4YveNkUOG9+IdmXwoOezem1ccptlD4wxI9zl71mO9lHC8WU78iJ64eEFqFM2VyjOrgYQfmw/vpjcOXR8nN3dXwSw1nheTl/Fahm51YhrotEbmelM3Ju3+A',
    'wag_sid': '9dvo2kupwbmkgmtjxmgqwjjw',
    'uts': '1617765401852',
    'at_check': 'true',
    'XSRF-TOKEN': 'FXIBz5aA0mzHOQ==.tiRB+kt5CRbMsXeGiSixZcyEMagyZvoG/zPXlS/JtFk=',
    'session_id': '178ff0f4-8669-4fec-9e2a-837557a5389e',
    'dtCookie': "3$6476286F7449BD53BCA740894F85D229|0eed2717dafcc06d|1",
    'AMCVS_5E16123F5245B2970A490D45%40AdobeOrg': '1',
    'gRxAlDis': 'N',
    'mbox': 'PC#a88d1c15e0354b9d9ef73bd0a8940f8c.35_0#1681010205|session#3e90dbf007d04340821bd784fa764102#1617767263',
    'bm_mi': '5D4462C723DB79091BFE9C0F30D2F93C~smev43MX7cNHqwEi/5eKARc0SKFfJ2x3dOu3U2biYXOSOCz9+rbZNU32hr07BXaxZCk9c+CQyKZQ7kAG6iYlLbav5qa6xJu8MyeXktGDTWIux6YIFoZi1LgS7f8eBy+FLk4T2a9dfpwM/NF4VSmT6rKGvpZ6fRWekvkpESal0753mNFE4mYXsyNmG/212BmQxEF/IHlaXOs7I6sxIovVmeCNQfpx6aCL1c6d4fSGd8b41cttLn3OavgagwF05UcMUCVfCwBdHQGh3YLM6YNRSA==',
    'fc_vnum': '10',
    'fc_vexp': 'true',
    'firstVisit': 'fc_fVisit',
    '_abck': '6F73BEEB317C48D0682BB33043CA3909~0~YAAQHCI1FwOywIF4AQAAzCVVqgX10S39lnk5X/R0aoUJfvULJQpnOaenJGpQOoc3hpUaMCMtJCi8yB6OlqrCNTlGjqM/gHcOoFarmyH9a/N93YuZbprtuDzWPyKiPCVyYScmSGDvzDC2PEsy3SHJFZd13/O7kUXHZOC6Jz7yJB/WvnxK76dPhBCsHxdz1jjWfzr0OSauZXyDzGItrguR7vF8A4/3FyPQNHSBwSIlYx2eA9PoFY0jqeYbdLKxWoebiLeSu9DVqcY+brK239k8KXT1+loIOw8//L60cbRkhAbDWzmBJ4fsOUljG9MrGSKxoC4tiL/Vc2dEDVhu4Vp3vD1KSlFRTsGXyXMGVxqXBOIoIfs2NN06L7beO036I+98MclDb47B85/N06LVwnz2IhxfLPfmX/3ftUYP~-1~-1~-1',
    'AMCV_5E16123F5245B2970A490D45%40AdobeOrg': '-1124106680%7CMCIDTS%7C18725%7CMCMID%7C54534039545645161936131838830965741612%7CMCOPTOUT-1617772612s%7CNONE%7CvVersion%7C5.2.0%7CMCAID%7CNONE',
    'akavpau_walgreens': '1617765714~id=85d1cd568d689191f1078dfe3a551cdf',
    'bm_sv': '664CBE3D36F23DD83AA485A775235089~cSghoN6N4cZFxoYzDjlTrHboZxrNyOPU5w7XOg5QNS5Md5oKMNGMQK8NBTrUfxBWBt32GuO1y2QdWAkIAqSkO06OdezkfNp6pHL900QaeONZLfJAlk8BGfxysTYopS9LN53G3oD09DPLqO2I4r5h6Qw/DuTA91oSX5788l4CahM=',
}

headers = {
    'authority': 'www.walgreens.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'x-xsrf-token': 'CPIhJaZg6XdbfA==.wYFHyR7JCtcilAk5sKHvUdqnlj4UGCwm0Xo60OV5j8s=',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.walgreens.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening',
    'accept-language': 'en-US,en;q=0.9',
}

data = '{"serviceId":"99","position":{"latitude":37.7717185,"longitude":-122.4438929},"appointmentAvailability":{"startDateTime":"' + str(datetime.now().date()) + '"},"radius":25}'


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
