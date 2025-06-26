mixed_list = [10, "hello", 3.14, False, "world", 50, True]

mixed_list.pop(3)  # წაშლის 3-ე ინდექსს (False)
mixed_list.pop(2)  # წაშლის 2-ე ინდექსს (3.14)
mixed_list.pop(4)  # წაშლის 4-ე ინდექსს (50) — ინდექსები იცვლება წაშლის მერე
print(mixed_list)

# მაგალითი 1
lst1 = [1, 2, 3, 4, 5]
lst1.pop()  # წაშლის ბოლო ელემენტს (5)
print(lst1)

# მაგალითი 2
lst2 = ["a", "b", "c"]
lst2.pop(0)  # წაშლის პირველ ელემენტს ("a")
print(lst2)
