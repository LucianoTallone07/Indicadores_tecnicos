def addBollinger(data, ruedas=20, desvios=2):
    data = data.copy()
    data['sma_20'] = data["Adj Close"].rolling(20).mean()
    volatilidad = data["Adj Close"].rolling(20).std()
    data['boll_inf'] = data.sma_20 - 2 * volatilidad
    data['boll_sup'] = data.sma_20 + 2 * volatilidad
    data.dropna(inplace=True)
    return data
  
  
  def addMACD(data, slow=26, fast=12, suavizado=9):
    '''
    El MACD toma la columna "Close" para hacer los calculos. Enviar datos ajustados
    '''
    df = data.copy()
    df['ema_fast'] = df.Close.ewm(span=fast).mean()
    df['ema_slow'] = df.Close.ewm(span=slow).mean()
    data['macd'] = df.ema_fast - df.ema_slow
    data['signal'] = data.macd.rolling(suavizado).mean()
    data['histograma'] = data.macd - data.signal
    data = data.dropna().round(2)
    return data
