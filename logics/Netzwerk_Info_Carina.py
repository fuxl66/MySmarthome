#!/usr/bin/env python
#
#Carina
if sh.AVM.devices.router_7360.FuxlSmart() == 0:
	if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.CarinaSmart':
		if trigger['value']==True:
			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=120)))
	else:
		if trigger['by']=='Logic':
			if sh.AVM.devices.router_7360.CarinaSmart()==True and sh.AVM.devices.router_7360.CarinaSmart.age()>119 and sh.AVM.devices.Carina() == 1:
				sh.pushbullet.note("Carina Online", "Carina Online")

	if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.CarinaSmart':
		if trigger['value']==False:
			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=120)))
	else:
		if trigger['by']=='Logic':
			if sh.AVM.devices.router_7360.CarinaSmart()==False and sh.AVM.devices.router_7360.CarinaSmart.age()>119 and sh.AVM.devices.Carina() == 1:
				sh.pushbullet.note("Carina Offline", "Carina seit 2 min Offline")