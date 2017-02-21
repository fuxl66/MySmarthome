#!/usr/bin/env python
#
#Trigger
#WS.Daemmerung.GW2
#06:30 Uhr

#Raff
tageszeit = sh.now()
if tageszeit.hour > 5 and tageszeit.hour < 10 and sh.WS.Daemmerung.GW2() == 0 and sh.ZS.Raffstore.Auto.Morgen() == 1:
	sh.WS.Fassade.Sued.angle(0)
	sh.WS.Fassade.SuedOG.angle(0)
	sh.WS.Fassade.SuedWest.angle(0)
	sh.WS.Fassade.Ost.angle(0)
	sh.WS.Fassade.West.angle(0)
	sh.WS.Fassade.WestOG.angle(0)
	sh.WS.Fassade.Sued.position(0)
	sh.WS.Fassade.SuedOG.position(0)
	sh.WS.Fassade.SuedWest.position(0)
	sh.WS.Fassade.Ost.position(0)
	sh.WS.Fassade.West.position(0)
	sh.WS.Fassade.WestOG.position(0)
	sh.EG.Raffstore.KuecheTuere.Autosperre(0)
	sh.EG.Raffstore.EZTuere.Autosperre(0)
	sh.EG.Raffstore.EZFensterGross.Autosperre(0)
	sh.EG.Raffstore.EZFensterKlein.Autosperre(0)
	sh.EG.Raffstore.WZTuere.Autosperre(0)
	sh.EG.Raffstore.WZFenster.Autosperre(0)
	sh.OG.Raffstore.KiZiWest.Autosperre(0)
	sh.OG.Raffstore.VR.angle(0)
	sh.OG.Raffstore.Bad.angle(0)
	sh.Status.TagAbendRaff(0)
	sh.LWZ.p04DHWsetDayTemp(42)
	sh.LWZ.p05DHWsetNightTemp(42)