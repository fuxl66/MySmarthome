#!/usr/bin/env python
#
tageszeit = sh.now()
if sh.LWZ.KWLParty() == 1 and sh.WS.KWL1() == 1 or sh.WS.KWL2() == 1 and sh.Status.Abwesend() == 0:
	if tageszeit.hour >= 6 and tageszeit.hour <= 19:
		sh.LWZ.p07FanStageDay(3)
		sh.LWZ.p07FanStageDay.timer(900, 1)
	else:
		sh.LWZ.p08FanStageNight(3)
		sh.LWZ.p08FanStageNight.timer(900, 1)