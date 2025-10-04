#!/usr/bin/env python3
# Problem: LeetCode 329 - Longest Increasing Path in a Matrix
# 
# Given an m x n integer matrix, return the length of the longest increasing path in the matrix.
# From each cell, you can move in four directions: up, down, left, or right. You may NOT move
# diagonally or move outside the boundary (i.e., wrap-around is not allowed).
# The path must be strictly increasing (each next cell's value > current cell's value).
#
# Example:
# Input: matrix = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9] (or [1,6,9, ...] depending on route).

from typing import List
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if memo[i][j]:
                return memo[i][j]
            best = 1
            val = matrix[i][j]
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > val:
                    cand = 1 + dfs(ni, nj)
                    if cand > best:
                        best = cand
            memo[i][j] = best
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                if memo[i][j] == 0:
                    dfs(i, j)
                if memo[i][j] > ans:
                    ans = memo[i][j]
        return ans

if __name__ == "__main__":
    sol = Solution()
    mat = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    print(sol.longestIncreasingPath(mat))
