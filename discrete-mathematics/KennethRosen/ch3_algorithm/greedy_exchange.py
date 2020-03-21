"""
procedure change(c1, c2, ..., cr: values of denominations of coins, where
    c1 > c2 > ... > cr ; n: a positive integer)

for i := 1 to r
    di := 0 (di counts the coins of denomination ci used}
    while n >= ci
        di := di + 1 {add a coin of denomination ci}
        n := n - ci
{di is the number of coins of denomination ci in the change for i = 1, 2, ..., r}
"""
