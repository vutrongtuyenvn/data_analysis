import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

VNM = pd.read_csv('datas/VNM_STOCK_DATA.csv', encoding='utf8')
# xử lý và làm sạch dữ liệu
VNM.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
VNM['Date'] = pd.to_datetime(VNM['Date'], format="%Y%m%d")  # format date
VNM.drop(columns='Ticker', inplace=True)  # drop column
VNM.set_index('Date', inplace=True)  # update index by column
VNM.sort_values(by="Date", inplace=True)