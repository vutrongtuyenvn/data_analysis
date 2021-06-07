import statistics
import pandas as pd

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
