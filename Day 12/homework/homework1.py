def get_integers_from_list(mixed_list):
    result = []
    for item in mixed_list:
        if isinstance(item, int):
            result.append(item)
    return result

# მაგალითი:
print(get_integers_from_list(["hello", 42, 3.14, True, 7, "5"]))  # [42, 7]
