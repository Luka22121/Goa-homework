my_list = [1, 2, 3, 4, 5]

# append() - ამატებს ელემენტს ბოლოში
my_list.append(6)  # [1, 2, 3, 4, 5, 6]

# insert() - ამატებს ელემენტს მითითებულ ინდექსზე
my_list.insert(2, 99)  # [1, 2, 99, 3, 4, 5, 6]

# extend() - ამატებს სიას სხვა სიას ბოლოში
my_list.extend([7, 8])  # [1, 2, 99, 3, 4, 5, 6, 7, 8]

# remove() - შლის კონკრეტულ ელემენტს
my_list.remove(99)  # [1, 2, 3, 4, 5, 6, 7, 8]

# pop() - შლის და აბრუნებს ბოლო ან მითითებულ ინდექსზე არსებულ ელემენტს
my_list.pop()  # 8, დარჩება: [1, 2, 3, 4, 5, 6, 7]

# index() - აბრუნებს ელემენტის ინდექსს
my_list.index(4)  # 3

# count() - რამდენჯერ მეორდება კონკრეტული მნიშვნელობა
my_list.count(3)  # 1

# sort() - ასორტირებს სიას ზრდადობით
my_list.sort()  # [1, 2, 3, 4, 5, 6, 7]

# reverse() - აბრუნებს სიის მიმდევრობას
my_list.reverse()  # [7, 6, 5, 4, 3, 2, 1]


