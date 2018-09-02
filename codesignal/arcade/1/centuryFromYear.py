def centuryFromYear(year):
    if year % 100:
        res = year // 100 + 1
    else:
        res = year // 100

    return res