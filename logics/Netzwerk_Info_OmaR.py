#!/usr/bin/env python
#
#OmaRosi
if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.OmaRosi':
	if trigger['value']==True:
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=120)))
else:
	if trigger['by']=='Logic':
		if sh.AVM.devices.router_7360.OmaRosi()==True and sh.AVM.devices.router_7360.OmaRosi.age()>119 and sh.AVM.devices.OmaRosi() == 1:
			sh.pushbullet.note("Oma Heidi Online", "Oma Heidi Online")

if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.OmaRosi':
	if trigger['value']==False:
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=120)))
else:
	if trigger['by']=='Logic':
		if sh.AVM.devices.router_7360.OmaRosi()==False and sh.AVM.devices.router_7360.OmaRosi.age()>119 and sh.AVM.devices.OmaRosi() == 1:
			sh.pushbullet.note("Oma Heidi Offline", "Oma Heidi seit 2 min Offline")