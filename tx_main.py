import gc

import wx

from datetime import datetime as dt
from dateutil import parser

import csv
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import mpl_finance as mpf   # old version mpl_finance

import talib
from talib import abstract

from tx_tools import *
from tx_data import *
from tx_draw import *

import frmMain

import sys
from PyQt5.QtWidgets import QApplication


class MainFrame(frmMain.frmMain):
    def __init__(self, parent, objTX_Data, objDraw_Data):
        self.m_objTX_Data = objTX_Data
        self.m_objDraw_Data = objDraw_Data

        self.m_bOnSize = False

        frmMain.frmMain.__init__(self, parent)

    def SetScrollBarRange(self, iRange):
        self.m_scrollBarDate.SetScrollbar(0, 10, iRange, 10, True)

    def DrawPanel(self):
        tpPanelSub = [self.m_panelSub0, self.m_panelSub1, self.m_panelSub2]
        tpPanelSubSize = []

        for objTmp in tpPanelSub:
            szTmp = objTmp.GetSize()
            tpPanelSubSize.append(szTmp)

        self.m_objDraw_Data.PrepareFigure(tpPanelSubSize)

        iIndex = self.m_scrollBarDate.GetThumbPosition()
        strStartDate, strEndDate = self.m_objDraw_Data.Draw(
            self.m_objTX_Data.m_dfTX_Data, iIndex, tpPanelSub)

        self.m_txtDrawInterval.SetLabel(strStartDate + ' - ' + strEndDate)

    # 事件觸發函式

    def OnPaint(self, event):
        if self.m_bOnSize == True:
            self.DrawPanel()
            self.m_bOnSize = False

        event.Skip()

    def OnSize(self, event):
        self.m_bOnSize = True
        event.Skip()

    def OnScrollChanged(self, event):
        self.DrawPanel()
        event.Skip()


def main():

    # get screen DPI
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()
    print('DPI : ', dpi)
    app.quit()

    # read data
    objTX_Data = TX_Data()
    objTX_Data.ReadData("./source/AI_Log_15n_50.csv")
    objTX_Data.CalculateTech()

    objDraw_Data = Draw_Data(dpi, 100)

    # prepare wxPython framework
    app = wx.App(False)
    frame = MainFrame(None, objTX_Data, objDraw_Data)
    frame.SetScrollBarRange(objTX_Data.m_iTotalRecords)
    frame.Show(True)

    # start the applications
    app.MainLoop()


if __name__ == '__main__':
    main()
