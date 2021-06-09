import matplotlib.pyplot as plt
import pandas as pd
from function import StockReader

VNM = StockReader("datas/VNM.csv", '2018-06-01', '2021-06-01').read()
# TCB = StockReader("datas/TCB.csv", '2018-06-01', '2021-06-01').read()
# VIC = StockReader("datas/VIC.csv", '2018-06-01', '2021-06-01').read()
print('............................Bảng cổ phiếu VNM.....................................')
print(VNM)
# Analysis VNM
print('............................Một số biểu đồ cơ bản.....................................')
VNM['Close'].plot(kind='line', figsize=(12, 8), title='Map Close of VNM')
plt.show()
VNM['Volume'].plot(kind='line', figsize=(12, 8), title='Map Volume of VNM')
plt.show()
VNM['TradingValue'].plot(kind='line', figsize=(12, 8), title='Map TradingValue of VNM')
plt.show()
VNM[['Close','20D-MA','40D-MA']].plot(kind='line',figsize=(12, 8),title='Map Close 20D & 40D of VNM')
plt.show()
VNM[['Close','20D-MA','40D-MA','UpperBand','LowerBand']].plot(figsize=(12,8),title='Map John Bollinger')
plt.show()

vnm_max = VNM['Close'].min()
vnm_max = VNM['Close'].max()
vnm_avg = VNM['Close'].mean()
vnm_index_max = VNM['Close'].idxmax()

