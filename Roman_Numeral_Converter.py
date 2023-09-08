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

def roman_to_int(input):
    if isinstance(input, type("I")):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(input)):
            if i > 0 and rom_val[input[i]] > rom_val[input[i - 1]]:
                int_val += rom_val[input[i]] - 2 * rom_val[input[i - 1]]
            else:
                int_val += rom_val[input[i]]
        return int_val
    else:
        return "Invalid input"

while True:
    print("\n1. Integer to Roman Numeral")
    print("2. Roman Numeral to Integer")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        num = int(input("Enter an integer: "))
        print(int_to_roman(num))
    elif choice == '2':
        num = input("Enter a Roman Numeral: ")
        print(roman_to_int(num.upper()))
    elif choice == '3':
        break
    else:
        print("Invalid choice")