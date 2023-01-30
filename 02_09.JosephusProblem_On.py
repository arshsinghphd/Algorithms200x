## Josephus Problem

## Find the position of the survivor in the vicious series of killings
## described by Flavius Josephus, the first-century historian and head
## of Jewish forces in Galilee.

## Input: Natural numbers n and k.
## n rebels standing in a circle.
## Rebels are being eliminated in such a way that every k-th still
## alive rebel around the circle is killed until only one rebel left.
## Rebels are killed clockwise starting from rebel 0, i.e., rebel k−1
## is killed first.

## Output: The position of the survivor, denoted Josephus(n,k).

def josephus(n, k):
    if n==1: # Base case for recursion if k != 2
        return 0
    if k==2: # Binary Joseph
        i = 0
        while 2**i < n:
            i += 1             
        return (n % (2**(i-1))) *2
    return (josephus(n - 1, k) + k) % n

if __name__=='__main__':
    f = open('02_09.test.txt','r')
    for line in f:
        n, k, ans=map(int, line.strip().split())
        print(n, k)
        print(josephus(n, k))
        print(josephus(n, k) == ans)
        
    
