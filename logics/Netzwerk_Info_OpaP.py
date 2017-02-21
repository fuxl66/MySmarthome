#!/usr/bin/env python
#
#OpaPepi
if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.OpaPepi':
	if trigger['value']==True:
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=120)))
else:
	if trigger['by']=='Logic':
		if sh.AVM.devices.router_7360.OpaPepi()==True and sh.AVM.devices.router_7360.OpaPepi.age()>119 and sh.AVM.devices.OpaPepi() == 1:
			sh.pushbullet.note("Oma Heidi Online", "Oma Heidi Online")

if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.OpaPepi':
	if trigger['value']==False:
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=120)))
else:
	if trigger['by']=='Logic':
		if sh.AVM.devices.router_7360.OpaPepi()==False and sh.AVM.devices.router_7360.OpaPepi.age()>119 and sh.AVM.devices.OpaPepi() == 1:
			sh.pushbullet.note("Oma Heidi Offline", "Oma Heidi seit 2 min Offline")