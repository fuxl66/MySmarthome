#!/usr/bin/env python
#
#Festnetznummer *10#
#Fuxl-Smartphone **700
#Carina-Smartphone **710
if sh.Wecker.Call() == 1:
	sh.Router7360.start_call('**700')
#	sh.fritzbox.call('*10#', '**700')
#	sh.fritzbox.call('0294220467', '00436767662233')