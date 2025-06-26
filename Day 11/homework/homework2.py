def positive_or_negative(num):
    if num > 0:
        return "დადებითია"
    elif num < 0:
        return "უარყოფითია"
    else:
        return "ნულია"

# მაგალითი
number = float(input("შეიყვანეთ რიცხვი: "))
print(positive_or_negative(number))
