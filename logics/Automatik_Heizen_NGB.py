#!/usr/bin/env python
#
NGBFrost = 'NGB Temperatur: {} °C'.format(sh.NGB.Melder.Temperatur())
if sh.NGB.Melder.Temperatur() <= 5 and sh.Status.Sommerbetrieb() == 0 and sh.ZS.Notify.Android.NGBFrost() == 1:
	sh.NGB.Schuko.Heizluefter(1)
	sh.ZS.Notify.Android.NGBFrost(0)
	sh.pushbullet.note("NGB Frost Alarm", NGBFrost)