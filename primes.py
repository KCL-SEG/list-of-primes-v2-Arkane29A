"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):


    def isprime(num):
        for n in range(2,int(num**0.5)+1):

            if num%n==0:
                return False
        return True



    list = []


    if number_of_primes == 0 or number_of_primes < 0:
        return ValueError


    for x in range (2, number_of_primes):


        if isprime(x) == True:
            list.append(x)

        else:
            pass

       

        

    return list

