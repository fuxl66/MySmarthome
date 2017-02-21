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

#West EG
WestEGPos = 'Position EG: {}'.format(sh.WS.Fassade.West.position())
WestEGAngle = 'Angle EG: {}'.format(sh.WS.Fassade.West.angle())
if sh.WS.Fassade.West.Status() == 1:
	WestEGStatus = 'Status EG: EIN'
if sh.WS.Fassade.West.Status() == 0:
	WestEGStatus = 'Status EG: AUS'
#West OG
WestOGPos = 'Position OG: {}'.format(sh.WS.Fassade.WestOG.position())
WestOGAngle = 'Angle OG: {}'.format(sh.WS.Fassade.WestOG.angle())
if sh.WS.Fassade.WestOG.Status() == 1:
	WestOGStatus = 'Status OG: EIN'
if sh.WS.Fassade.WestOG.Status() == 0:
	WestOGStatus = 'Status OG: AUS'

if sh.ZS.Notify.Android.Beschattung() == 1 and sh.WS.Fassade.SperreWEG() == 0 or sh.WS.Fassade.SperreWOG() == 0 and sh.WS.UNDLogikSperre() == 0:
	sh.pushbullet.note("Beschattung West", WestEGStatus)