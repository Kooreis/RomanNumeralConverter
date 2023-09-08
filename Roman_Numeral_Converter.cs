```CSharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number to convert to Roman Numerals:");
        int number = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Roman Numeral: " + IntToRoman(number));
    }

    static string IntToRoman(int num)
    {
        Dictionary<int, string> map = new Dictionary<int, string>()
        {
            {1000, "M"},
            {900, "CM"},
            {500, "D"},
            {400, "CD"},
            {100, "C"},
            {90, "XC"},
            {50, "L"},
            {40, "XL"},
            {10, "X"},
            {9, "IX"},
            {5, "V"},
            {4, "IV"},
            {1, "I"}
        };

        string result = "";
        foreach (var item in map)
        {
            while (num >= item.Key)
            {
                result += item.Value;
                num -= item.Key;
            }
        }
        return result;
    }
}
```