import requests
import datetime
import json 
import util

headers = {
    'authority': 'api.myturn.ca.gov',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'x-correlation-id': '4ab64ad8-d8f2-48d0-ade6-2948eb2c40f1',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://myturn.ca.gov',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://myturn.ca.gov/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ak_bmsc=AA21DCBACD789358A91A782BB3DC0897B81A3596AA0C000078DC566030ED3F2D~plORokuOH2QP6pCZdj/HeSj/aJnN02REbYSoCQm65Ht4VRJgaowdigXpZOFg+Vbv98fuoq2gKzVPSJgNx3mpWZe5XN0WNPNqIQ3clbQVPRThkvrRE4MXw6v0KGStwyF/MOCl896aY3Y4HFjNYXQ1hzQpf7QRepVQTOKyHn7DLSMPpOf4DkNQIA1svQQIcd+7lLu8fooOtLKtQBRlOiXgo1QWQwtFEgLaXKtoAqmenbHiM=; bm_sz=C10C5844430CF5D87F55D8BCA87F1DDE~YAAQljUauFsdjD54AQAAMDZNUwt6L6ZfkYVdu5T8Tqw4iL4yLg4eIoBKExQHaZJPud8EidpbUgAw0NBxrAIcc7mnEmC4Pehri+/0XgXRGsqh1/fUw63rUwQGqnGe5Cw+bEfmkTZC2zhKJZxEqrvTg3BdlNLg1e1s+5HZEdM6iXdyM/A2o7NwgHTIVU0=; _abck=D23E885F7FE01A22F0D76138743F471F~0~YAAQljUauFwdjD54AQAAMDZNUwXW297KHLEg7W3RS2JtXbpiT0hbsCBRAGpHMWciqxzCAQjyNX+ByVIDlXzlRdRqvxtcJcLonBuAzui+UXGwzL5UMElNCcCmjz6nnqxPQr0TaE2Lbh373LPmCwwIDmrzrm/Tn4lvfp2j2eIiql4PekOnB1M77ds8c0ne70vZmDlSMp8LtvE9pSOaXee8s5Y13yy6sg5KhnKSOv4dGfrmKeMMGjPcPtPpYF6t3O7LpOI31jtMOzuIkb3bgdBfrOu4BDVzewJzXeE+dky4UxWXh0debtFsSy63NFjTHAKcotEJTK6Qa3tFxPulhPNUHaRHFFrtbYAyoUNQIgSvfMPQ0XykZAYacU6d8XM+fjsKfoTw3W1rBJk8kXrY6uqrc6iCmNk=~-1~-1~-1; bm_sv=42296B8CF44E5FD0AD8710E82205D0DF~aIXrFAy1m7Qye8+8vyUyjP2Qfg1x/bW9oCECSWfip5qmhisQ0jwMNWmV3oW+EykDkiVkWxqFGieRkrGxUmCltaTMRT9eSwjvJOsn+Inp/bJubKNqbgHwt7bpPuYUTIIwGjV8H2xVdRiPSA2NVj12LA==',
}

startdate = str(datetime.datetime.now().date())
enddate = str(datetime.datetime.now().date() + datetime.timedelta(days=10))
data = {
  "startDate":"{}".format(startdate),
  "endDate":"{}".format(enddate),
  "vaccineData":"WyJhM3F0MDAwMDAwMDFBZExBQVUiXQ==",
  "doseNumber":1,
  "url":"https://myturn.ca.gov/appointment-select"
}
RESEND_WINDOW = 60 * 60 * 3

last_sent_time = {"myturn": None}

def should_send_text(date):
    if date not in last_sent_time:
        return True
    return (datetime.datetime.now() - last_sent_time[date]).seconds > RESEND_WINDOW

def check_myturn():
    print("Checking MyTurn @ {}".format(datetime.datetime.now()))
    response = requests.post('https://api.myturn.ca.gov/public/locations/a2ut0000006eUhiAAE/availability', headers=headers, data=json.dumps(data)).json()
    
    for date in response["availability"]:
        if date["available"] and should_send_text(date["date"]):
            last_sent_time[date["date"]] = datetime.datetime.now()

            text = "{} has a vaccine available on this date: {}".format("San Francisco (Moscone Center)", date["date"])
            link = "https://myturn.ca.gov/appointment-select"
            text += "\n {}".format(link)
            util.send_msg(text, "San Francisco", "Moscone Center", link)
