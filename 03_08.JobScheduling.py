def jobScheduling(list_tuples):
    '''
    Given:
    A list of tuples of the form (name, profit, deadline)
    e.g.
    Job  Profit  deadline
    A    50      2
    B    20      1
    C    30      2
    D    25      1
    E    15      3

    Return:
    Most profitable schedule of the form string of jobs:
    e.g.
    DAE
    '''



    '''
    Pseudocode:    
    Make slots by deadline ascending
    1, 2, 3
    
    Fill the most profitable job in it's deadline slot.
    1: DB
    fill D
    2: AC
    fill A
    3: E
    fill E

    Return: DAE
    '''
    
