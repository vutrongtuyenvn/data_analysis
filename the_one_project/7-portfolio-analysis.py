import matplotlib.pyplot as plt
import pandas as pd
from function import StockReader

VNM = StockReader("datas/VNM.csv", '2018-06-01', '2021-06-01').read()
TCB = StockReader("datas/TCB.csv", '2018-06-01', '2021-06-01').read()
VIC = StockReader("datas/VIC.csv", '2018-06-01', '2021-06-01').read()