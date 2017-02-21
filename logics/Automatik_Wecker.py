#!/usr/bin/env python
#
tageszeit = sh.now()
ATemp = 'Aussentemperatur: {} °C'.format(sh.WS.Temperatur())
ATempMin = 'Lowest: {} °C'.format(sh.WS.Temperatur.MIN())
Wind = 'Windstärke: {} km/h'.format(sh.WS.Windstaerke.kmH())
Windmax = 'Highest: {} km/h'.format(sh.WS.Windstaerke.MAX())
Hell = 'Helligkeit: {} Lux'.format(sh.WS.Helligkeit())
if sh.WS.Regen() == 1:
	Regen = 'Regen: Ja'
if sh.WS.Regen() == 0:
	Regen = 'Regen: Nein'

#Festnetznummer *10#
#Fuxl-Smartphone **700
#Carina-Smartphone **710
#if sh.Wecker.Call() == 1:
#	sh.fritzbox.call('*10#', '**700')

#Zug 5:30
if sh.Wecker.Eins() == 1 and sh.Wecker.Eins.OnOff() == 1:
	if sh.Wecker.CallMarkus() == 1:
		sh.Router7360.start_call('**700')
		time.sleep(20)
	sh.pushbullet.note("Morgenbericht", Regen)
	sh.Wecker.Eingang(1)
	sh.Taster.SZSperreBett(1)
	sh.OG.SR.Dimmen(50)
	sh.OG.SR.Dimmen.timer(180, 0)
	sh.OG.Licht.BadSpiegel(1)
	sh.EG.Licht.BadWand(1)
	sh.EG.Licht.VRWand(1)
	sh.EG.Licht.VRDecke.timer(900, 1)
	sh.EG.Licht.VRWand.timer(900, 0)
	if sh.WS.Daemmerung.GW3() == 1:
		sh.EG.Licht.Stiege(1)
		sh.EG.Licht.KuecheSpuele(1)
		sh.EG.Licht.LeseWand(1)
	else:
		sh.OG.Raffstore.Bad.angle(70)
		sh.EG.Raffstore.EZTuere.angle(70)
		sh.EG.Raffstore.EZFensterGross.angle(70)
		sh.EG.Raffstore.WZTuere.angle(70)
		sh.EG.Raffstore.WZFenster.angle(70)
#Zug 5:52
if sh.Wecker.Zwei() == 1 and sh.Wecker.Zwei.OnOff() == 1:
	if sh.Wecker.CallMarkus() == 1:
		sh.Router7360.start_call('**700')
		time.sleep(20)
	sh.pushbullet.note("Morgenbericht", Regen)
	sh.Wecker.Eingang(1)
	sh.Taster.SZSperreBett(1)
	sh.OG.SR.Dimmen(50)
	sh.OG.SR.Dimmen.timer(180, 0)
	sh.OG.Licht.BadSpiegel(1)
	sh.EG.Licht.BadWand(1)
	sh.EG.Licht.VRWand(1)
	sh.EG.Licht.VRDecke.timer(1020, 1)
	sh.EG.Licht.VRWand.timer(1020, 0)
	if sh.WS.Daemmerung.GW3() == 1:
		sh.EG.Licht.Stiege(1)
		sh.EG.Licht.KuecheSpuele(1)
		sh.EG.Licht.LeseWand(1)
	else:
		sh.OG.Raffstore.Bad.angle(70)
		sh.EG.Raffstore.EZTuere.angle(70)
		sh.EG.Raffstore.EZFensterGross.angle(70)
		sh.EG.Raffstore.WZTuere.angle(70)
		sh.EG.Raffstore.WZFenster.angle(70)
#Zug 6:17
if sh.Wecker.Drei() == 1 and sh.Wecker.Drei.OnOff() == 1:
	if sh.Wecker.CallMarkus() == 1:
		sh.Router7360.start_call('**700')
		time.sleep(20)
	sh.pushbullet.note("Morgenbericht", Regen)
	sh.Wecker.Eingang(1)
	sh.Taster.SZSperreBett(1)
	sh.OG.SR.Dimmen(50)
	sh.OG.SR.Dimmen.timer(180, 0)
	sh.OG.Licht.BadSpiegel(1)
	sh.EG.Licht.BadWand(1)
	sh.EG.Licht.VRWand(1)
	sh.EG.Licht.VRDecke.timer(1020, 1)
	sh.EG.Licht.VRWand.timer(1020, 0)
	if sh.WS.Daemmerung.GW3() == 1:
		sh.EG.Licht.Stiege(1)
		sh.EG.Licht.KuecheSpuele(1)
		sh.EG.Licht.LeseWand(1)
	else:
		sh.OG.Raffstore.Bad.angle(70)
		sh.EG.Raffstore.EZTuere.angle(70)
		sh.EG.Raffstore.EZFensterGross.angle(70)
		sh.EG.Raffstore.WZTuere.angle(70)
		sh.EG.Raffstore.WZFenster.angle(70)
#Zug x:xx
if sh.Wecker.Vier() == 1 and sh.Wecker.Vier.OnOff() == 1:
	if sh.Wecker.CallMarkus() == 1:
		sh.Router7360.start_call('**700')
		time.sleep(20)
	sh.pushbullet.note("Morgenbericht", Regen)
	sh.OG.Licht.BadSpiegel(1)
	if sh.WS.Daemmerung.GW3() == 1:
		sh.EG.Licht.Stiege(1)
		sh.EG.Licht.KuecheSpuele(1)
		sh.EG.Licht.LeseWand(1)
	else:
		sh.OG.Raffstore.Bad.angle(70)
		sh.EG.Raffstore.EZTuere.angle(70)
		sh.EG.Raffstore.EZFensterGross.angle(70)
		sh.EG.Raffstore.WZTuere.angle(70)
		sh.EG.Raffstore.WZFenster.angle(70)