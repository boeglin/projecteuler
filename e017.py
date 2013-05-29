#!/usr/bin/python

unit = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}

def num(n):
    
    if n >= 1000:
        ac = n / 1000
        dc = n % 1000
        return num(ac) + unit[1000] + num(dc)

    if n >= 100:
        ac = n / 100
        dc = n % 100
        ret = num(ac) + unit[100]
        if dc:
            ret += 'and' + num(dc)
        return ret

    if n in unit:
        return unit[n]

    dec = n / 10 * 10
    uni = n % 10

    return num(dec) + num(uni)

print num(342), num(115)
print len(num(342)), len(num(115))

acc = 0
for i in xrange(1001):
    acc += len(num(i))
print acc

