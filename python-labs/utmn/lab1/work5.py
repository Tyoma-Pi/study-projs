def check_str():
    in_str = input('Введите строку: ')
    seen = []
    for c in in_str: # c = character
        if c not in seen:
            seen.append(in_str.count(c))
    seen_counts = list(set(seen))
    if len(seen_counts) == 2\
            and abs(seen_counts[0] - seen_counts[1]) < 2\
            or len(seen_counts) == 1:
        return True
    else:
        return False


print(check_str())
