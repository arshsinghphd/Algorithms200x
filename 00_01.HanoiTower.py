def hanoiTower(n, from_, to_):
    '''
    HANOI TOWER: we have three towers: 1, 2, 3.
  
    START: In the beginning, n discs are arranged from largest on bottom and
    smallest on top in Tower 2.
  
    END CONDITION: all discs are rearranged on Tower 1 smallest on top.
  
    RULES: we are allowed to move discs from any tower to any other tower to
    reachcthe end condition, but no disc can be placed on top on a smaller disc
    at any time.
  
    Return: the minimum number of steps needed to reach from start to end.
    '''
    global counter, call

    if n == 1:
        counter += 1
        print("Step {}: move disc from {} to {}"
              .format(counter, from_, to_))

    else:
        unused_ = 6 - from_ - to_
        call += 1
        print("Call no.",call,
              "n = {}, from_ = {}, to_ = {}".format(n-1,from_,unused_))
        hanoiTower(n - 1, from_, unused_)
        counter += 1
        print("Step {}: move disc from {} to {}".format(counter, from_, to_))
        call += 1
        print("Call no.", call,"n = {}, from_ = {}, to_ = {}"
              .format(n-1,unused_,to_))
        hanoiTower(n - 1, unused_, to_)

    return counter

if __name__ == '__main__':
    #n = int(input())
    n = 4
    counter = 0
    call = 1
    from_ = 2
    to_ = 1
    print("Call no.", call,"n = {}, from_ = {}, to_ = {}".format(n,from_,to_))
    print("Total steps:",hanoiTower(n,from_,to_))
