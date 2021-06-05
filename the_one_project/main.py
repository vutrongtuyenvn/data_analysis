import numpy as np
import pandas as pd

VNM = pd.read_csv('VNM_STOCK.csv', encoding='utf8')
print('..............thông tin dữ liệu đầu tiên...................')
print(VNM.head())
print('..............thông tin chung của dữ liệu...................')
print(VNM.info())
print('.............thông tin phân tích cơ bản....................')
print(VNM.describe())

# sắp xếp chứng khoán theo ngày
print('................thông tin sắp xếp chứng khoán theo ngày.................')
VNM['ngay_giao_dich']=pd.to_datetime(VNM['ngay_giao_dich'])
print(VNM.sort_values(by=['ngay_giao_dich']))
