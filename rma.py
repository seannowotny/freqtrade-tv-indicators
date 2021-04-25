# RMA (Moving Average used in TV RSI)

def rma(self, series: Series, length: int) -> Series:
    alpha = 1.0 / length

    for i in range(1, series.size):
        series.iloc[i] = series.iloc[i] * alpha + (1 - alpha) * (
            series.iloc[i - 1] if not pd.isna(series.iloc[i - 1]) else 0)

    return series