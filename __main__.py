#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication

from MQTTClient import MQTTClient

from ThermView import ThermView

#import time
import sys
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    widget = ThermView.ThermView()
    
    mqttClient = MQTTClient.MQTTClient(widget)
    mqttClient.start()
    
    sys.exit(app.exec_())
    