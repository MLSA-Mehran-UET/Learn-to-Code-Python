#program to check the prime numbers
#we are taking input of a number and converting it in to float then in to an integer
#conditions to check prime number
#As we know prime number is always greater than 1

#taking input
num = int(float(input("Enter any number: ")))


if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break;
    else:
        print(num, "is a prime number")

# if the input is not greater than 1
else:
    print(num, "is not a prime number")