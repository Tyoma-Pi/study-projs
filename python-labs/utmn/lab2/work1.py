def numeralsToInt():
    numerals = str(input('Введите римское число: '))
    romanNums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    numFromRoman = 0
    i = 0
    while i < len(numerals):
        if i + 1 < len(numerals) and numerals[i:i+2] in romanNums:
            numFromRoman += romanNums[numerals[i:i+2]]
            i += 2
        else:
            numFromRoman += romanNums[numerals[i]]
            i += 1
    return numFromRoman


print(numeralsToInt())
