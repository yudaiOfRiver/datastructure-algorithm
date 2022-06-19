def cumulativeSum(a: list) -> list:

    s = [0]
    curSum = 0
    for ai in a:
        curSum += ai
        s.append(curSum)
    return s


if __name__ == '__main__':
    a = [1,3,5,2,5,6]
    print(cumulativeSum(a))
