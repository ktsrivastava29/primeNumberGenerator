import sys
import time

primes = []


def calculate_prime_numbers(how_many, iterations):
    elapsed_time_sum = 0
    for i in range(iterations):
        start = time.time()
        primes = [2]
        possible_prime = 3
        while len(primes) <= how_many:
            is_prime = True
            for num in range(2, possible_prime):
                if possible_prime % num == 0:
                    is_prime = False
            if is_prime:
                primes.append(possible_prime)
            possible_prime += 2

        end = time.time()
        elapsed_time = round(end-start, 4)
        elapsed_time_sum += elapsed_time
        print('Iteration: {}\nElapsed time: {} seconds'.format(i+1, elapsed_time))
        # print(primes[0:-1])
    return(elapsed_time_sum/iterations)


def print_help():
    print('Hi, this script is a prime number generators/benchmark')
    print('The first argument is the number of prime numbers to try, the second number is the number of iterations.')
    print("You can use the following command line: 'python prime_number_generator 1000 2' or just 'python prime_number_generator' without arguments.")
    sys.exit()


if len(sys.argv) == 1:
    try:
        how_many = int(input("How many numbers to generate: "))
        iterations = int(input("How many iterations: "))
    except:
        print("Invalid input!")
        sys.exit(1)

if len(sys.argv) == 2:
    arg1 = sys.argv[1]
    if arg1 == 'help' or arg1 == '?':
        print_help()
    else:
        try:
            int(arg1) > 0
            how_many = int(arg1)
            iterations = 1
        except:
            print("Invalid input!")
            sys.exit()


if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    try:
        how_many = int(arg1)
        iterations = int(arg2)
    except:
        print("Invalid input!")
        sys.exit()

average_time_elapsed = round(calculate_prime_numbers(how_many, iterations), 4)
print("\nAverage time elapsed: {} seconds".format(average_time_elapsed))