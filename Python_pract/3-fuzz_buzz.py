def fizz_buzz(input):
    if input%3 == 0 and input%5 == 0 :
        return f"Fizz_Buzz"
    elif input%5 == 0:
        return f"Buzz"
    elif input%3 == 0:
        return f"Fizz"
    else:
        return f"{input}"
    


print(fizz_buzz(8))