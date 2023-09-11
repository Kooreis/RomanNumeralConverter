# Python Documentation

# Python Script for Roman Numeral Conversion

This Python script provides a simple interface for converting integers to Roman numerals and vice versa. It does not require any external libraries, making it easy to run on any system with Python installed.

## Script Description

The script contains two main functions: `int_to_roman(input)` and `roman_to_int(input)`. 

- `int_to_roman(input)` takes an integer as input and returns its Roman numeral equivalent. If the input is not an integer, it returns "Invalid input".

- `roman_to_int(input)` takes a Roman numeral as input and returns its integer equivalent. If the input is not a Roman numeral, it returns "Invalid input".

The script also contains a simple while loop that provides a user interface for the conversion functions. The user can choose to convert an integer to a Roman numeral, convert a Roman numeral to an integer, or exit the program.

## Function Descriptions

### `int_to_roman(input)`

This function converts an integer to a Roman numeral. It first checks if the input is an integer. If it is, it uses a while loop to divide the input by the largest possible Roman numeral value, then subtracts that value from the input and adds the corresponding Roman numeral to the output string. This process is repeated until the input is 0. If the input is not an integer, the function returns "Invalid input".

### `roman_to_int(input)`

This function converts a Roman numeral to an integer. It first checks if the input is a string. If it is, it iterates over the string, adding the value of each Roman numeral to the output integer. If a numeral is smaller than the next numeral, it subtracts twice the value of the smaller numeral from the output integer. If the input is not a string, the function returns "Invalid input".

## User Interface

The user interface is a simple while loop that prompts the user to choose an option: convert an integer to a Roman numeral, convert a Roman numeral to an integer, or exit the program. If the user chooses to convert an integer or a Roman numeral, they are prompted to enter the number or numeral. The converted value is then printed to the console. If the user chooses to exit the program, the while loop is broken and the program ends. If the user enters an invalid choice, the program prints "Invalid choice" and prompts the user to choose an option again.

---

# C# Documentation

# CSharp Roman Numerals Converter

This C# script is a simple console application that converts an integer input into its equivalent Roman numeral representation.

## Script Description

The script prompts the user to enter a number. It then converts this number into its equivalent Roman numeral and displays the result on the console.

## Code Breakdown

The script is composed of a `Main` method and a helper method `IntToRoman`.

### Main Method

The `Main` method is the entry point of the script. It first prompts the user to enter a number. It then converts this number into a Roman numeral using the `IntToRoman` method and displays the result.

### IntToRoman Method

The `IntToRoman` method takes an integer as input and returns a string that represents the Roman numeral equivalent of the input number. It uses a dictionary to map integers to their corresponding Roman numerals. It then iterates over this dictionary in descending order, subtracting the largest possible value from the input number until it becomes zero.

## Imported Libraries

The script uses two namespaces from the .NET Framework:

- `System`: This namespace contains fundamental classes and base classes that define commonly-used value and reference data types, events and event handlers, interfaces, attributes, and processing exceptions. In this script, it is used to handle standard I/O operations (via `Console`) and exceptions (via `Convert`).

- `System.Collections.Generic`: This namespace contains interfaces and classes that define generic collections, which allow users to create strongly typed collections that provide better type safety and performance than non-generic strongly typed collections. In this script, it is used to create a dictionary that maps integers to their corresponding Roman numerals.

## Usage

To use this script, simply run it in a C# compatible environment. When prompted, enter a number to convert to Roman numerals. The script will then display the Roman numeral equivalent of the entered number.

---

# Java Documentation

# Java Roman Numeral Converter

This Java script is a simple Roman numeral converter. It takes an integer input and converts it to its equivalent Roman numeral representation. The script is capable of converting numbers from 1 to 1000.

## Script Overview

The script uses a `TreeMap` to map integers to their corresponding Roman numerals. The `TreeMap` is a Red-Black tree based NavigableMap implementation. It is used in this script because it provides guaranteed log(n) time cost for the `containsKey`, `get`, `put` and `remove` operations. 

The `toRoman` method is a recursive function that finds the highest value in the `TreeMap` that is less than or equal to the input number. It then subtracts this value from the input number and recursively calls itself until the input number is reduced to 0. The Roman numeral representation is built up during this process.

The `main` method runs a loop from 1 to 100, calling the `toRoman` method for each number and printing the result.

## Imported Libraries

- `java.util.TreeMap`: This is a Red-Black tree based implementation of the NavigableMap interface. The map is sorted according to the natural ordering of its keys, or by a Comparator provided at map creation time, depending on which constructor is used. This implementation provides guaranteed log(n) time cost for the `containsKey`, `get`, `put` and `remove` operations.

## Usage

To use this script, simply run the `Main` class. The script will print the Roman numeral representation for numbers 1 to 100.

## Example

Here is an example of the output:

```
1	 =	 I
2	 =	 II
3	 =	 III
4	 =	 IV
5	 =	 V
6	 =	 VI
7	 =	 VII
8	 =	 VIII
9	 =	 IX
10	 =	 X
...
```

This shows the integer on the left and its Roman numeral representation on the right.

---
