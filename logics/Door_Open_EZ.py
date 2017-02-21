#!/usr/bin/env python
#
if sh.EG.Kontakt.EZ() == 0:
	sh.EG.Raffstore.EZTuere.Autosperre(1)
if sh.EG.Kontakt.EZ() == 1:
	if sh.Status.TagAbendRaff() == 1:
		sh.EG.Raffstore.EZTuere.move(1)
	if sh.WS.Fassade.Sued.Status() == 1 and sh.WS.Fassade.Sued.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 0:
		sh.EG.Raffstore.EZTuere.position(100)
		sh.EG.Raffstore.EZTuere.angle.timer(70, 60)
		sh.EG.Raffstore.EZTuere.Autosperre(1)
	if sh.WS.Fassade.Sued.Status() == 1 and sh.WS.Fassade.Sued.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 1:
		sh.EG.Raffstore.EZTuere.position(100)
		sh.EG.Raffstore.EZTuere.angle.timer(70, 100)
		sh.EG.Raffstore.EZTuere.Autosperre(1)
	if sh.WS.Temperatur.GW3() == 0 and sh.WS.Temperatur.GW4() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.EZTuere.Autosperre(0)