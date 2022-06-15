"""
Word Search
-------

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, columns = len(board), len(board[0])
        path = set()

        def dfs(row, column, char):

            if char == len(word):
                return True
            if (
                row < 0
                or column < 0
                or row >= rows
                or column >= columns
                or word[char] != board[row][column]
                or (row, column) in path
            ):
                return False

            path.add((row, column))
            res = (
                dfs(row + 1, column, char + 1)
                or dfs(row - 1, column, char + 1)
                or dfs(row, column + 1, char + 1)
                or dfs(row, column - 1, char + 1)
            )
            path.remove((row, column))
            return res

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True

        return False


### Time Complexity: O( n * m * 4^(lenght of word))
