#!/usr/bin/env python
#
if sh.env.location.moonphase() == 5 and sh.ZS.Notify.Android.Vollmond() == 1:
#	sh.nma('Regen', 'Es hat zu Regnen begonnen', 1)
	sh.pushbullet.note("VOLLMOND", "Heute ist Vollmond")