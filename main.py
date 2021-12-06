# Odd or Even Number
def odd_or_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Print Prime Number in given Range
def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# prime_number(int(input("Enter a number: ")))

# Print all Prime Number in given Range
def prime_number_range(prime_number_range):
    Prime_of_arrays = []
    for i in range(2, prime_number_range):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            Prime_of_arrays.append(i)
    print(Prime_of_arrays)


prime_number_range(int(input("Enter a number: ")))


