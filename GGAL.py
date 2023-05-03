"""El siguiente script proporcione el dólar CCL ("Contado con liquidación"), uno de los dólares financieros de Argentina. Está
calculado en base al precio de la acción cotizante en USA (ADR GGAL, NASDAQ), el precio en la bolsa local (GGAL.BA) y un 
factor de conversión (10 para este caso del banco GGAL), según base cierre del último día hábil"""

import pandas as pd 
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override() # This step is made to allow the Yahoo API to work (because it was discontinued)
import datetime as dt 

tickers = ['GGAL.BA', 'GGAL'] # I chose bank stocks from Argentina, in this case, Banco Galicia. 
start = dt.datetime(2023, 1, 3)
 
data = pdr.get_data_yahoo(tickers, start)
data.info() # info method to get a sense of the data frame obtained via Yahoo
data = data['Adj Close']
data.head(120) # I want the first 10 dataframe rows to be shown

#DOLAR MEP FORMULA CCL= GGAL.BA / GGAL * 10

df_CCL = pd.DataFrame(data['GGAL.BA'] / data['GGAL'] * 10, columns=['CCL'])
print(type(df_CCL))

print(df_CCL)
