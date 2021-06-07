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

# Tính tỉ suất sinh lời của cổ phiếu simple return
VNM['SimpleReturn'] = VNM['Close'] / VNM['Close'].shift(1) - 1
VNM_DailySimpleReturn = VNM['SimpleReturn'].mean();
VNM_YearSimpleReturn = VNM_DailySimpleReturn * 252;
print('Tỉ suất sinh lời ngày trung bình VNM(2006->2021):', VNM_DailySimpleReturn)
print('Tỉ suất sinh lời năm trung bình VNM(2006->2021):', VNM_YearSimpleReturn)

# Tính tỉ suất sinh lời cổ phiếu log return
VNM['LogReturn'] = np.log(VNM['Close'] / VNM['Close'].shift(1))
VNM_DailyLogReturn = VNM['LogReturn'].mean();
VNM_YearLogReturn = VNM_DailyLogReturn * 252;
print('Tỉ suất sinh lời (log) ngày trung bình VNM(2006->2021):', VNM_DailyLogReturn)
print('Tỉ suất sinh lời (log) năm trung bình VNM(2006->2021):', VNM_YearLogReturn)

VNM[['SimpleReturn', 'LogReturn']].plot(figsize=(12, 8), title="Biểu đồ tỉ suất sinh lời ngày của cổ phiếu VNM")
plt.show()
