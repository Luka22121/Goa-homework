def reverse_with_dash(text):
    reversed_text = "goa"
    for char in text:
        reversed_text = char + "-" + reversed_text
    return reversed_text.strip("-")

print(reverse_with_dash("goa"))