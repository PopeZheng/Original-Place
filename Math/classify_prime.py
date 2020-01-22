# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:02:02 2020

@author: Pope  Zheng
"""

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
        
def main():
    file1 = open('a.txt','w')
    file2 = open('b.txt','w')
    file3 = open('c.txt','w')
    
    for i in range(1,10001):
        if is_prime(i):
            if i in range(2,100):
                file1.write(str(i)+'\n')
            elif i  in range(100,1000):
                file2.write(str(i)+'\n')
            elif i  in range(1000,10000):
                file3.write(str(i)+'\n')
            else:
                pass
    
    file1.close()
    file2.close()
    file3.close()
    
if __name__ == '__main__':
    main()
    
    
    
    
    