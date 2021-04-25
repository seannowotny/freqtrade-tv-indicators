# Heikin Ashi (Candles)

def heikin_ashi(self, df: DataFrame) -> None:
    df_shifted = df.shift()
    df['ha_open'] = (df_shifted['open'] + df_shifted['close']) / 2
    df['ha_close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    df['ha_high'] = df[['high', 'open', 'close']].max(axis=1)
    df['ha_low'] = df[['low', 'open', 'close']].min(axis=1)