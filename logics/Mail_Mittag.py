#!/usr/bin/env python
	#Wetter
W = 'Aktuelle Wetterdaten:'
WTemp = '  Aussentemperatur: {} °C'.format(sh.WS.Temperatur())
WTempMax = '    Highest: {} °C'.format(sh.WS.Temperatur.MAX())
WTempMaxUhr = '    Uhrzeit: {}'.format(sh.WS.Temperatur.MAXUhr())
WTempMin = '    Lowest: {} °C'.format(sh.WS.Temperatur.MIN())
WWind = '  Windstärke: {} km/h'.format(sh.WS.Windstaerke.kmH())
WWindmax = '    Highest: {} km/h'.format(sh.WS.Windstaerke.MAX())
if sh.WS.Regen() == 1:
	WRegen = '  Regen: Ja'
if sh.WS.Regen() == 0:
	WRegen = '  Regen: Nein'

#Grenzwerte
if sh.WS.Waermeschutz.Status() == 1 or sh.WS.Temperatur.GW1() == 1 or sh.WS.Windstaerke.GW1() == 1 or sh.WS.Helligkeit.GW1() == 1 or sh.WS.Helligkeit.GW2() == 1:
	G = 'Aktive Grenzwerte:'
else:
	G = ''
if sh.WS.Waermeschutz.Status() == 1:
	GWaerme = ' Wärmeschutz'
else:
	GWaerme = ''
if sh.WS.Temperatur.GW1() == 1:
	GFrost = ' Frost'
else:
	GFrost = ''
if sh.WS.Windstaerke.GW1() == 1:
	GWind = ' Windalarm'
else:
	GWind = ''
if sh.WS.Helligkeit.GW1() == 1 or sh.WS.Helligkeit.GW2() == 1:
	GHell = ' Helligkeit'
else:
	GHell = ''

#Beschattung
B = 'Beschattung:'
BHell = '  Helligkeit: {} Lux'.format(sh.WS.Helligkeit())
BFass = 'aktive Fassaden'
if sh.WS.Fassade.Ost.EinAus() == 1:
	BOst = ' Osten '
else:
	BOst = ''
if sh.WS.Fassade.Sued.EinAus() == 1:
	BSued = ' Süden '
else:
	BSued = ''
if sh.WS.Fassade.SuedWest.EinAus() == 1:
	BSW = ' Süd/West '
else:
	BSW = ''
if sh.WS.Fassade.West.EinAus() == 1:
	BWest = ' Westen '
else:
	BWest = ''

#Energie
E = 'Energie:'
EPVcurrent = '  Aktuelle Leistung: {} W'.format(sh.solar.current())
#EPVcurrentmax = '    Highest: {} W'.format(sh.solar.current.MAX())
EPVday = '  Tagesertrag: {} kWh'.format(sh.solar.day())
EPVdaybefore = '    Vortag: {} kWh'.format(sh.solar.day.daybefore())
EPVtotal = '  Gesamtertrag: {} kWh'.format(sh.solar.total())

#Netzwerk
N = 'Netzwerk:'
if sh.AVM.devices.repeater_eg.CarinaSmart() == 1 or sh.AVM.devices.repeater_og.CarinaSmart() == 1:
	NCarina = '  Carina @Home'
else:
	NCarina = '  Carina NOT @Home'

#Signatur
textSignatur = '<<< powered by fuxl >>>'

#Mittag
Mittag = W + "\n" + WTemp + "\n" + WTempMax + "\n" + WTempMin + "\n" + WWind + "\n" + WWindmax + "\n" + WRegen + "\n" + "\n" + G + "\n" + GWaerme + GFrost + GWind + GHell + "\n" + "\n" + B + "\n" + BHell + "\n" + BFass + "\n" + BOst + BSued + BSW + BWest + "\n" + "\n" + E + "\n" + EPVcurrent + "\n" + EPVday + "\n" + EPVdaybefore + "\n" + EPVtotal + "\n" + "\n" + N + "\n" + NCarina + "\n" + "\n" + textSignatur

if sh.ZS.Notify.Mail() == 1 and sh.WS.SonneElevation.RoundAktuell() == sh.WS.SonneElevation.MaxGestern(): #MittagMaxElevationVortag
	sh.mail('fuxl@outlook.com', 'Mittagsbericht', Mittag.encode('utf-8'))

