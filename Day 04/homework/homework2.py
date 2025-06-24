word = input("შეიტანეთ სიტყვა: ")
number = int(input("შეიტანეთ რიცხვი: "))
result = ''.join([char * number for char in word])
print(result)
