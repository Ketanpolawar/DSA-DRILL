st = "abcdcabdtnsvsacfsc"
l = 0
r = 0
mlen = 0
s = set()

while r < len(st):
    if st[r] not in s:
        s.add(st[r])
        mlen = max(mlen, len(s))
        r += 1
    else:
        while st[r] in s:
            s.remove(st[l])
            l += 1
        s.add(st[r])
        r += 1

print(mlen)
