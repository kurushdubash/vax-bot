import cvs
import wg
import myturn
import time
import util

SLEEP_TIME_IN_MINS = 1

def main():
	while True:
		try:
			wg.check_walgreens()
			myturn.check_myturn()
			cvs.check_cvs()
		except Exception as e:
			print(e)
			
		time.sleep(60 * SLEEP_TIME_IN_MINS)
		
main()