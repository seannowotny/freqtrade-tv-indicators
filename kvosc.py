# Modified Kaufmann VOL OSC
# Based on https://www.tradingview.com/script/rycTE19Y-Kaufman-modified-volume-Oscillator/ by RafaelZioni

length = 14

change1: Series = (dataframe['volume'] - dataframe['volume'].shift(length)).abs()
change2: float = (dataframe['volume'] - dataframe['volume'].shift()).abs().rolling(length).sum()

er: Series = change1 / change2

def kama(series: Series) -> Series:
    ak: Series = er * series
    for i in range(1, ak.size):
        ak[i] = ak[i] + (1 - er[i]) * (ak[i - 1] if not pd.isna(ak[i - 1]) else ak[i])
    return ak

def st(series: Series) -> Series:
    return np.sqrt(kama(series ** 2) - (kama(series) ** 2))

a: Series = kama(dataframe['index'] * dataframe['close']) - kama(dataframe['index']) * kama(dataframe['close'])

b: Series = st(dataframe['index']) * st(dataframe['close'])

x: Series = a - b / dataframe['volume']

len = 25

signal: Series = ta.EMA(x, len)

dataframe['kvoscPositive'] = ((x >= 0) & (x > signal)) | ((x > 0) & (x < signal))
dataframe['kvoscLong'] = qtpylib.crossed_above(x, signal)
dataframe['signal'] = signal