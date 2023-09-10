class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number to convert to Roman Numerals:");
        int number = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Roman Numeral: " + IntToRoman(number));
    }