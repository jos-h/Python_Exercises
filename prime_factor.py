def prime_factors(num):
    prime_list = list()
    div, prime_fact = 0, 2
    while num >= prime_fact * prime_fact:
        if num % prime_fact == 0:
            div = num // prime_fact
            num = div
            prime_list.append(prime_fact)
        else:
            prime_fact += 1
    if div == 0:
        print("prime_list", num)
    else:
        print("prime_list", prime_list)

prime_factors(100)

