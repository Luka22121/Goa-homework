mixed_list = ["start", 20, 3.14, True, "end"]

# ელემენტების ჩასმა კონკრეტულ ინდექსზე
mixed_list.insert(2, "middle1")  # მესამე ინდექსი
mixed_list.insert(4, "middle2")  # მეხუთე ინდექსი
mixed_list.insert(6, "middle3")  # მეშვიდე ინდექსი
print(mixed_list)

# მაგალითი 1
lst1 = [1, 2, 3, 4]
lst1.insert(1, 100)
lst1.insert(3, 200)
lst1.insert(5, 300)
print(lst1)

# მაგალითი 2
lst2 = ["x", "y", "z"]
lst2.insert(0, "start")
lst2.insert(2, "middle")
lst2.insert(5, "end")
print(lst2)
