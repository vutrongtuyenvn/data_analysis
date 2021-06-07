import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mlt

VNM = pd.read_csv('datas/VNM_STOCK_DATA.csv', encoding='utf8')

# thông tin chung
print('..............thông tin dữ liệu đầu tiên...................')
print(VNM.head())
print('..............thông tin chung của dữ liệu...................')
print(VNM.info())
print('.............thông tin phân tích cơ bản....................')
print(VNM.describe())
# print(VNM.describe().transpose())

# xử lý và làm sạch dữ liệu
VNM.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
VNM['Date'] = pd.to_datetime(VNM['Date'], format="%Y%m%d")  # format date
VNM.drop(columns='Ticker', inplace=True)  # drop column
VNM.set_index('Date', inplace=True)  # update index by column
VNM.sort_values(by="Date", inplace=True)

# xử lý missing value
VNM.isnull().sum()  # check missing value
VNM.dropna(inplace=True)  # xóa missing value
VNM.fillna(value=VNM.shift(-1))  # thay thế mising value bằng giá trị gần nhất trước đó

# xử lý dữ liệu biên

print('.............dữ liệu sau khi làm sạch....................')
print(VNM)

# xử lý filter dữ liệu theo thời gian

print(VNM.resample(rule='M').mean())  # dữ liệu giá trung bình theo tháng (rule='M' month....)
print(VNM.resample(rule='M').min())  # dữ liệu giá thấp nhất theo tháng (rule='M' month....)
print(VNM.resample(rule='M').max())  # dữ liệu giá cao nhất theo tháng (rule='M' month....)

# lấy giá trị trung bình 30 ngày của giá đóng cửa cổ phiểu VNM

VNM['30D-MA'] = VNM['Close'].rolling(window=30).mean()
print(VNM)

# vẽ biểu đồ cổ phiếu và giá trị trung bình 30 ngày trước đó ở trên

VNM['Close'].plot(figsize=(12, 6), title='Bieu do co phieu VNM')
VNM['30D-MA'].plot()
plt.legend()
plt.show()

# vẽ biểu đồ  bollinger band
# giá đóng cửa trung bình 20 ngày trước đó
VNM['20D-MA'] = VNM['Close'].rolling(20).mean()
# dải băng trên upperband
VNM['Upperband'] = VNM['20D-MA']+2*(VNM['Close'].rolling(20).std())
VNM['Lowerband'] = VNM['20D-MA']-2*(VNM['Close'].rolling(20).std())

VNM[['Close','20D-MA','Upperband','Lowerband']].tail(200).plot(figsize=(12,8),title='Bieu do bollinger band')
plt.show()
