import time 
usr_inp = int(input('press 1 for fibonacci series\npress 2 for armstrong\npress 3 for reverse of a nummber\npress 4 for palindrome\npress 5 for diagonal elements of a matrix\n \nyour option: '))

if usr_inp == 1:
    n = int(input('enter how many number you want in series: '))
    p = 0
    q = 1
    for i in range(n):
        r = p + q
        print(r)
        p , q = q , p + q
    
elif usr_inp == 2:
    n = int(input("Enter the number to be checked: "))
    s = 0
    t = n
    while t > 0:
        dig = t % 10
        s += dig ** 3
        t //= 10
    if n == s:
       print(n,"is an Armstrong number")
    else:
       print(n,"is not an Armstrong number")
       
elif usr_inp == 3:
    n = int(input("Please Enter any Number: "))
    rev = 0
    while(n > 0):
        rem = n %10
        rev = (rev *10) + rem
        n = n //10  
    print("\n Reverse of entered number is = %d" %rev)
    
elif usr_inp == 4:
    n=int(input("Enter the number to be checked: "))
    temp=n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    if(temp==r):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
        
elif usr_inp == 5:
    time.sleep(4)
    print('...')
    time.sleep(2)
    print('....')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('....')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('....')
    time.sleep(5)
    print('working on it...')
    time.sleep(7)
    print('working on it....')
    time.sleep(8)
    print('under maintainence')
    print('try again later')
        
else:
    print('pls enter a valid number from the menu')