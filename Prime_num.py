def check_prime(num):

    if num > 1:
        for i in range(2,int(num/2) + 1):
            if (num % i) == 0:
                print('The number',num,'is not prime number')
                break
        else:
            print('The number',num,'is prime number!!!')
    else:
        print('The number',num,'is not prime number')
num = int(input('Enter the number to check wheather it is prime or not : '))
check_prime(num)