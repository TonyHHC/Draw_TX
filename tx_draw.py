import gc

import wx

from datetime import datetime as dt
from dateutil import parser

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import mpl_finance as mpf   # old version mpl_finance

from tx_tools import *


class Draw_Data():
    def __init__(self, iDPI, iCount):
        self.m_iDPI = iDPI
        self.m_iDrawCount = iCount

        self.m_figSub = []
        self.m_plotSub = []

        self.PrepareFifure([None, None, None])

    def PrepareFifure(self, szPanelPixelSub):
        # create figure if necessary
        if len(self.m_figSub) == 0:
            i = 0
            while i <= 2:
                self.m_figSub.append(Figure())
                self.m_plotSub.append(self.m_figSub[i].add_subplot(111))
                i += 1

        # set width & length
        i = 0
        for szTmp in szPanelPixelSub:
            if szTmp is None:
                self.m_figSub[i].set_size_inches(7.8, 3.6)
            else:
                self.m_figSub[i].set_size_inches(
                    szTmp.width/self.m_iDPI, szTmp.height/self.m_iDPI)

            i += 1

    def Draw(self, dfSource, iStartIndex, objPanelSub):

        dfTmp = dfSource.iloc[iStartIndex:iStartIndex +
                              self.m_iDrawCount-1].reset_index()
        #print(dfTmp)

        for objPlot in self.m_plotSub:
            objPlot.clear()

        if objPanelSub[0] is not None:
            mpf.candlestick2_ohlc(self.m_plotSub[0], dfTmp['open'], dfTmp['high'], dfTmp['low'],
                                  dfTmp['close'], width=0.5, colorup='r', colordown='g', alpha=0.75)
            self.m_plotSub[0].plot(dfTmp.index, dfTmp['Close_SMA5'], color='blue', label='SMA 5')
            self.m_plotSub[0].plot(dfTmp.index, dfTmp['Close_SMA20'], color='black', label='SMA 20')
            self.m_plotSub[0].legend(loc='upper right')
            FigureCanvas(objPanelSub[0], -1, self.m_figSub[0])

        if objPanelSub[1] is not None:
            self.m_plotSub[1].bar(
                dfTmp.index, dfTmp['MACD_OSC'], 0.5, color='black', label='OSC')
            self.m_plotSub[1].plot(dfTmp.index, dfTmp['MACD_DIF'], color='green', label='DIF')
            self.m_plotSub[1].plot(dfTmp.index, dfTmp['MACD_DEM'], color='red', label='DEM')
            self.m_plotSub[1].legend(loc='upper right')
            FigureCanvas(objPanelSub[1], -1, self.m_figSub[1])

        if objPanelSub[2] is not None:
            self.m_plotSub[2].plot(dfTmp.index, dfTmp['KD_K'], color='red', label='K')
            self.m_plotSub[2].plot(dfTmp.index, dfTmp['KD_D'], color='green', label='D')
            self.m_plotSub[2].legend(loc='upper right')
            FigureCanvas(objPanelSub[2], -1, self.m_figSub[2])

        del(dfTmp)

        return dfSource.iloc[iStartIndex]['date'], dfSource.iloc[iStartIndex +
                              self.m_iDrawCount-1]['date']

