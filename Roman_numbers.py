class RomanNumerals:
    roman_dict={'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X':10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D':500, 'CM': 900, 'M': 1000}

    @staticmethod
    def to_roman(val):
        t=''
        for k, v in sorted(RomanNumerals.roman_dict.items(), key=lambda x: x[1], reverse=True):
            a = int(val//v)
            t+=k*a
            val -= a*v
        return t

    @staticmethod
    def from_roman(roman_num):
        t=0
        for a in [x for x in RomanNumerals.roman_dict.keys() if len(x)==2]:
            if a in roman_num:
                t+=RomanNumerals.roman_dict[a]*roman_num.count(a)
                roman_num = roman_num.replace(a, "")
        for a in [x for x in RomanNumerals.roman_dict.keys() if len(x)==1]:
            if a in roman_num:
                t+=RomanNumerals.roman_dict[a]*roman_num.count(a)
                roman_num = roman_num.replace(a, "")
        return t

'''Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
1000 -> "M"
 400 -> "CD"
  90 -> "XC"
  40 -> "XL"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      -> 400
"XC"      -> 90
"XL"      -> 40
"I"       -> 1'''

print(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
print(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
print(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
print(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
print(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')
#    @test.it('from roman')
#    def sample_tests_from():
print(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
print(RomanNumerals.from_roman('I'), 1, 'I should == 1')
print(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
print(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
print(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
