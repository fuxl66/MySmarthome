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

#Sued EG
SuedEGPos = 'Position EG: {}'.format(sh.WS.Fassade.Sued.position())
SuedEGAngle = 'Angle EG: {}'.format(sh.WS.Fassade.Sued.angle())
if sh.WS.Fassade.Sued.Status() == 1:
	SuedEGStatus = 'Status EG: EIN'
if sh.WS.Fassade.Sued.Status() == 0:
	SuedEGStatus = 'Status EG: AUS'
#Sued OG
SuedOGPos = 'Position OG: {}'.format(sh.WS.Fassade.SuedOG.position())
SuedOGAngle = 'Angle OG: {}'.format(sh.WS.Fassade.SuedOG.angle())
if sh.WS.Fassade.SuedOG.Status() == 1:
	SuedOGStatus = 'Status OG: EIN'
if sh.WS.Fassade.SuedOG.Status() == 0:
	SuedOGStatus = 'Status OG: AUS'

if sh.ZS.Notify.Android.Beschattung() == 1 and sh.WS.Fassade.SperreSEG() == 0 or sh.WS.Fassade.SperreSOG() == 0 and sh.WS.UNDLogikSperre() == 0:
	sh.pushbullet.note("Beschattung SÜD", SuedEGStatus)