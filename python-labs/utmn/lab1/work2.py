def anagram():
    in_str = sorted(str(input('Введите строку слов: ')).lower().split())
    matches = str()

    for i in range(len(in_str)):
        for j in range(len(in_str)):
            if len(in_str[i]) == len(in_str[j])\
                    and in_str[i] != in_str[j]\
                    and sorted(list(in_str[i])) == sorted(list(in_str[j]))\
                    and in_str[i] not in matches:
                matches += '\n' + in_str[i] + ' - ' + in_str[j]
    return matches


print(anagram())

