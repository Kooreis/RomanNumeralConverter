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