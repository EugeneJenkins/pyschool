def getMaxNumber(numbers):
    a = sorted(numbers)
    b = len(numbers)
    if b == 0:
        return 'N.A'
    else:
        return a[b-1]