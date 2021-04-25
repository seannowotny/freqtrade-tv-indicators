# Smoothed Directional Movement Index
# https://www.tradingview.com/script/9L6Wof1i-Smoothed-Directional-Movement-Index/

def sdmi(self, high: Series, low: Series, close: Series) -> Callable:
    def fn(length: int, smooth_length=5) -> DataFrame:
        dmi: DataFrame = self.dmi(high, low, close, length)
        return pd.DataFrame({
            'plus': ta.SMA(dmi['plus'], smooth_length),
            'minus': ta.SMA(dmi['minus'], smooth_length)
        })

    return fn