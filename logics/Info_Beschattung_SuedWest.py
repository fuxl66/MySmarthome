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
SWPos = 'Position: {}'.format(sh.WS.Fassade.SuedWest.position())
SWAngle = 'Angle: {}'.format(sh.WS.Fassade.SuedWest.angle())
if sh.WS.Fassade.SuedWest.Status() == 1:
	SWStatus = 'Status: EIN'
if sh.WS.Fassade.SuedWest.Status() == 0:
	SWStatus = 'Status: AUS'

if sh.ZS.Notify.Android.Beschattung() == 1 and sh.WS.Fassade.SperreSW() == 0 and sh.WS.UNDLogikSperre() == 0:
	sh.pushbullet.note("Beschattung Süd/West", SWStatus)