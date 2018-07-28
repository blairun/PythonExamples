def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    bTup = ()
    i=0
    n=0
    for n in range(0,len(aTup)):
        bTup += (aTup[i],)
        i +=2
    
    return bTup

oddTuples((13, 13, 7, 8, 14, 6, 19, 15))



###################