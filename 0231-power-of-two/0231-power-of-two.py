# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if (n < 0):
#             return False
#         elif (n == 1):
#             return True
#         else:
#             while(n % 2 == 0):
#                 n = n/2

#             if(n == 1):
#                 return True
#             else:
#                 return False                    
        
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False 
#         return (n & (n-1)) == 0

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n % 2 == 0:
#             n //= 2

#         return n == 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 2 != 0:
            return False
        return self.isPowerOfTwo(n//2)