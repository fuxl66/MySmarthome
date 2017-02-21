#!/usr/bin/env python
#
if sh.EG.Kontakt.WZ() == 0:
	sh.EG.Raffstore.WZTuere.Autosperre(1)
if sh.EG.Kontakt.WZ() == 1:
	if sh.Status.TagAbendRaff() == 1:
		sh.EG.Raffstore.WZTuere.move(1)
	if sh.WS.Fassade.SuedWest.Status() == 1 and sh.WS.Fassade.SuedWest.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 0:
		sh.EG.Raffstore.WZTuere.position(100)
		sh.EG.Raffstore.WZTuere.angle(70, 60)
		sh.EG.Raffstore.WZTuere.Autosperre(1)
	if sh.WS.Fassade.SuedWest.Status() == 1 and sh.WS.Fassade.SuedWest.position() == 100 and sh.WS.Temperatur.GW3() == 1 and sh.WS.Temperatur.GW4() == 1:
		sh.EG.Raffstore.WZTuere.position(100)
		sh.EG.Raffstore.WZTuere.angle(70, 100)
		sh.EG.Raffstore.WZTuere.Autosperre(1)
	if sh.WS.Temperatur.GW3() == 0 and sh.WS.Temperatur.GW4() == 0 and sh.Status.TagAbendRaff() == 0:
		sh.EG.Raffstore.WZTuere.Autosperre(0)