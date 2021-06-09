import pandas as pd


class StockReader:
    def __init__(self, path, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date
        self.path = path

    def read(self):
        stock = pd.read_csv(self.path, encoding='utf8')
        # xử lý và làm sạch dữ liệu
        # dữ liệu cổ phiếu vinamilk
        stock.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        stock['Date'] = pd.to_datetime(stock['Date'], format="%Y%m%d")  # format date
        stock.drop(columns='Ticker', inplace=True)  # drop column
        stock.set_index('Date', inplace=True)  # update index by column
        stock.sort_values(by="Date", inplace=True)
        stock = stock[self.from_date:self.to_date]
        stock['TradingValue'] = stock['Close'] * stock['Volume']
        stock['20D-MA'] = stock['Close'].rolling(20).mean()
        stock['40D-MA'] = stock['Close'].rolling(40).mean()
        stock['UpperBand'] = stock['20D-MA'] + 2 * (stock['Close'].rolling(20).std())
        stock['LowerBand'] = stock['20D-MA'] - 2 * (stock['Close'].rolling(20).std())
        stock.dropna(inplace=True)
        return stock

