#!/usr/bin/env python
#
#if sh.Fritzbox.CarinaSmart() == 1 and sh.ZS.Notify.Android.Carina() == 1:
#	sh.nma('Carina @Home', 'Carina kommt nach Hause', 0)

#if sh.Fritzbox.CarinaSmart() == 0 and sh.ZS.Notify.Android.Carina() == 1:
#	sh.nma('Carina @Out', 'Carina geht aus dem Haus', 0)

if trigger['by']=='Item' and trigger['source']=='Fritzbox.Dreambox':
	if trigger['value']==False:
		logger.info("Dreambox Offline, set trigger!")
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
else:
	if trigger['by']=='Logic':
		if sh.Fritzbox.Dreambox()==False and sh.Fritzbox.Dreambox.age()>299:
			logger.info("Dreambox Offline more than 295s, sending NMA")
#			sh.nma('Dreambox Offline', 'Dreambox seit 5min Offline', 0)
			sh.pushbullet.note("Dreambox Offline", "Dreambox seit 5min Offline")

if trigger['by']=='Item' and trigger['source']=='Fritzbox.Server':
	if trigger['value']==False:
		logger.info("Server Offline, set trigger!")
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
else:
	if trigger['by']=='Logic':
		if sh.Fritzbox.Server()==False and sh.Fritzbox.Server.age()>299:
			logger.info("Server Offline more than 299s, sending NMA")
#			sh.nma('Server Offline', 'Server seit 5min Offline', 0)
			sh.pushbullet.note("Server Offline", "Server seit 5min Offline")

if trigger['by']=='Item' and trigger['source']=='Fritzbox.CarinaSmart':
	if trigger['value']==True:
		logger.info("Carina @home, set trigger!")
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=60)))
else:
	if trigger['by']=='Logic':
		if sh.Fritzbox.CarinaSmart()==True and sh.Fritzbox.CarinaSmart.age()>59 and sh.ZS.Notify.Android.Carina() == 1:
			logger.info("Carina @Home more than 59s, sending NMA")
#			sh.nma('Carina @Home', 'Carina kommt nach Hause', 0)
			sh.pushbullet.note("Carina @Home", "Carina kommt nach Hause")

if trigger['by']=='Item' and trigger['source']=='Fritzbox.CarinaSmart':
	if trigger['value']==False:
		logger.info("Carina not @home, set trigger!")
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
else:
	if trigger['by']=='Logic':
		if sh.Fritzbox.CarinaSmart()==False and sh.Fritzbox.CarinaSmart.age()>299 and sh.ZS.Notify.Android.Carina() == 1:
			logger.info("Carina @Home more than 295s, sending NMA")
#			sh.nma('Carina not @Home', 'Carina geht aus dem Haus', 0)
			sh.pushbullet.note("Carina not @Home", "Carina geht aus dem Haus")