m = int(input())
P = input()
n = int(input())
S = input()
ne = [0]
#P是模式串,S是主串,ne是next数组
def build_next():
    i = 1
    j = 0
    while i < m:
        if P[i] == P[j]:
            j += 1
            i += 1
            ne.append(j)
        else:
            if j:
                j = ne[j - 1]
            else:
                ne.append(0)
                i += 1


def kmp():
    build_next()
    i = 0
    j = 0
    while i < n:
        if S[i] == P[j]:
            i += 1
            j += 1
        else:
            if j:
                j = ne[j - 1]
            else:
                i += 1
        if j == m:
            print(i - j, end=' ')
            j = ne[j - 1]
kmp()