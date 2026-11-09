import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Better to name them plural for clarity
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # Check for duplicates in current row, column, or 3x3 box
                box_key = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in squares[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[box_key].add(val)

        return True
