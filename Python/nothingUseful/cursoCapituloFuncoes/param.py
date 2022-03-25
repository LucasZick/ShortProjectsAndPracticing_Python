def show(p1=0,p2=0,p3=0):
    return(p1,p2,p3)

if __name__ == '__main__':
    assert show(p2=2) == (0, 2, 0)
    assert show(p1=1,p2=2,p3=3) == (1, 2, 3)
    assert show() == (0, 0, 0)