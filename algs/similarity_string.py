def Solution(a, b):
    # avoid repeatedly evoking the function
    if a == "" or b == "":
        return max(len(a), len(b))
 
    if a[0] == b[0]:
        return Solution(a[1:], b[1:])
    else:
        p1 = Solution(a[1:], b)
        p2 = Solution(a[1:], b[1:])
        p3 = Solution(a, b[1:])
 
        return 1 + min(p1, p2, p3)
 
 
if __name__ == "__main__":
    print Solution("alutdon", "abcde")