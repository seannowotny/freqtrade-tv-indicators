# Directional Movement Index

# There are some variations between this indicator and the one on TV,
# should you find a fix for this please open a PR / Issue or message me on Discord

def dmi(self, high: Series, low: Series, close: Series, length: int) -> DataFrame:
    trur = self.rma(pd.Series(ta.TRANGE(high, low, close)), length)

    up = high.diff()
    down = low.diff() * -1

    plusDM = up.where((up > down) & (up > 0), other=0)
    minusDM = down.where((down > up) & (down > 0), other=0)

    plus = (100 * self.rma(plusDM, length) / trur).fillna(method='ffill')
    minus = (100 * self.rma(minusDM, length) / trur).fillna(method='ffill')

    return pd.DataFrame({
        'plus': plus,
        'minus': minus
    })