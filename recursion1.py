def ntime(n):
    if n == 0:        # base case
        return
    ntime(n-1)        # recursive call
    print(n)          # print after smaller numbers

n = 10
ntime(n)
