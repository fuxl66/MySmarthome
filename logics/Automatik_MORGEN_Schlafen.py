#!/usr/bin/env python
#
#Trigger
#08:00 Uhr

#Raff
tageszeit = sh.now()
if tageszeit.hour >= 8 and sh.ZS.Raffstore.Auto.Morgen() == 1:
	sh.OG.Raffstore.Bad.Autosperre(0)
	sh.OG.Raffstore.KiZiJona.Autosperre(0)
	sh.OG.Raffstore.SZ.Autosperre(0)
	sh.OG.Raffstore.VR.Autosperre(0)
	sh.ZS.Licht.AllesAus(1)
	sh.ZS.Licht.AllesAus(0)
	sh.Status.JonaAbend(0)
	sh.ZS.JonaSchlafenNacht(0)
