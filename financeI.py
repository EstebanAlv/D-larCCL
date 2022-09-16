"""El siguiente script proporcione el dólar CCL ("Contado con liquidación"), uno de los dólares financieros de Argentina. Está
calculado en base al precio de la acción cotizante en USA (ADR GGAL, NASDAQ), el precio en la bolsa local (GGAL.BA) y un 
factor de conversión (10 para este caso del banco GGAL), según base cierre del último día hábil"""

import yfinance as yf

ggal_df = yf.download('GGAL', start ='2022-05-01', end = '2022-05-27', progress = False)
ggalba_df = yf.download('GGAL.BA', start ='2022-05-01', end = '2022-05-27', progress = False)

print(ggal_df.head())
print(ggalba_df.head())
print(ggal_df.iat[0,3])
print(ggalba_df.iat[0,3])

#DOLAR MEP FORMULA CCL= GGAL.BA / GGAL * 10

dccl = (ggalba_df.iat[0,3] / ggal_df.iat[0,3]) * 10

print('CCL(GGAL) :', round(dccl,2))
