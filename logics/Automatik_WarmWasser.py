#!/usr/bin/env python
#
tageszeit = sh.now()
if sh.ZS.WW() == 1 and sh.LWZ.dhwPumpOn() == 0:
#Stufe 0 WW 42 Grad
	if trigger['by']=='Item' and trigger['source']=='EZ.P_Minus.Stufe0':
		if trigger['value']==True:
			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
	else:
		if trigger['by']=='Logic':
			if sh.EZ.P_Minus.Stufe0()==True and sh.EZ.P_Minus.Stufe0.age()>299 and sh.EZ.P_Minus.Stufe0.age()<304:
				sh.LWZ.p04DHWsetDayTemp(42)
#				sh.pushbullet.note("Setze WW SOLL 43", "43 Grad")
#				if sh.LWZ.dhwTemp() < 40 and sh.ZS.WW.Info() == 1:
#					sh.pushbullet.note("Energie Stufe 0", "Lieferung 500 W, WW Temp Soll 43 Grad")
#Stufe 1 WW 48 Grad
	if trigger['by']=='Item' and trigger['source']=='EZ.P_Minus.Stufe1':
		if trigger['value']==True:
			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
	else:
		if trigger['by']=='Logic':
			if sh.EZ.P_Minus.Stufe1()==True and sh.EZ.P_Minus.Stufe1.age()>299 and sh.EZ.P_Minus.Stufe1.age()<304:
				sh.LWZ.p04DHWsetDayTemp(48)
#				sh.pushbullet.note("Setze WW SOLL 48", "48 Grad")
				if sh.LWZ.dhwTemp() < 46 and sh.ZS.WW.Info() == 1:
					sh.pushbullet.note("Energie Stufe 1", "Lieferung zw 500 und 2000 W, WW Temp Soll 48 Grad")
#Stufe 2 WW 53 Grad
#	if trigger['by']=='Item' and trigger['source']=='EZ.P_Minus.Stufe2':
#		if trigger['value']==True:
#			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=300)))
#	else:
#		if trigger['by']=='Logic':
#			if sh.EZ.P_Minus.Stufe2()==True and sh.EZ.P_Minus.Stufe2.age()>299 and sh.EZ.P_Minus.Stufe2.age()<304:
#				sh.LWZ.p04DHWsetDayTemp(53)
#				sh.pushbullet.note("Setze WW SOLL 53", "53 Grad")
#				if sh.LWZ.dhwTemp() < 51 and sh.ZS.WW.Info() == 1:
#					sh.pushbullet.list("Energie Stufe 2", ["Lieferung zw 2000 und 3500 W", "WW Temp Soll 53 Grad"])
#Stufe 3 WW 55 Grad
#	if trigger['by']=='Item' and trigger['source']=='EZ.P_Minus.Stufe3':
#		if trigger['value']==True:
#			logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=600)))
#	else:
#		if trigger['by']=='Logic':
#			if sh.EZ.P_Minus.Stufe3()==True and sh.EZ.P_Minus.Stufe3.age()>599 and sh.EZ.P_Minus.Stufe3.age()<604:
#				sh.LWZ.p04DHWsetDayTemp(55)
#				sh.pushbullet.note("Setze WW SOLL 55", "55 Grad")
#				if sh.LWZ.dhwTemp() < 53 and sh.ZS.WW.Info() == 1:
#					sh.pushbullet.list("Energie Stufe 3", ["Lieferung 2500 W", "WW Temp Soll 55 Grad"])
#Stufe Abend WW x Grad
	if sh.Status.Sommerbetrieb() == 1:
#		if tageszeit.hour == 18 and (sh.LWZ.p04DHWsetDayTemp() - sh.LWZ.dhwTemp()) >= 0 and sh.LWZ.dhwPumpOn() == 0:
#			sh.LWZ.p04DHWsetDayTemp(sh.p04DHWsetDayTemp() + 2)
#			sh.pushbullet.note("WW Abend Minimum", "WW Abend Minimum")
		if tageszeit.hour == 18 and sh.LWZ.dhwTemp() < 45 and sh.LWZ.dhwPumpOn() == 0:
			sh.LWZ.p04DHWsetDayTemp(47)
			sh.pushbullet.note("WW Abend Minimum", "WW Abend Minimum")
	if sh.Status.Sommerbetrieb() == 0:
#		if tageszeit.hour == 17 and (sh.LWZ.p04DHWsetDayTemp() - sh.LWZ.dhwTemp()) >= 0 and sh.LWZ.dhwPumpOn() == 0:
#			sh.LWZ.p04DHWsetDayTemp(sh.LWZ.p04DHWsetDayTemp() + 2)
#			sh.pushbullet.note("WW Abend Minimum", "WW Abend Minimum")
		if tageszeit.hour == 17 and sh.LWZ.dhwTemp() < 45 and sh.LWZ.dhwPumpOn() == 0:
			sh.LWZ.p04DHWsetDayTemp(47)
			sh.pushbullet.note("WW Abend Minimum", "WW Abend Minimum")