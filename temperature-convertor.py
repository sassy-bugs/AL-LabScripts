def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Temperature is below absolute zero, which is not physically possible."
    else:
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

def main():
    print("Agrima Gupta - 11501012021")
    try:
        celsius = float(input("Enter temperature in degrees Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        if type(fahrenheit) == str:
            print(fahrenheit)
        else:
            print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a valid number for temperature.")

if __name__ == "__main__":
    main()
