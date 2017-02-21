#!/usr/bin/env python
if sh.WS.Fassade.Ost.angle() == 0 and sh.WS.Fassade.Ost.position() == 0 and sh.WS.Fassade.Ost.Status() == 0:
	sh.WS.Fassade.SperreOst(1)

if sh.WS.Fassade.Sued.angle() == 0 and sh.WS.Fassade.Sued.position() == 0 and sh.WS.Fassade.Sued.Status() == 0:
	sh.WS.Fassade.SperreSEG(1)

if sh.WS.Fassade.SuedOG.angle() == 0 and sh.WS.Fassade.SuedOG.position() == 0 and sh.WS.Fassade.SuedOG.Status() == 0:
	sh.WS.Fassade.SperreSOG(1)

if sh.WS.Fassade.SuedWest.angle() == 0 and sh.WS.Fassade.SuedWest.position() == 0 and sh.WS.Fassade.SuedWest.Status() == 0:
	sh.WS.Fassade.SperreSW(1)

if sh.WS.Fassade.West.angle() == 0 and sh.WS.Fassade.West.position() == 0 and sh.WS.Fassade.West.Status() == 0:
	sh.WS.Fassade.SperreWEG(1)

if sh.WS.Fassade.WestOG.angle() == 0 and sh.WS.Fassade.WestOG.position() == 0 and sh.WS.Fassade.WestOG.Status() == 0:
	sh.WS.Fassade.SperreWOG(1)