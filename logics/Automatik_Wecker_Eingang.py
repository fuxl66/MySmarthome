#!/usr/bin/env python
#
if sh.Wecker.Eingang() == 1 and sh.EG.Kontakt.Eingang() == 0:
	if sh.AB.Licht.Eingang() == 0:
		sh.ZS.Licht.AllesAus(1)
		sh.ZS.Licht.AllesAus(0)
#		if sh.WS.TagNacht() == 1:
#			sh.AB.Licht.Eingang(1)
#			sh.AB.Licht.Eingang.timer(300, 0)
#	if sh.AB.Licht.Eingang() == 1:
#		if sh.WS.TagNacht() == 1:
#			sh.AB.Licht.Eingang(1)
#			sh.AB.Licht.Eingang.timer(300, 0)