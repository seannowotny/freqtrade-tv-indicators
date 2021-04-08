# Stochastic RSI

smoothK = 3
smoothD = 3
lengthRSI = 10
lengthStoch = 11

dataframe['rsi'] = ta.RSI(dataframe, timeperiod=lengthRSI)

stochrsi = (dataframe['rsi'] - dataframe['rsi'].rolling(lengthStoch).min()) / (
        dataframe['rsi'].rolling(lengthStoch).max() - dataframe['rsi'].rolling(lengthStoch).min())

dataframe['srsi_k'] = stochrsi.rolling(smoothK).mean() * 100
dataframe['srsi_d'] = dataframe['srsi_k'].rolling(smoothD).mean()

dataframe['srsi_top'] = 80
dataframe['srsi_bottom'] = 20