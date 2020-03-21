"""
procedure binary search(x: integer, a1, a2, ... , an: increasing integers)
i := 1 {i is left endpoint of search interval}
j := n {j is right endpoint of search interval}

while i < j 
    m := [(i+j)/2]
    if x > am then i := m+1
    else j := m
if x = ai then location := i
else location := 0

return location{location is the subscript i of the term ai equal to x, or 0 if x is not found}`
"""
