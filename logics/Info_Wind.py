#!/usr/bin/env python
#
Wind = 'Windstärke: {} km/h'.format(sh.WS.Windstaerke.kmH())
if sh.WS.Windstaerke.GW1() == 1 and sh.ZS.Notify.Android.Wind() == 1:
#	sh.nma('Wind Alarm GW1', 'Grenzwert überschritten, Windstärke: {} km/h'.format(sh.WS.Windstaerke.kmH()), 2)
	sh.pushbullet.note("Wind Alarm GW1", Wind)
	sh.WS.Windstaerke.GW1.Info('Grenzwert überschritten. Aktuelle Windstärke: {} km/h'.format(sh.WS.Windstaerke.kmH()))
else:
#	sh.nma('Wind Alarm ENDE', 'Windstärke: {} km/h'.format(sh.WS.Windstaerke.kmH()), 0)
	sh.pushbullet.note("Wind Alarm ENDE", Wind)