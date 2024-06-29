def main():

    numbers = []
    for x in range (0,5):
        user = int(input("Enter Value: "))
        numbers.append(user)

    maxval = numbers[0]
    for i in numbers:
        if i > maxval:
            maxval = i

    minval = numbers [0]
    for y in numbers:
        if y < minval:
            minval = y

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
