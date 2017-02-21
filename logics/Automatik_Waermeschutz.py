#!/usr/bin/env python
#
#Trigger
#WS.Temperatur.GW3
#WS.Temperatur.GW4
#WS.Fassade.*.Status
#WS.Fassade.*.position
#EG.Kontakt.WZ
#EG.Kontakt.EZ

ATemp = 'Aussentemperatur: {} °C'.format(sh.WS.Temperatur())
if sh.WS.Temperatur.GW3() == 1:
	WS3 = 'Wärmeschutz 25°C: Ja'
if sh.WS.Temperatur.GW3() == 0:
	WS3 = 'Wärmeschutz 25°C: Nein'
if sh.WS.Temperatur.GW4() == 1:
	WS4 = 'Wärmeschutz 30°C: Ja'
if sh.WS.Temperatur.GW4() == 0:
	WS4 = 'Wärmeschutz 30°C: Nein'
if sh.ZS.WaermeschutzPlus() == 1:
#Ost Waermeschutz PLUS
	if sh.WS.Fassade.Ost.Status() == 1 and sh.WS.Fassade.Ost.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 0:
		sh.WS.Fassade.Ost.position(100)
		sh.OG.Raffstore.SZ.angle(60)
		sh.OG.Raffstore.SZ.Autosperre(1)
	if sh.WS.Fassade.Ost.Status() == 1 and sh.WS.Fassade.Ost.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 1:
		sh.WS.Fassade.Ost.position(100)
		sh.OG.Raffstore.SZ.angle(100)
		sh.OG.Raffstore.SZ.Autosperre(1)
	if sh.WS.Temperatur.GW3() == 0 and sh.WS.Temperatur.GW4() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.OG.Raffstore.SZ.Autosperre(0)
	if sh.WS.Fassade.Ost.Status() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.OG.Raffstore.SZ.Autosperre(0)
#Sued Waermeschutz PLUS
	if sh.WS.Fassade.Sued.Status() == 1 and sh.WS.Fassade.Sued.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 0:
		sh.WS.Fassade.Sued.position(100)
		sh.WS.Fassade.SuedOG.position(100)
		sh.EG.Raffstore.KuecheTuere.angle(60)
		sh.EG.Raffstore.EZTuere.angle(60)
		sh.EG.Raffstore.EZFensterGross.angle(60)
		sh.OG.Raffstore.KiZiWest.angle(60)
		sh.EG.Raffstore.KuecheTuere.Autosperre(1)
		sh.EG.Raffstore.EZTuere.Autosperre(1)
		sh.EG.Raffstore.EZFensterGross.Autosperre(1)
		sh.OG.Raffstore.KiZiWest.Autosperre(1)
		if sh.Status.JonaMittag() == 1 or sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.KiZiJona.Autosperre(1)
		else:
			sh.OG.Raffstore.KiZiJona.angle(60)
			sh.OG.Raffstore.KiZiJona.Autosperre(1)
	if sh.WS.Fassade.Sued.Status() == 1 and sh.WS.Fassade.Sued.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 1:
		sh.WS.Fassade.Sued.position(100)
		sh.WS.Fassade.SuedOG.position(100)
		sh.EG.Raffstore.KuecheTuere.angle(100)
		sh.EG.Raffstore.EZTuere.angle(100)
		sh.EG.Raffstore.EZFensterGross.angle(100)
		sh.OG.Raffstore.KiZiWest.angle(100)
		sh.EG.Raffstore.KuecheTuere.Autosperre(1)
		sh.EG.Raffstore.EZTuere.Autosperre(1)
		sh.EG.Raffstore.EZFensterGross.Autosperre(1)
		sh.OG.Raffstore.KiZiWest.Autosperre(1)
		if sh.Status.JonaMittag() == 1 or sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.KiZiJona.Autosperre(1)
		else:
			sh.OG.Raffstore.KiZiJona.angle(100)
			sh.OG.Raffstore.KiZiJona.Autosperre(1)
	if sh.WS.Temperatur.GW3() == 0 and sh.WS.Temperatur.GW4() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.KuecheTuere.Autosperre(0)
		sh.EG.Raffstore.EZTuere.Autosperre(0)
		sh.EG.Raffstore.EZFensterGross.Autosperre(0)
		sh.OG.Raffstore.KiZiWest.Autosperre(0)
		if sh.Status.JonaMittag() == 1 or sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.KiZiJona.Autosperre(1)
		else:
			sh.OG.Raffstore.KiZiJona.Autosperre(0)
	if sh.WS.Fassade.Sued.Status() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.KuecheTuere.Autosperre(0)
		sh.EG.Raffstore.EZTuere.Autosperre(0)
		sh.EG.Raffstore.EZFensterGross.Autosperre(0)
		sh.OG.Raffstore.KiZiWest.Autosperre(0)
		if sh.Status.JonaMittag() == 1 or sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.KiZiJona.Autosperre(1)
		else:
			sh.OG.Raffstore.KiZiJona.Autosperre(0)
#SuedWest Waermeschutz PLUS
	if sh.WS.Fassade.SuedWest.Status() == 1 and sh.WS.Fassade.SuedWest.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 0:
		sh.WS.Fassade.SuedWest.position(100)
		sh.EG.Raffstore.WZTuere.angle(60)
		sh.EG.Raffstore.WZTuere.Autosperre(1)
	if sh.WS.Fassade.SuedWest.Status() == 1 and sh.WS.Fassade.SuedWest.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 1:
		sh.WS.Fassade.SuedWest.position(100)
		sh.EG.Raffstore.WZTuere.angle(100)
		sh.EG.Raffstore.WZTuere.Autosperre(1)
	if sh.WS.Temperatur.GW3() == 0 and sh.WS.Temperatur.GW4() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.WZTuere.Autosperre(0)
	if sh.WS.Fassade.SuedWest.Status() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.WZTuere.Autosperre(0)
#West Waermeschutz PLUS
	if sh.WS.Fassade.West.Status() == 1 and sh.WS.Fassade.West.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 0:
		sh.WS.Fassade.West.position(100)
		sh.WS.Fassade.WestOG.position(100)
		sh.EG.Raffstore.EZFensterKlein.angle(60)
		sh.EG.Raffstore.WZFenster.angle(60)
		sh.EG.Raffstore.EZFensterKlein.Autosperre(1)
		sh.EG.Raffstore.WZFenster.Autosperre(1)
		if sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.Bad.Autosperre(1)
			sh.OG.Raffstore.VR.Autosperre(1)
		else:
			sh.OG.Raffstore.Bad.angle(60)
			sh.OG.Raffstore.Bad.Autosperre(1)
			sh.OG.Raffstore.VR.angle(60)
			sh.OG.Raffstore.VR.Autosperre(1)
	if sh.WS.Fassade.West.Status() == 1 and sh.WS.Fassade.West.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 1:
		sh.WS.Fassade.West.position(100)
		sh.WS.Fassade.WestOG.position(100)
		sh.EG.Raffstore.EZFensterKlein.angle(100)
		sh.EG.Raffstore.WZFenster.angle(100)
		sh.EG.Raffstore.EZFensterKlein.Autosperre(1)
		sh.EG.Raffstore.WZFenster.Autosperre(1)
		if sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.Bad.Autosperre(1)
			sh.OG.Raffstore.VR.Autosperre(1)
		else:
			sh.OG.Raffstore.Bad.angle(100)
			sh.OG.Raffstore.Bad.Autosperre(1)
			sh.OG.Raffstore.VR.angle(100)
			sh.OG.Raffstore.VR.Autosperre(1)
	if sh.WS.Temperatur.GW3() == 0 and sh.WS.Temperatur.GW4() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.EZFensterKlein.Autosperre(0)
		sh.EG.Raffstore.WZFenster.Autosperre(0)
		if sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.Bad.Autosperre(1)
			sh.OG.Raffstore.VR.Autosperre(1)
		else:
			sh.OG.Raffstore.Bad.Autosperre(0)
			sh.OG.Raffstore.VR.Autosperre(0)
	if sh.WS.Fassade.West.Status() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.EZFensterKlein.Autosperre(0)
		sh.EG.Raffstore.WZFenster.Autosperre(0)
		if sh.Status.JonaAbend() == 1:
			sh.OG.Raffstore.Bad.Autosperre(1)
			sh.OG.Raffstore.VR.Autosperre(1)
		else:
			sh.OG.Raffstore.Bad.Autosperre(0)
			sh.OG.Raffstore.VR.Autosperre(0)