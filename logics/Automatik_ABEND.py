#!/usr/bin/env python
#
#Trigger
#WS.TagNacht
#WS.Windstaerke.GW1
#WS.Daemmerung.GW1

#RAFFSTORES
tageszeit = sh.now()
if tageszeit.hour >= 16 and tageszeit.hour <= 22 and sh.WS.TagNacht() == 1 and sh.ZS.Raffstore.Auto.Nacht() == 1 and sh.WS.Windstaerke.GW1() == 0:
	sh.Status.TagAbendRaff(1)
	if sh.EG.Raff.KuecheTuere.ReadPos() == 100:
		sh.EG.Raffstore.KuecheTuere.angle(100)
	else:
		sh.EG.Raffstore.KuecheTuere.move(1)
	if sh.EG.Kontakt.EZ() == 1:
		if sh.EG.Raff.EZTuere.ReadPos() == 100:
			sh.EG.Raffstore.EZTuere.angle(100)
		else:
			sh.EG.Raffstore.EZTuere.move(1)
	if sh.EG.Raff.EZFensterGross.ReadPos() == 100:
		sh.EG.Raffstore.EZFensterGross.angle(100)
	else:
		sh.EG.Raffstore.EZFensterGross.move(1)
	if sh.EG.Raff.EZFensterKlein.ReadPos() == 100:
		sh.EG.Raffstore.EZFensterKlein.angle(100)
	else:
		sh.EG.Raffstore.EZFensterKlein.move(1)
	if sh.EG.Kontakt.WZ() == 1:
		if sh.EG.Raff.WZTuere.ReadPos() == 100:
			sh.EG.Raffstore.WZTuere.angle(100)
		else:
			sh.EG.Raffstore.WZTuere.move(1)
	if sh.EG.Raff.WZFenster.ReadPos() == 100:
		sh.EG.Raffstore.WZFenster.angle(100)
	else:
		sh.EG.Raffstore.WZFenster.move(1)
	if sh.OG.Raff.Bad.ReadPos() == 100:
		sh.OG.Raffstore.Bad.angle(100)
	else:
		sh.OG.Raffstore.Bad.move(1)
	if sh.OG.Raff.SZSR.ReadPos() == 100:
		sh.OG.Raffstore.SZ.angle(0)
	else:
		sh.OG.Raffstore.SZ.move(1)
		time.sleep(70)
		sh.OG.Raffstore.SZ.angle(0)
	sh.EG.Raffstore.KuecheTuere.Autosperre(1)
	sh.EG.Raffstore.EZTuere.Autosperre(1)
	sh.EG.Raffstore.EZFensterGross.Autosperre(1)
	sh.EG.Raffstore.EZFensterKlein.Autosperre(1)
	sh.EG.Raffstore.WZTuere.Autosperre(1)
	sh.EG.Raffstore.WZFenster.Autosperre(1)
	sh.OG.Raffstore.Bad.Autosperre(1)
	sh.OG.Raffstore.SZ.Autosperre(1)
	if sh.Status.Sommerbetrieb() == 1:
		sh.OG.Raffstore.VR.Autosperre(1)
#LICHT
if  tageszeit.hour >= 15 and tageszeit.hour <= 21 and sh.WS.Daemmerung.GW1() == 1 and sh.ZS.Raffstore.Auto.Nacht() == 1 and sh.Status.Abwesend() == 0 and sh.Status.TagAbendRaff() == 0:
	sh.EG.Licht.Stiege(1)
	sh.EG.Licht.LeseWand(1)