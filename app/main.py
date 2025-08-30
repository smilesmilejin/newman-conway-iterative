def newman_conway(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    # elif n > 2
    output = [1, 1]


    for i in range(3, n+1):
        # print(output)
        p_n_1= output[i-1-1]

        first = output[p_n_1 - 1]

        # print('### first value P(P(n - 1)) is ', first)

        num = i - p_n_1

        # print(num)

        second = output[num - 1]

        # print('### second value P(n - P(n - 1)) is ', second)

        output.append(first + second)

        # print(output)

    return output

# P(1) = 1 
# P(2) = 1

# n = 1, [1]
# n = 2, [1, 1]

# for all n > 2:
# P(n) = P(P(n - 1)) + P(n - P(n - 1))

# P(3) = P(P(3-1)) + P(3 - P(3-1))
# P(3) = P(P(2)) + P(3 - 1)
# P(3) = P(1) + P(2) = 1 + 1 = 2

# n = 3, [1, 1, 2]



print(newman_conway(5)) #  [1, 1, 2, 2, 3]

print(newman_conway(12)) # [1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7]