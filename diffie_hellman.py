import random

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list

random_list = primesInRange(100, 500)

g=random.randint(1, 10)
p=random.choice(random_list)

# Alice number
a=random.randint(5, 10)

#Bob number
b=random.randint(10,20)

# Diffe-hellmam
A = (g**a) % p
B = (g**b) % p

print('g: ',g,' (a shared value), p: ',p, ' (a prime number)')

print('\nAlice calculates:')
print('a (Alice random number): ',a)
print('Alice value (A): ',A,' (g^a) mod p')

print('\nBob calculates:')
print('b (Bob random): ',b)
print('Bob value (B): ',B,' (g^b) mod p')

print('\nAlice secret key:')
keyA=(B**a) % p
print('Key: ',keyA,' (B^a) mod p')

print('\nBob secret key:')
keyB=(A**b) % p
print('Key: ',keyB,' (A^b) mod p')
