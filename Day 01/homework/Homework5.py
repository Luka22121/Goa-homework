# მომხმარებლისგან მონაცემების მიღება
car_name = input("შეიყვანე ავტომობილის სახელი: ")
car_color = input("შეიყვანე ავტომობილის ფერი: ")
car_price = int(input("შეიყვანე ავტომობილის ფასი (რიცხვით): "))
car_year = int(input("შეიყვანე ავტომობილის გამოშვების წელი: "))

# კონკატენაცია f-string-ის გამოყენებით
sentence = ( {car_name},  {car_color}, {car_price},{car_year} )

print(sentence)
