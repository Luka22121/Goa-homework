def is_perfect_square(num):
    if num < 0:
        return False
    i = 0
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False

