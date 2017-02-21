#!/usr/bin/env python3
#########################################################################
#  Copyright 2014 toggle
#########################################################################
#
#  THZ plugin for SmartHome.py.   http://mknx.github.com/smarthome/
#
#  This plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this plugin. If not, see <http://www.gnu.org/licenses/>.
#########################################################################

import logging
import time
import sys
import datetime
from . import ThzProtocol

logger = logging.getLogger('THZ')

specialRequests = ['logFullScan', 'logRegister']

class THZ():

    def __init__(self, smarthome, serial_port='/dev/ttyUSB0', baudrate=115200, poll_period=300, min_update_period=86400, max_update_period=300):
        self._sh = smarthome
        self._poll_period = int(poll_period)
        self._min_update_period = datetime.timedelta(seconds=int(min_update_period))
        self._max_update_period = datetime.timedelta(seconds=int(max_update_period))
        self._params = {}
        self._thzProtocol = ThzProtocol.ThzProtocol(serial_port, int(baudrate))
        self._msgList = {}
        self._logRegisterId = None

###############################################################################
#
# _update_values() retrieves the values from the heat pump and
#                  updates the corresponding items
#
###############################################################################

    def _update_values(self):
        # request all messages
        newData = self._thzProtocol.requestData(self._msgList)

        now = datetime.datetime.now()

        # update status info
        stats = self._thzProtocol.getStats()
        for param in stats.keys():
            if param in self._params:
                # notify smarthome.py
                for item in self._params[param]['item']:
                    item(stats[param], source='thzRefresh')

        # parse new data and update items
        for param in newData:
            # make sure that the parameter exists
            if param in self._params:
                update = False

                # check for changes to reduce the update rate
                if not self._params[param]['lastValue'] == newData[param]:
                  # value changed
                  # update discrete values on every change
                  if (self._params[param]['lastValue'] in (0,1,2,3) and
                               newData[param] in (0,1,2,3)):
                      update = True
                      logger.debug('Discrete value changed - {0}: {1} => {2}'.format(param, self._params[param]['lastValue'], newData[param]))
                  else:
                    # the value is not discrete, check the minimum period
                    if self._params[param]['lastUpdate'] + self._min_update_period < now:
                      update = True
                      logger.debug('minimum period expired {0}: {1} => {2}'.format(param, self._params[param]['lastValue'], newData[param]))
                else:
                  # no change
                  # check the maximum update period
                  if self._params[param]['lastUpdate'] + self._max_update_period < now:
                      update = True
                      logger.debug('maximum period expired {0}: {1} => {2}'.format(param, self._params[param]['lastValue'], newData[param]))
                      
                if update:
                    # update the history
                    self._params[param]['lastUpdate'] = now
                    self._params[param]['lastValue'] = newData[param]

                    # notify smarthome.py
                    for item in self._params[param]['item']:
                        item(newData[param], source='thzRefresh')

###############################################################################
#
# run() main function
#
###############################################################################
    def run(self):
        self.alive = True
        try:
            self._sh.scheduler.add('THZ', self._update_values,
                               prio=5, cycle=self._poll_period)
            self._update_values()
            logger.info("plugin started")
        except:
            logger.error(
                "thz: plugin start failed - {}".format(sys.exc_info()))

###############################################################################
#
# _logFullScan() requests logging a full scan of the heat pump registers
#
###############################################################################
    def _logFullScan(self):
        #logger.info('logFullScan started')
        self._thzProtocol.logFullScan()
        self._params['logFullScan']['item'][0]('done', source = 'thzRefresh')
        #logger.info('logFullScan completed')

###############################################################################
#
# _logRegister() requests logging the specified heat pump register
#
###############################################################################
    def _logRegister(self):
        #logger.info('logRegister started')
        self._thzProtocol.logRegister(self._logRegisterId)
        self._params['logRegister']['item'][0]('done', source = 'thzRefresh')
        #logger.info('logRegister completed')

###############################################################################
#
# stop() stops the plugin execution
#
###############################################################################
    def stop(self):
        self.alive = False
        self._thzProtocol.stop()
        try:
            self._sh.scheduler.remove('THZ')
        except:
            logger.error(
                "thz: removing thz.update from scheduler failed - {}".format(sys.exc_info()))

###############################################################################
#
# update_item() forwards a new item value to the heat pump
#
###############################################################################
    def update_item(self, item, caller=None, source=None, dest=None):
        #logger.info('{}: caller={}, source={}'.format(item.conf['thz'], caller, source))
        # skip updates triggered by own refresh
        if source == 'thzRefresh':
          return

        try:
            if not self._thzProtocol.getMsgFromParameter(item.conf['thz']) == None:
              self._thzProtocol.sendSetRequest(item.conf['thz'], item())
            elif item.conf['thz'] == 'logFullScan':
              # request logging a full register scan
              # update the item status
              item('processing', source = 'thzRefresh')
              try:
                  self._sh.scheduler.add('ThzScan', self._logFullScan, next=self._sh.now() + datetime.timedelta(milliseconds=10))
                  #logger.info('logFullScan requested')
              except:
                  logger.error( "thz: scheduling logFullScan failed - {}".format(sys.exc_info()))
            elif item.conf['thz'] == 'logRegister':
              # request logging a register
              self._logRegisterId = item()
              # update the item status
              item('processing', source = 'thzRefresh')
              try:
                  self._sh.scheduler.add('ThzRegister', self._logRegister, next=self._sh.now() + datetime.timedelta(milliseconds=10))
                  #logger.info('logRegister requested')
              except:
                  logger.error( "thz: scheduling logRegister failed - {}".format(sys.exc_info()))
            else:
              logger.warning('thz: Invalid parameter name - {}'.format(item.conf['thz']))
        except:
            logger.warning(
                "thz: Setting parameter failed - {}".format(sys.exc_info()))

###############################################################################
#
# parse_item() implements parsing the items associated with plugin parameters
#
###############################################################################
    def parse_item(self, item):
        if 'thz' in item.conf:
            # validate the parameter name

            try:
              msgName = self._thzProtocol.getMsgFromParameter(item.conf['thz'])
            except:
              logger.error('thz: ### parse_item - {}'.format(sys.exc_info()))
            try:
              if msgName:
                  # a message parameter
                  # add the message name to the list
                  self._msgList[msgName] = 1

                  if not item.conf['thz'] in self._params:
                      # new parameter
                      self._params[item.conf['thz']] = {'lastValue': 0,
                                                        'lastUpdate': datetime.datetime.min,
                                                        'item': [item]}
                  else:
                      # parameter exists, associate the new item with it
                      self._params[item.conf['thz']]['item'].append(item)

                  if self._thzProtocol.isParameterWritable(item.conf['thz']):
                    return self.update_item
                  else:
                    return None
              elif (item.conf['thz'] in self._thzProtocol.getStats() or
                    item.conf['thz'] in specialRequests):
                # a plugin parameter
                if not item.conf['thz'] in self._params:
                    # new parameter
                    self._params[item.conf['thz']] = {'lastValue': 0,
                                                      'lastUpdate': datetime.datetime.min,
                                                      'item': [item]}
                else:
                    # parameter exists, associate the new item with it
                    self._params[item.conf['thz']]['item'].append(item)

                # provide the update function for special requests
                if item.conf['thz'] in specialRequests:
                    return self.update_item
              else:
                logger.warning('thz: No such parameter - {}'.format(item.conf['thz']))
            except:
              logger.error('thz: ### parse_item - {}'.format(sys.exc_info()))
 
        return None

