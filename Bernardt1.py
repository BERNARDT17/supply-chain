def testfibinocci(n):
    a=1
    b=2
    for i in range(n):
        print(a)
        a,b=b,a+b

testfibinocci(15)
