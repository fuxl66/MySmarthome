#!/usr/bin/env python
#
if sh.WS.Temperatur.Stoerung() == 1:
	sh.pushbullet.note("Error", "Stoerung des Temperatur Sensors")
if sh.WS.Windstaerke.Stoerung() == 1:
	sh.pushbullet.note("Error", "Stoerung des Wind Sensors")
if sh.WS.GPSStoerung() == 1:
	sh.pushbullet.note("Error", "GPS Stoerung")
if sh.LWZ.numberOfFaults() > 0:
	sh.pushbullet.note("Error", "Stoerung Heizung")
#if sh.LWZ.boosterStage1On() == 1:
#	sh.pushbullet.note("Heizstab EIN", "Stufe 1")
#if sh.LWZ.boosterStage2On() == 1:
#	sh.pushbullet.note("Heizstab EIN", "Stufe 2")
#if sh.LWZ.boosterStage3On() == 1:
#	sh.pushbullet.note("Heizstab EIN", "Stufe 3")