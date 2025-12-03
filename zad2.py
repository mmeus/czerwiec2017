def reg(w):
    if len(w) == 1:
        return 1
    elif len(w) % 2 == 1:
        w = w[:(len(w)//2)] + 'A' + w[(len(w)//2 + 1):]
    if w[::] == w[::-1]:
        return reg(w[:(len(w)//2)]) + 1
    else:
        return 0
#print(reg('BABBAB'))
A = ['BABBAB', 'BABBBB', 'BAAAAB', 'B', 'BBB', 'AAAAAAAA']
for s in A:
    print(reg(s))