correct_password = "secret123"
attempts = 0
while attempts < 3:
    password = input("შეიტანეთ პაროლი: ")
    if password == correct_password:
        print("პაროლი სწორია!")
        break
    else:
        attempts += 1
        print("არასწორი პაროლი, დარჩენილი ცდები:", 3 - attempts)
if attempts == 3:
    print("პაროლის ცდები ამოიწურა.")
