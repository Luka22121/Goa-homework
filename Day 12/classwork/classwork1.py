def count_a_letters():
    text = input("შეიყვანე ტექსტი: ")
    count = 0
    for char in text:
        if char.lower() == 'a':
            count += 1
    return count

