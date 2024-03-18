
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# the one indexing took me a while to think about, but after setting the iterating 1, n + 1 and then i-1 for indices
# to prevent overflow, it worked out. I think a neat skill to know is how to create an array with n * [0]
# finally, adding the check that i needs to be greater than 2 for the 3 check and 4 for the 5 check was 
# important


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = n *[0]

        for i in range(1,n+1):
            if (i> 2 and i % 3 == 0) and (i > 4 and i % 5 == 0 ):
                answer[i-1] = "FizzBuzz"
            elif (i > 4 and i % 5 == 0):
                answer[i-1] = "Buzz"
            elif (i > 2 and i % 3== 0):
                answer[i-1] = "Fizz"
            else:
                answer[i-1] = str(i)
        
        return answer
        
        


        
