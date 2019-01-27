# KMP algorithm
def kmp(txt, pat):
    lps = [0]  # first one assigned to zero
    cur, i = 0, 1
    while i < len(pat):
        if pat[i] == pat[cur]:
            lps.append(cur + 1)
            cur += 1
        else:
            while cur > 0:
                if pat[i] == pat[cur]:
                    lps.append(cur + 1)
                    cur += 1
                    break
                else:
                    cur = lps[cur - 1]
            if cur == 0:
                if pat[i] == pat[0]:
                    cur += 1
                    lps.append(1)
                else:
                    lps.append(0)
        i = i + 1
    # using lps to skip the match
    i, j = 0, 0  # for the index for pat
    while i < len(txt):
        while j < len(pat) and i < len(txt):
            if pat[j] == txt[i]:
                j += 1
                i += 1
            else:
                break
 
        if j == len(pat):  # match
            return i - j
 
        if j < len(pat):  # do not match
            j = lps[j - 1] if j > 0 else 0
            i += 1
 
    return -1
 
 
print kmp("MMMMAAABAAAxxxjx", "AAABAAA")
print kmp("AAABAAAxxxjx", "AAABAAA")
print kmp("MMMAAABAAA", "AAABAAA")
print kmp("AAABAxxxjx", "AAABAAA")