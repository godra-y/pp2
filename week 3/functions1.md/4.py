def filter_prime(number):
    for i in number: 
        if i>1: 
            for j in range(2, i): 
                if(i%j)==0: 
                    break 
            else: 
                print(i)
prime=[int(i) for i in input().split()]
filter_prime(prime)