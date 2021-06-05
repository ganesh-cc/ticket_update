import schedule
import time
import Integrator

def job():
	Integrator.integrator_func("rxtech")
	
schedule.every().day.at("17:00").do(job)

while True:
	schedule.run_pending()
	
