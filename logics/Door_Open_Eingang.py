#!/usr/bin/env python
#
if sh.EG.Kontakt.Eingang() == 0 and sh.ZS.Notify.Android.Eingang() == 1:
#	sh.nma('Eingangstuer', 'Eingangstuer wurde geoeffnet', 2)
	sh.pushbullet.note("Eingangstüre", "Eingangstüre wurde geöffnet")