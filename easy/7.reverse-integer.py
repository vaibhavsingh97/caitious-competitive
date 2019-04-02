#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.22%)
# Total Accepted:    640.5K
# Total Submissions: 2.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
#
#


class Solution:
    def reverse(self, x: int) -> int:
        res = ""
        if x < 0:
            stack = []
            for i in list(map(int, str(abs(x)))):
                stack.append(i)
            for i in range(len(stack)):
                res += str(stack.pop())
            if int("-" + res) < (-1 << 31):
                return 0
            else:
                return int("-" + res)
        else:
            stack = []
            for i in list(map(int, str(abs(x)))):
                stack.append(i)
            for i in range(len(stack)):
                res += str(stack.pop())
            if (abs(int(res)) > ((1 << 31) - 1)):
                return 0
            else:
                return int(res)
