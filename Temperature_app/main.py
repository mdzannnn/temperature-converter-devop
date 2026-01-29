from src.app import celsius_to_fahrenheit, fahrenheit_to_celsius, is_freezing, celsius_to_kelvin

def run_app():
    print("=== DevOps Temperature Converter Prototype ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("\nSelect an option (1-3): ")
    temp = input("Enter the temperature value: ")

    try:
        # Convert input to a number
        val = float(temp)
        
        if choice == '1':
            result = celsius_to_fahrenheit(val)
            print(f"\nResult: {val} C is {result} F")
        elif choice == '2':
            result = fahrenheit_to_celsius(val)
            print(f"\nResult: {val} F is {result} C")
        elif choice == '3':
            result = celsius_to_kelvin(val)
            print(f"\nResult: {val} C is {result} K")
        
        # Check freezing status
        if choice in ['1', '3'] and is_freezing(val):
            print("Status: This temperature is at or below freezing! (Safe Check)")

    except ValueError as e:
        print(f"\n[Logic Error]: {e}")
    except TypeError as e:
        print(f"\n[Validation Error]: {e}")
    except Exception as e:
        print(f"\n[Error]: Something went wrong.")

if __name__ == "__main__":
    while True:
        run_app()
        if input("\nTry again? (y/n): ").lower() != 'y':
            break