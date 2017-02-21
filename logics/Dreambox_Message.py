#!/usr/bin/env python

#send_message(messagetext, messagetype=1, timeout=10)
#Sets a message to the device messagetype: Number from 0 to 3, 0= Yes/No, 1= Info, 2=Message, 3=Attention timeout: Number of seconds the message should stay on the device, default: 10

#timeout = 10
sh.DM7020HD.send_message("Test JA-NEIN",0,5)
time.sleep(10)
#count = 10
#while (count > 0):
#	count = count - 1
sh.enigma2.dm7020hd.answer(sh.DM7020HD.get_answer())