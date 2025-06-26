def get_non_divisibles():
    divisor = int(input("შეიყვანე გამყოფი: "))
    numbers = list(range(1, 51))  
    result = []

    for num in numbers:
        if num % divisor != 0:
            result.append(num)
    return result

