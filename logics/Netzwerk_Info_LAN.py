#!/usr/bin/env python
#
#Dreambox
if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.Dreambox':
	if trigger['value']==False:
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
else:
	if trigger['by']=='Logic':
		if sh.AVM.devices.router_7360.Dreambox()==False and sh.AVM.devices.router_7360.Dreambox.age()>299 and sh.AVM.devices.Dreambox() == 1:
			sh.pushbullet.note("Dreambox Offline", "Dreambox seit 5 min Offline")

#Server
if trigger['by']=='Item' and trigger['source']=='AVM.devices.router_7360.Server':
	if trigger['value']==False:
		logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
else:
	if trigger['by']=='Logic':
		if sh.AVM.devices.router_7360.Server()==False and sh.AVM.devices.router_7360.Server.age()>299 and sh.AVM.devices.Server() == 1:
			sh.pushbullet.note("Server Offline", "Server seit 5 min Offline")