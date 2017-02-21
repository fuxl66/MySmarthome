#!/usr/bin/env python
#
if sh.ZS.JonaSchlafen() == 1 and sh.Status.Abwesend() == 0:
	sh.Status.JonaMittag(1)
	if sh.OG.Raff.KiZiJona.ReadPos() == 100:
		sh.OG.Raffstore.KiZiJona.angle(100)
	else:
		sh.OG.Raffstore.KiZiJona.move(1)
	sh.OG.Raffstore.KiZiJona.Autosperre(1)
if sh.ZS.JonaSchlafen() == 0 and sh.Status.Abwesend() == 0:
	sh.Status.JonaMittag(0)
	if sh.WS.Fassade.Sued.Status() == 1 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 0:
		sh.OG.Raffstore.KiZiJona.angle(60)
		sh.OG.Raffstore.KiZiJona.Autosperre(1)
	if sh.WS.Fassade.Sued.Status() == 1 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 1:
		sh.OG.Raffstore.KiZiJona.angle(100)
		sh.OG.Raffstore.KiZiJona.Autosperre(1)
	if sh.WS.Temperatur.GW3() == 0 and sh.WS.Temperatur.GW4() == 0:
		sh.OG.Raffstore.KiZiJona.Autosperre(0)
	if sh.WS.Fassade.Sued.Status() == 0:
		sh.OG.Raffstore.KiZiJona.Autosperre(0)