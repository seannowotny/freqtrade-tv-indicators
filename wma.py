def wma(self, series: Series, length: int) -> Series:
    norm = 0
    sum = 0

    for i in range(1, length - 1):
        weight = (length - i) * length
        norm = norm + weight
        sum = sum + series.shift(i) * weight

    return sum / norm