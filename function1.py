#Try writing a function called is_even(number) 
# that returns True for an even number and False for an odd one.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def double(number):
    return number * 2

result = double(4)
print(result + 1)  # 9

def show_double(number):
    print(number * 2)

result = show_double(4)  # prints 8
print(result)            # prints None

#Write a function larger(a, b) 
# that returns the larger of two numbers. Try using if and else

def larger(a, b):
    if a > b:
        return a
    else:
        return b    


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Maya"))          # Hello, Maya!
print(greet("Maya", "Hi"))    # Hi, Maya!

def cal_tax(income, tax_rate=0.2):
    return income - (income * tax_rate)

print(cal_tax(1000))        # 200.0
print(cal_tax(1000, 0.3))   # 300.0 

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input type"
    except Exception as e:
        return f"An error occurred: {e}"

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Cannot divide by zero
print(divide(10, "a"))  # Invalid input type
print(divide(10, None))  # Invalid input type