def is_prime(n):
    if n == 1:
        print(n, "is not a prime number")
    elif n > 1:

        for i in range(2, n):
            if (n % i) == 0:
                return f"{n} is not a prime number"
                break
        else:
            return "is a prime number"

    # if input number is less than
    # or equal to 1, it is not  prime
    else:
        print(n, "is not a prime number")


print(is_prime(10))
