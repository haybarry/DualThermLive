'''
Created on 28Jun.,2018

@author: dels
'''

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPixmap # , QBrush, QPen
from PyQt5.QtCore import Qt

import random

degc = ''
topl=200
topr=200
highl=10
highr=10


class ThermView(QWidget):
    
    lcel = 0
    rcel = 0
       
    def __init__(self, lcel=0, rcel=0 ):
        super().__init__()
        self.func1 = None
        self.func2 = None
        self.initUI()
        self.lcel = lcel
        self.rcel = rcel
        self.mPixmap = QPixmap()

        
    def initUI(self):      
        self.setGeometry(0, 0, 320, 240)
        self.setWindowTitle('Dual Therm')
        self.mModified = True
        self.show()       # this trigger 'paintEvent()'

    def processMsg(self, index, payload):
        value = int(payload)
        if index == 0:
            self.lcel = value
        if index == 1:
            self.rcel = value
        self.func1 = (leftbulb,self.lcel)
        self.func2 = (rightbulb,self.rcel)
        self.mModified = True
        self.update()       # this trigger 'paintEvent()'

    def paintEvent(self, e):
        if self.mModified:
            pixmap = QPixmap(self.size())
            pixmap.fill(Qt.white)
            painter = QPainter(pixmap)
            self.drawTherm(painter)
            if self.func1 != None :
                (action,value) = self.func1
                action( painter, value)
            if self.func2 != None :
                (action,value) = self.func2
                action( painter, value)
            self.mPixmap = pixmap
            self.mModified = False
            
        qp = QPainter(self)
        qp.drawPixmap(0, 0, self.mPixmap)
    
    def drawTherm(self, qp):
        col = QColor(0, 0, 0)
        qp.setPen(col)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawEllipse(145, 200, 40, 40)
        qp.drawLine(155, 80, 155, 202)
        qp.drawLine(175, 80, 175, 202)
        for nn in range (0, 41):
            bar = 80 + nn * 3
            if nn % 10 == 0:
                startbar = 147
            elif nn % 5 == 0:
                startbar = 150
            else:
                startbar = 152 
            qp.drawLine(startbar, bar, 155, bar)
        qp.setPen(Qt.NoPen)
#        rightbulb(qp, int(2*random.uniform(11,24))/2)

def leftbulb(qp, lcel): 
    print( "{0} {1}".format("leftbulb",lcel) )
    topl = 80 + (40-lcel)*3
    highl = lcel*3 + 5   
    qp.setBrush(QColor(200, 0, 0))
    # qp.save()
    qp.drawRect(156,topl,10,highl)
    # qp.restore()
    
def rightbulb(qp, rcel): 
    print( "{0} {1}".format("rightbulb",rcel) )
    topr = 80 + (40-rcel)*3
    highr = rcel*3 + 5   
    qp.setBrush(QColor(200, 0, 0))
    #qp.save()
    qp.drawRect(166,topr,9,highr)
    #qp.restore()

        