def count_digits_in_text():
    text = input("შეიყვანე ტექსტი: ")
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count


