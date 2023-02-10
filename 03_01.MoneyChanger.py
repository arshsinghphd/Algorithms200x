def moneyChanger(money):
    '''
    problem: a non-negative integer money, find the minimum number of coins with
    denominations 1, 5, and 10 that changes money.
    '''
     
    denominations = [10,5,1]
    change = 0
    while len(denominations) > 0:
        coin = denominations.pop(0)
        change += money // coin
        money = money % 10
    return change

if __name__ == '__main__':
    money=int(input())
    print(moneyChanger(money))
