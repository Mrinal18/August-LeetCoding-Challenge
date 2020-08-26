"""

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.


Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        res.append('1')
        
        for i in range(1, n):
            if (i + 1) % 3 == 0 and (i + 1)%5 == 0:
                res.append("FizzBuzz")
            elif ( i + 1) % 5 == 0:
                res.append('Buzz')
            elif (i + 1) % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(i+1))     
        return res


