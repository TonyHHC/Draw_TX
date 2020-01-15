import gc

from datetime import datetime as dt
from dateutil import parser

import csv
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import mpl_finance as mpf   # old version mpl_finance

import talib
from talib import abstract

from tx_tools import *

class TX_Data():
    def __init__(self):
        pass

    def ReadData(self, strFilename):
        self.m_dfTX_Data = pd.read_csv(strFilename)
        self.m_iTotalRecords = len(self.m_dfTX_Data)
        print(strFilename,'total recoeds :', self.m_iTotalRecords)

    def CalculateTech(self):
        self.m_dfTX_Data['PCT_Close'] = (
            self.m_dfTX_Data['close'].pct_change() * 100)
        self.m_dfTX_Data['PCT_SMA20'] = abstract.SMA(
            self.m_dfTX_Data['PCT_Close'], timeperiod=20)

        # MACD
        self.m_dfTX_Data['MACD_DEF'], self.m_dfTX_Data['MACD_DEM'], self.m_dfTX_Data['MACD_OSC'] = talib.MACD(
            self.m_dfTX_Data['PCT_Close'], fastperiod=12, slowperiod=26, signalperiod=6)

        # KD
        self.m_dfTX_Data['KD_K'], self.m_dfTX_Data['KD_D'] = talib.STOCH(
            self.m_dfTX_Data['high'], self.m_dfTX_Data['low'], self.m_dfTX_Data['close'], fastk_period=27, slowk_period=3, slowd_period=2)
        self.m_dfTX_Data['KD_J'] = 3 * \
            self.m_dfTX_Data['KD_K']-2*self.m_dfTX_Data['KD_D']