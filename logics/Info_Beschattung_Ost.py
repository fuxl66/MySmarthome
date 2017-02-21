#!/usr/bin/env python
ATemp = 'Aussentemperatur: {} °C'.format(sh.WS.Temperatur())
Hell = 'Helligkeit: {} Lux'.format(sh.WS.Helligkeit())
if sh.WS.Temperatur.GW3() == 1:
	WS3 = 'Wärmeschutz 25°C: Ja'
if sh.WS.Temperatur.GW3() == 0:
	WS3 = 'Wärmeschutz 25°C: Nein'
if sh.WS.Temperatur.GW4() == 1:
	WS4 = 'Wärmeschutz 30°C: Ja'
if sh.WS.Temperatur.GW4() == 0:
	WS4 = 'Wärmeschutz 30°C: Nein'

#Ost
OstPos = 'Position: {}'.format(sh.WS.Fassade.Ost.position())
OstAngle = 'Angle: {}'.format(sh.WS.Fassade.Ost.angle())
if sh.WS.Fassade.Ost.Status() == 1:
	OstStatus = 'Status: EIN'
if sh.WS.Fassade.Ost.Status() == 0:
	OstStatus = 'Status: AUS'

if sh.ZS.Notify.Android.Beschattung() == 1 and sh.WS.Fassade.SperreOst() == 0 and sh.WS.UNDLogikSperre() == 0:
	sh.pushbullet.note("Beschattung Ost", OstStatus)
