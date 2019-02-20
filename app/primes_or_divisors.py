# number = int(input("Enter a digit and i will check if it is a prime"))
def primes_or_remainders(number):
    upper_limit = int(number / 2 + 1)
    divisors = list(range(2, upper_limit))

    dividing_by = [divisor for divisor in divisors if number % divisor == 0]
    if not dividing_by:
        return True
    else:
        return dividing_by


check_number = 417
answer = primes_or_remainders(check_number)
if answer is True:
    print(check_number, 'is a prime')
else:
    print('{} is not a prime it has {} divisors'.format(check_number, len(answer)) if len(answer) < 2 else
          '{} is not a prime it has {} divisor'.format(check_number, len(answer)))

