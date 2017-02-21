#!/usr/bin/env python
#
if sh.ZS.JonaSchlafenNacht() == 1 and sh.Status.Abwesend() == 0:
	sh.Status.JonaAbend(1)
	if sh.OG.Raff.Bad.ReadPos() == 100:
		sh.OG.Raffstore.Bad.angle(100)
	else:
		sh.OG.Raffstore.Bad.move(1)
	if sh.OG.Raff.KiZiJona.ReadPos() == 100:
		sh.OG.Raffstore.KiZiJona.angle(100)
	else:
		sh.OG.Raffstore.KiZiJona.move(1)
	if sh.Status.Sommerbetrieb() == 1:
		if sh.OG.Raff.VR.ReadPos() == 100:
			sh.OG.Raffstore.VR.angle(100)
		else:
			sh.OG.Raffstore.VR.move(1)
		sh.OG.Raffstore.VR.Autosperre(1)
	sh.OG.Raffstore.Bad.Autosperre(1)
	sh.OG.Raffstore.KiZiJona.Autosperre(1)
	sh.OG.KiZiJona.Schalten(1)
	sh.OG.Licht.BadBox(1)
	sh.OG.Licht.BadWand(1)