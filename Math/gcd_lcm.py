def gcd(x,y):
    if x>y:
        for i in range(y,0,-1):
            if x % i == 0 and y % i == 0 :
                break
        return i
    if x == y:
        return x
    if x < y:
        for i in range(x,0,-1):
            if x % i == 0 and y % i ==0:
                break
        return i
    
def lcm(x,y):
    return x*y // gcd(x,y)
    
            
            