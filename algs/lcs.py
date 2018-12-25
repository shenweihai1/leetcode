
# excellent explanation: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# longest common subsequence
def lcs(X, Y, m, n):
    if m > len(X) - 1 or n > len(Y) - 1:
        return 0

    if X[m] == Y[n]:
        return 1 + lcs(X, Y, m + 1, n + 1)
    else:
        return max(lcs(X, Y, m + 1, n), lcs(X, Y, m, n + 1), lcs(X, Y, m + 1, n + 1))
  
if __name__ == "__main__":
    X = "AWGTTOBNM"
    Y = "ZAGZZTNBN"
    print "Length of LCS is ", lcs(X , Y, 0, 0)