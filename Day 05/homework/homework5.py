
n = int(input("შეიყვანე 10-ზე მაღალი რიცხვი: "))
sum_for = 0
for i in range(5, n+1):
    sum_for += i
print("ჯამი for loop-ით:", sum_for)


i = 5
sum_while = 0
while i <= n:
    sum_while += i
    i += 1
print("ჯამი while loop-ით:", sum_while)
