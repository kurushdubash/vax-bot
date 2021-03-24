import googlemaps
import requests
import util
import os
from datetime import datetime

api_key = os.environ['GMAPS_KEY']

gmaps = googlemaps.Client(key=api_key)

DISTANCE_IN_MINS = 25
DISTANCE_IN_SECS = DISTANCE_IN_MINS * 60
RESEND_WINDOW = 60 * 60 * 3
HOME_ADDRESS = "590 Steiner St., San Francisco, California, 94117"
CVS_RESOURCE = "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.CA.json"

cookies = {
	'pe': 'p1',
	'acctdel_v1': 'on',
	'adh_new_ps': 'on',
	'adh_ps_pickup': 'on',
	'adh_ps_refill': 'on',
	'buynow': 'off',
	'sab_displayads': 'on',
	'dashboard_v1': 'off',
	'db-show-allrx': 'on',
	'disable-app-dynamics': 'on',
	'disable-sac': 'on',
	'dpp_cdc': 'off',
	'dpp_drug_dir': 'off',
	'dpp_sft': 'off',
	'getcust_elastic': 'on',
	'echomeln6': 'off-p0',
	'enable_imz': 'on',
	'enable_imz_cvd': 'on',
	'enable_imz_reschedule_instore': 'on',
	'enable_imz_reschedule_clinic': 'off',
	'flipp2': 'on',
	'gbi_cvs_coupons': 'true',
	'ice-phr-offer': 'off',
	'v3redirecton': 'false',
	'mc_cloud_service': 'on',
	'mc_hl7': 'on',
	'mc_home_new': 'off2-p0',
	'mc_ui_ssr': 'off-p2',
	'mc_videovisit': 'on',
	'memberlite': 'on',
	'pauth_v1': 'on',
	'pivotal_forgot_password': 'off-p0',
	'pivotal_sso': 'off-p0',
	'pbmplaceorder': 'off',
	'pbmrxhistory': 'on',
	'ps': 'on',
	'refill_chkbox_remove': 'off-p0',
	'rxdanshownba': 'off',
	'rxdfixie': 'on',
	'rxd_bnr': 'on',
	'rxd_dot_bnr': 'on',
	'rxdpromo': 'on',
	'rxduan': 'on',
	'rxlite': 'on',
	'rxlitelob': 'off',
	'rxm': 'on',
	'rxm_phone_dob': 'off-p1',
	'rxm_demo_hide_LN': 'off',
	'rxm_phdob_hide_LN': 'on',
	'rxm_rx_challenge': 'off',
	's2c_akamaidigitizecoupon': 'on',
	's2c_beautyclub': 'off-p0',
	's2c_digitizecoupon': 'on',
	's2c_dmenrollment': 'off-p0',
	's2c_herotimer': 'off-p0',
	's2c_newcard': 'off-p0',
	's2c_papercoupon': 'on',
	's2c_persistEcCookie': 'on',
	's2c_rewardstrackerbctile': 'on',
	's2c_rewardstrackerbctenpercent': 'on',
	's2c_rewardstrackerqebtile': 'on',
	's2c_smsenrollment': 'on',
	's2cHero_lean6': 'on',
	'sft_mfr_new': 'on',
	'sftg': 'on',
	'show_exception_status': 'on',
	'v2-dash-redirection': 'on',
	'ak_bmsc': '980FC3BE26305EF55109F2CB306A879617C532F4FA4C000025EB54606F2FB11A~pl7xr8gx2GNg7bNP4N7m0qqRDYs9/HIDq6OwVUYCgvD73snZUvvPxEoC67+TYLCmsshPGGi+3BXx9lGucYklziHcP2pNDCalMZUcNgw08/SvN7Do9Zv2G85EQfsP/0mL9hEawRdEBJ0I5gE8i7C6i4P5jAZFitkFGyo4X1d4ut5ffr/mpBo1My6oQMjuQm+NrqgBSCHl36sI8V4pMZKxdTii+G/IuVdaJW+M/xYfzj3wg=',
	'bm_sz': 'E7DAEB56DED113468978D1AE71518D7E~YAAQ9DLFF9eJQUV4AQAAhoq2SwvSICVDEdQHx0WOYH+a/lvV0a5vgCoznMnZ8o9dWJI7WMQLCmrLWaT/FMpNs0TYXumwh85wirUCo49RZzxXGXBvsByxeI+s9FXWjhi+CWk4cKnlJIqEdLDQILxWl5E+Hm0Rev215hQzu8cnQfiXemw1yUwV44fWXnUv',
	'_group1': 'quantum',
	'utag_main': 'v_id:01784bb68bbb00333f6d53a3fc200307800320700093c$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1616179757819$ses_id:1616177957819%3Bexp-session',
	'AMCVS_06660D1556E030D17F000101%40AdobeOrg': '1',
	'AMCV_06660D1556E030D17F000101%40AdobeOrg': '-330454231%7CMCIDTS%7C18706%7CMCMID%7C82821780858528071327475076260460503151%7CMCAID%7CNONE%7CMCOPTOUT-1616185157s%7CNONE%7CvVersion%7C3.1.2',
	'CVPF': 'CT-1',
	'akavpau_www_cvs_com_general': '1616178379~id=928760d31eab1853ce85ffccf7154ed8',
	'_abck': '8F93E00AD5B76E583F7037157544D5E0~0~YAAQ9DLFF/SJQUV4AQAAo5K2SwWeSOvN039CM/SQIjt9S78AvemRRsQgHsqYk42XCZzuzIJEX//GeQtSTA4T6sCmU6WG/FpKR5Zysx8R/BLIROnd9uupHerAp7Nsprc1xjnj4KOSrDWx6NliiAMQSEZFUvZ5lgcQKzZWpEHUbjqAAlsvdz841XYdtOf6hbQiHHd60J5iUmI+R17Bt0esswO2VB/m/A9ZSlA31s/7mqIiqphla1oY3O+OODa85JvQF92hMAsQ0onIibNzyr/FRlJahI3gGQxfi/TQeq/WzZrBitWCgVF3D6yt2Pjjo63jL0Xi5hMYoxtMmIQ4iHGsl8MzyvYsqPRAZjpW+2/4UsLG5f3i6SYgM8PWksn0tksmhvwS3KOP8mdrF7CmRGO3VB2ViqNb~-1~||-1||~-1',
	'gbi_sessionId': 'ckmgmmmqy00003g7sv6pd6gm8',
	'gbi_visitorId': 'ckmgmmmqy00013g7soc66jj22',
	'ADRUM_BT': 'R:50|g:90ddfcb7-2e83-403a-bcaf-dfca742da7f66148335|i:81658|e:9|n:customer1_28053a73-9130-49bc-bebe-00daf9afaf35',
	'bm_sv': '98F6774471F768AAF0A6C953E6EE23A6~4bzRxbWtuCUNfvbt3AFt6T1MOBLnMvOrrhkptCZqBcsGWEL+VsQofqowFhMignzSZtRxhTZnUvWa21lqlAplTCBn8RUhPK5lpl6yoJkEj+Ux/CJYFaZYyo8K9EWgIK6WjeXV6v7Fmlr01aZ8dkFVGg==',
}

headers = {
	'authority': 'www.cvs.com',
	'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	'dnt': '1',
	'sec-ch-ua-mobile': '?0',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
	'accept': '*/*',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-mode': 'cors',
	'sec-fetch-dest': 'empty',
	'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine',
	'accept-language': 'en-US,en;q=0.9',
}

params = (
	('vaccineinfo', ''),
)

close_by_cities = set()

def update_close_by_cities(cities):
	for city in cities:
		city_name = "{}, CA".format(city["city"])

		directions_result = gmaps.distance_matrix(HOME_ADDRESS, city_name, mode="driving", departure_time=datetime.now())
		for row in directions_result["rows"]:
			seconds_to_place = row["elements"][0]["duration"]["value"]
			if seconds_to_place <= DISTANCE_IN_SECS:
				print("Adding {}".format(city_name))
				close_by_cities.add(city_name)

city_to_sent_time = {}

def should_send_text_for_city(city_name):
	if city_name not in city_to_sent_time:
		return True
	return (datetime.now() - city_to_sent_time[city_name]).seconds > RESEND_WINDOW


def check_cvs():
	print("Checking CVS @ {}".format(datetime.now()))
	CVS_response = requests.get(CVS_RESOURCE, headers=headers, params=params, cookies=cookies)
	cities = CVS_response.json()["responsePayloadData"]["data"]["CA"]
	
	if len(close_by_cities) == 0:
		update_close_by_cities(cities)

	for city in cities:
		city_name = "{}, CA".format(city["city"])
		city_status = city["status"]

		if city_name in close_by_cities and city_status != "Fully Booked" \
		and should_send_text_for_city(city_name):
			city_to_sent_time[city_name] = datetime.now()
			util.send_text(city_name, "CVS", "https://www.cvs.com/immunizations/covid-19-vaccine")
