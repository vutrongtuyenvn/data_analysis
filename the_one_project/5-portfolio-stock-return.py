import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd

# lấy dữ liệu cổ phiếu
portfolios = ['datas/VNM.csv', 'datas/TCB.csv', 'datas/VIC.csv']
stock_temp = pd.DataFrame()
for item in portfolios:
    stock_temp[item] = pd.read_csv(item, parse_dates=True, index_col='Date')['Close']

# làm sạch và sắp xếp dữ liệu
stock_temp.dropna(inplace=True)
stock_temp.columns = ['VNM', 'TCB', 'VIC']  # -> đặt lại column name
stock_temp.sort_index(ascending=True, inplace=True)  # -> sắp xếp lại theo thời gian

stock = stock_temp / stock_temp.iloc[0]  # -> chuyển giá trị cổ phiếu về giá trị chung

# tính  tỉ suất sinh lời theo ngày simple return của từng cổ phiếu trong nhóm
stock_return = (stock / stock.shift(1)) - 1  # tính  tỉ suất sinh lời theo ngày simple return của từng cổ phiếu
stock_return.dropna(inplace=True)  # loại bỏ giá trị NaN
stock_return_avg = stock_return.mean()*252  # tính tỉ suất sinh lời trung bình theo ngày của từng cổ phiếu
print('.......................Bảng thống kê tỉ suất sinh lời năm của từng cổ phiếu trong nhóm.......................')
print(stock_return_avg)

# tính tỉ suất theo tỉ trọng tỉ trọng của nhóm cổ phiếu (giả sử tỉ trọng là (0.3,0.2,0.5))
stock_weight = np.array([0.1, 0.6, 0.3])
portfolio_return = np.dot(stock_return, stock_weight) # tỉ suất sinh lời treo tỉ trọng
portfolio_return_avg = np.dot(stock_return_avg, stock_weight) # tỉ suất sinh lời trung bình theo tỉ trọng
print('.......................Tỉ suất sinh lời trung bình năm của nhóm cổ phiếu theo tỉ trọng.......................')
print(portfolio_return_avg)


# biểu đồ chi tiết
stock.plot(kind='line', figsize=(12, 8), title='Biểu đồ biến động giá trị cổ phiếu của VNM,TCB,VIC')
stock_return.plot(kind='line', figsize=(12, 8), title='Biểu đồ tỉ suất sinh lợi nhuận ngày của VNM,TCB,VIC')
plt.show()
