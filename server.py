#!/usr/bin/env python2

import os
import sys
import datetime
import time
import re

from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
from dxlclient.callbacks import EventCallback
from common import *

clientPath = os.path.dirname(os.path.realpath(__file__))

class loggerCallback(EventCallback):

    def on_event(self, event):

      # fileformat yyyymmdd.log eg 27072017
      fileName = datetime.datetime.now().strftime("%Y%m%d.log")
      logPath = os.path.join(clientPath, os.sep, 'logs', os.sep, fileName)
      tStamp = datetime.datetime.now().strftime("%H:%M:%S")

      # filter out connect - disconnect
      if not event.destination_topic.endswith("connect"):
          
          # write and close immediately
          with open(logPath, 'a') as file:
              file.write("%s;%s;%s;%s;%s;%s\n" % (tStamp, event.destination_topic, event.source_client_id, \
                        event.source_broker_id, event.message_type, re.sub(r"(?m)[\x00\n\r]+", "", event.payload.decode())))
              file.close()


if __name__ == '__main__':

    # standard opendxl client conf
    config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

    # inform user
    print ("Logpath: %s" % clientPath + os.sep + 'logs')

    # connect, subscribe to all MQTT topics with callback 
    with DxlClient(config) as client:
      
      client.connect()
      client.add_event_callback("#", loggerCallback())

      try:
        while 1:
          time.sleep(0.1)
      except (KeyboardInterrupt, EOFError) as e:
          sys.exit(0)
