def vwma(self, dataframe: DataFrame, length: int) -> Series:
    return ta.SMA(dataframe['close'] * dataframe['volume'], length) / ta.SMA(dataframe['volume'], length)