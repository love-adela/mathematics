"""
procedure schedule(s1 <= s2 <= ... <= sn: start times of talks, 
        e1 <= e2 <= ... <= en: ending times of talks)

sort talks by finish time and reorder so that e1 <= e2 <= ... <= en
S := 0
for j := 1 to n
    if talk j is compatible with S then 
        S := S U {talk j}
return S {S is the set of talks scheduled}
"""
