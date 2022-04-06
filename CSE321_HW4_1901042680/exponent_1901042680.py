def exponent(a, n):
    if n == 0:
        return 1
    else:
        m = exponent(a, n//2)
        if n%2 == 0:
            return m*m
        else:
            return m*m*a
    
print("res: ", exponent(3,2))