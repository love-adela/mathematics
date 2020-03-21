"""
procedure insertion sort (a1, a2, ... , an: real numbers with n>=2)
for j := 2 to n
    i := 1
    while aj > ai
        i := i +1 
    m := aj
    for k := 0 to j - i -1
        a(j-k) := a (j-k-1)
    ai := m
{a1, ..., an is in  increasing order}
"""
