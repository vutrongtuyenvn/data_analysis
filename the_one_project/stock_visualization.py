import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# tạo và xử lý và làm sạch dữ liệu cổ phiếu VNM
VNM = pd.read_csv('datas/VNM_STOCK_DATA.csv', encoding='utf8')
VNM.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
VNM['Date'] = pd.to_datetime(VNM['Date'], format="%Y%m%d")  # format date
VNM.drop(columns='Ticker', inplace=True)  # drop column
VNM.set_index('Date', inplace=True)  # update index by column
VNM.sort_values(by="Date", inplace=True)

# Tạo dữ liệu data frame về tỷ số điện thoại
random_array = np.random.randint(100, size=10)
random_array = random_array.reshape(5, 2)
mobile_datas = pd.DataFrame(random_array, index=['2016', '2017', '2018', '2019', '2020'], columns=['Android', 'IOS'])

# vẽ biểu đồ line plot cho giá đóng cửa
VNM['Close'].plot(kind='line', figsize=(12, 8), title='Biểu đồ giá đóng cửa cổ phiếu ', color="green")

# vẽ biểu đồ subplot cho giá đóng cửa và khối lượng giao dịch
VNM[['Close', 'Volume']].plot(kind='line', figsize=(12, 8), subplots=True)

# vẽ biểu đồ bar plot cho khối lượng giao dịch
VNM.drop('Volume', axis=1).plot.bar(title='Biểu đồ bar cho khối lượng giao dịch')

# vẽ biểu đồ histogram cho khối lượng giao dịch
VNM['Volume'].plot(kind='hist',bins=30,title='Biểu đồ histogram cho khối lượng giao dịch')

# vẽ biểu đồ bar cho dữ liệu thị trường điện
mobile_datas.plot.bar(figsize=(12, 8), title='Tỉ lệ điện thoại trên thị trường (bar)')

# vẽ biểu đồ stack bar cho dữ liệu thị trường điện
mobile_datas.plot.bar(figsize=(12, 8), stacked=True, title='Tỉ lệ điện thoại trên thị trường (stack bar)')

# vẽ biểu đồ area cho dữ liệu thị trường điện thoại
mobile_datas.plot(kind='area', figsize=(12, 8), title='Tỉ lệ điện thoại trên thị trường (stack bar)')

# vẽ biểu đồ scater plot cho dư liệu thị trường điện thoại
mobile_datas.plot(kind='scatter', figsize=(12, 8), x='Android', y='IOS', s=50, c='Android', cmap='rainbow')

# vẽ biểu đồ box plot cho dữ liệu thị trường điện thoại
mobile_datas[['Android', 'IOS']].plot(kind='box', figsize=(12, 8))

plt.show()
