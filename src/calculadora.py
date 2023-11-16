def soma(x,y):
    """
        soma x e y
                
        >>> soma(-15, 20)
        5
        
        >>> soma(10, 20)
        30
    """

    assert isinstance(x, (int, float)) , 'O valor de X precisa ser inteiro ou float' 
    assert isinstance(y, (int, float)) , 'O valor de Y precisa ser inteiro ou float'
    
    return x+y

def subtrai(x,y):
    """
        subtrai x e y
        
        >>> subtrai(10, 5)
        5
        
        >>> subtrai('10', 5)
        Traceback (most recent call last):
        AssertionError: O valor de X precisa ser inteiro ou float
    """
    assert isinstance(x, (int, float)) , 'O valor de X precisa ser inteiro ou float' 
    assert isinstance(y, (int, float)) , 'O valor de Y precisa ser inteiro ou float'
    
    return x-y


if __name__ == '__main__':
    import doctest
    
    doctest.testmod(verbose=True)