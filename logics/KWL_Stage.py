#!/usr/bin/env python
#
tageszeit = sh.now()
ATemp = 'Aussentemperatur: {} °C'.format(sh.WS.Temperatur())
ITemp = 'Raumtemperatur: {} °C'.format(sh.LWZ.roomTempRC())
if sh.ZS.KWL() == 1 and sh.Status.KWLPartyMittag() == 0:
	if sh.Status.Sommerbetrieb() == 1:
		#KWL Stufe 0
		if trigger['by']=='Item' and trigger['source']=='WS.KWL0':
			if trigger['value']==True:
				logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=900)))
		else:
			if trigger['by']=='Logic':
				if sh.WS.KWL0()==True and sh.WS.KWL0.age()>899:
					if tageszeit.hour >= 6 and tageszeit.hour <= 19 and sh.WS.KWL0() != sh.WS.KWL0.prev_value():
						sh.LWZ.p07FanStageDay(0)
	#					sh.pushbullet.list("KWL Stage Day 0", [ATemp, ITemp])
						if sh.LWZ.p07FanStageDay() != sh.LWZ.p07FanStageDay.prev_value() and sh.ZS.KWL.Info() == 1:
							sh.pushbullet.list("KWL Stage Day 0", [ATemp, ITemp])
					if tageszeit.hour < 6 or tageszeit.hour > 19 and sh.WS.KWL0() != sh.WS.KWL0.prev_value():
						sh.LWZ.p08FanStageNight(0)
	#					sh.pushbullet.list("KWL Stage Night 0", [ATemp, ITemp])
						if sh.LWZ.p08FanStageNight() != sh.LWZ.p08FanStageNight.prev_value() and sh.ZS.KWL.Info() == 1:
							sh.pushbullet.list("KWL Stage Night 0", [ATemp, ITemp])
	#KWL Stufe 1
		if trigger['by']=='Item' and trigger['source']=='WS.KWL1':
			if trigger['value']==True:
				logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=900)))
		else:
			if trigger['by']=='Logic':
				if sh.WS.KWL1()==True and sh.WS.KWL1.age()>899:
					if tageszeit.hour >= 6 and tageszeit.hour <= 19 and sh.WS.KWL1() != sh.WS.KWL1.prev_value():
						sh.LWZ.p07FanStageDay(1)
	#					sh.pushbullet.list("KWL Stage Day 1", [ATemp, ITemp])
						if sh.LWZ.p07FanStageDay() != sh.LWZ.p07FanStageDay.prev_value() and sh.ZS.KWL.Info() == 1:
							sh.pushbullet.list("KWL Stage Day 1", [ATemp, ITemp])
					if tageszeit.hour < 6 or tageszeit.hour > 19 and sh.WS.KWL1() != sh.WS.KWL1.prev_value():
						sh.LWZ.p08FanStageNight(1)
	#					sh.pushbullet.list("KWL Stage Night 1", [ATemp, ITemp])
						if sh.LWZ.p08FanStageNight() != sh.LWZ.p08FanStageNight.prev_value() and sh.ZS.KWL.Info() == 1:
							sh.pushbullet.list("KWL Stage Night 1", [ATemp, ITemp])
	#KWL Stufe 2
		if trigger['by']=='Item' and trigger['source']=='WS.KWL2':
			if trigger['value']==True:
				logic.trigger(dt=(sh.now()+datetime.timedelta(seconds=900)))
		else:
			if trigger['by']=='Logic':
				if sh.WS.KWL2()==True and sh.WS.KWL2.age()>899:
					if tageszeit.hour >= 6 and tageszeit.hour <= 19 and sh.WS.KWL2() != sh.WS.KWL2.prev_value():
						sh.LWZ.p07FanStageDay(2)
	#					sh.pushbullet.list("KWL Stage Day 2", [ATemp, ITemp])
						if sh.LWZ.p07FanStageDay() != sh.LWZ.p07FanStageDay.prev_value() and sh.ZS.KWL.Info() == 1:
							sh.pushbullet.list("KWL Stage Day 2", [ATemp, ITemp])
					if tageszeit.hour < 6 or tageszeit.hour > 19 and sh.WS.KWL2() != sh.WS.KWL2.prev_value():
						sh.LWZ.p08FanStageNight(2)
	#					sh.pushbullet.list("KWL Stage Night 2", [ATemp, ITemp])
						if sh.LWZ.p08FanStageNight() != sh.LWZ.p08FanStageNight.prev_value() and sh.ZS.KWL.Info() == 1:
							sh.pushbullet.list("KWL Stage Night 2", [ATemp, ITemp])
	if sh.Status.Sommerbetrieb() == 0:
		sh.LWZ.p07FanStageDay(1)
		sh.LWZ.p08FanStageNight(1)