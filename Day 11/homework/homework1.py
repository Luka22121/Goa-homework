def is_even_or_odd(num):
    if num % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

# მაგალითი
number = int(input("შეიყვანეთ მთელი რიცხვი: "))
print(is_even_or_odd(number))
