#!/usr/bin/env python
#
#if sh.WS.Regen() == 1 and sh.ZS.Notify.Android.Regen() == 1:
#	sh.nma('Regen', 'Es hat zu Regnen begonnen', 1)
#	sh.pushbullet.note("Regen", "Es hat zu Regnen begonnen")
#	sh.WS.Regen.Info('Regen', 'Es hat zu Regnen begonnen')
#if sh.WS.Regen() == 0 and sh.ZS.Notify.Android.Regen() == 1:
#	sh.nma('KEIN Regen', 'Es regnet nicht mehr', 0)
#	sh.pushbullet.note("KEIN Regen", "Es regnet nicht mehr")
	
	
if sh.WS.Regen() == 1 and sh.WS.Regen.prev_value() == 0 and sh.ZS.Notify.Android.Regen() == 1:
	if trigger['by']=='Item' and trigger['source']=='WS.Regen':
		if trigger['value']==True:
			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
	else:
		if trigger['by']=='Logic':
			if sh.WS.Regen()==True and sh.WS.Regen.prev_value() == False and sh.WS.Regen.age()>299 and sh.WS.Regen.age()<304:
				sh.pushbullet.note("Regen", "Es hat zu Regnen begonnen")
				sh.WS.Regen.Info('Regen', 'Es hat zu Regnen begonnen')

if sh.WS.Regen() == 0 and sh.WS.Regen.prev_value() == 1 and sh.ZS.Notify.Android.Regen() == 1:
	if trigger['by']=='Item' and trigger['source']=='WS.Regen':
		if trigger['value']==False:
			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
	else:
		if trigger['by']=='Logic':
			if sh.WS.Regen()==False and sh.WS.Regen.prev_value() == True and sh.WS.Regen.age()>299 and sh.WS.Regen.age()<304:
				sh.pushbullet.note("KEIN Regen", "Es regnet nicht mehr")