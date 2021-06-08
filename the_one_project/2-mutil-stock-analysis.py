import matplotlib.pyplot as plt
import pandas as pd

VNM = pd.read_csv('datas/VNM.csv', encoding='utf8')

# xử lý và làm sạch dữ liệu
# dữ liệu cổ phiếu vinamilk
VNM.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
VNM['Date'] = pd.to_datetime(VNM['Date'], format="%Y%m%d")  # format date
VNM=VNM.loc[(VNM['Date'] >= '2018-06-04')]
VNM.drop(columns='Ticker', inplace=True)  # drop column
VNM.set_index('Date', inplace=True)  # update index by column
VNM.sort_values(by="Date", inplace=True)

# dữ liệu cổ phiếu Techcombank
TCB = pd.read_csv('datas/TCB.csv', encoding='utf8')
TCB.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
TCB['Date'] = pd.to_datetime(TCB['Date'], format="%Y%m%d")  # format date
TCB=TCB.loc[(TCB['Date'] >= '2018-06-04')]
TCB.drop(columns='Ticker', inplace=True)  # drop column
TCB.set_index('Date', inplace=True)  # update index by column
TCB.sort_values(by="Date", inplace=True)


# dữ liệu cổ phiếu Vingroup
VIC = pd.read_csv('datas/VIC.csv', encoding='utf8')
VIC.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
VIC['Date'] = pd.to_datetime(VIC['Date'], format="%Y%m%d")  # format date
VIC=VIC.loc[(VIC['Date'] >= '2018-06-04')]
VIC.drop(columns='Ticker', inplace=True)  # drop column
VIC.set_index('Date', inplace=True)  # update index by column
VIC.sort_values(by="Date", inplace=True)

print('.........................Vinamilk..................................')
print(VNM)
print('.........................Techcombank.................................')
print(TCB)
print('.........................Vingroup.................................')
print(VIC)



