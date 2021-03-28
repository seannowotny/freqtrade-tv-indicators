def hma(self, series: Series, length: int) -> Series:
    h = 2 * self.wma(series, math.floor(length / 2)) - self.wma(series, length)
    hma = self.wma(h, math.floor(math.sqrt(length)))
    return hma