n=int(input('Enter the number:'))

def checkprime(n):
        if n<=1:
                return False
        for i in range(2,n):
                if (n%i==0):
                        return False
        return True

if checkprime(n):
        print(n,"is prime number")
else:
        print(n,'is not a prime number')

#time complexity o(n)
#space comlexity o(n)
