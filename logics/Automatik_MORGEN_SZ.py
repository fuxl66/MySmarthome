#!/usr/bin/env python
#
#Trigger
#WS.TagNacht
#WS.Windstaerke.GW1
tageszeit = sh.now()
if tageszeit.hour > 3 and tageszeit.hour <= 7 and sh.WS.TagNacht() == 0 and sh.ZS.Raffstore.Auto.SZ() == 1 and sh.WS.Windstaerke.GW1() == 0 and sh.Status.Abwesend() == 0:
	if sh.OG.Raff.SZSR.ReadPos() == 100:
		sh.OG.Raffstore.SZ.angle(100)
	else:
		sh.OG.Raffstore.SZ.move(1)