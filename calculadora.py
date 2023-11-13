def soma(x,y):
    """
        soma x e y
        
        >>> soma(10, 20)
        30 
        >>> soma(-15, 20)
        5
        >>> soma(5, 20)
        
    """

    assert isinstance(x, (int, float)) , 'O valor de X precisa ser inteiro ou float' 
    assert isinstance(y, (int, float)) , 'O valor de Y precisa ser inteiro ou float'
    
    return x+y

if __name__ == '__main__':
    import doctest
    
    doctest.testmod(verbose=True)