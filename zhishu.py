def zhishu_1000():
    number=[]
    for c in range(1001):
        if c <2:
            continue
        for r in range(2,c):
            if c % r==0:
                break
            else:
                number.append(c)
    return sum(number)
print("1000以内的质数为:",zhishu_1000())



