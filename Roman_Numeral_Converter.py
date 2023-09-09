def int_to_roman(input):
    if isinstance(input, type(1)):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 
               100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", 
               "L", "XC", "C", "CD", "D", "CM", "M"]
        roman_num = ''
        i = 12
        while  input:
            div = input // num[i]
            input %= num[i]
            while div:
                roman_num += sym[i]
                div -= 1
            i -= 1
        return roman_num
    else:
        return "Invalid input"