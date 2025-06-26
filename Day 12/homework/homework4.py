def collect_words():
    words = []
    while True:
        word = input("შეიყვანე სიტყვა: ")
        if word.lower() == "საკმარისია":
            break
        words.append(word)
    return words

print(collect_words())
