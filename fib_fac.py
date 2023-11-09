def fibonacci(number):
    if(number<=0):
        return []
    elif(number == 1):
        return [0]
    else:
        sequence = [0,1]
        while(len(sequence)<number):
            sequence.append(sequence[-1]+sequence[-2])
        return sequence

def factorial(number):
    if(number == 0):
        return 1
    else:
        return number*factorial(number-1)

def main():
    print("Agrima Gupta - 11501012021")
    try:
        number = int(input("Enter a number: "))
        if number<0:
            print("Factorial and Fibonacci sequence undefined.")
        else:
            fac = factorial(number)
            fib = fibonacci(number)
            print(f"Factorial of {number} is {fac}")
            print(f"Fibonacci sequence of length {number} is {fib}")
    except ValueError:
        print("Enter a valid integer input")

if __name__ == "__main__":
    main()