def longest_string():
    in_str = input('Введите строку (повторите в\nконце любой предыдущий символ)\n')
    temp_part = []
    out_parts = []
    for i in range(len(in_str)):
        if in_str[i] not in temp_part:
            temp_part.append(in_str[i])
        else:
            out_parts.append(''.join(temp_part))
            del temp_part[:]
            temp_part.append(in_str[i])
    out_parts.append(''.join(temp_part))
    max_part = max(out_parts, key=len)
    return max_part
# йцукйтполдьбис
# abcdferklhipzadfkdmkkla


print(longest_string())
