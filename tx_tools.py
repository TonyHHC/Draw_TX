import gc

from datetime import datetime as dt
from dateutil import parser

import csv
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import talib
from talib import abstract


# 取得指定日期 前 n 筆 或 後 n 筆 資料
def Find_n_Rows(dfSource, strDate, iNumRows):
    iIndex = dfSource.loc[dfSource['date'] >= strDate].index.values[0]
    if iNumRows < 0:
        dfTmp = dfSource.iloc[iIndex + iNumRows + 1:iIndex + 1]
    else:
        dfTmp = dfSource.iloc[iIndex:iIndex + iNumRows]
    return dfTmp

# 將資料分割成一個個區塊
def Split_DataFrame_Datas(dfSource, lstFields, iFragmentSize):
    iSourceSize = len(dfSource.index)
    iIndex = iFragmentSize
    lstAns = list()
    while iIndex < iSourceSize:
        dfTmp = dfSource[iIndex - iFragmentSize:iIndex]
        lstAns.append(dfTmp[lstFields])
        iIndex += 1

    return lstAns
