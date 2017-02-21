#!/usr/bin/env python
#
tageszeit = sh.now()
if tageszeit.hour >= 6 and tageszeit.hour <= 19:
	sh.WS.KWLIcon(sh.LWZ.p07FanStageDay())
else:
	sh.WS.KWLIcon(sh.LWZ.p08FanStageNight()) 