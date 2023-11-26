"""

"""
import copy


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_grid = [[None]*len(s)] * numRows

        print(zigzag_grid)
        row_pointer = numRows-1 # trace my indexes
        col = 0
        char_ind = 0
        while char_ind < len(s):
            if row_pointer+1 == numRows:
                for i in range(numRows):

                    if char_ind < len(s):
                        print(i, col, s[char_ind])
                        row = copy.deepcopy(zigzag_grid[i])
                        row[col] = s[char_ind]
                        zigzag_grid[i] = row

                        char_ind += 1
                        print(f"Updated to  ==> {zigzag_grid[i][col]}")
                    else:
                        break

            else:
                print(row_pointer, col, s[char_ind])

                row = zigzag_grid[row_pointer]
                row[col] = s[char_ind]
                zigzag_grid[row_pointer] = row

                char_ind += 1
                print(f"Updated to {zigzag_grid[row_pointer][col]}")

            col += 1
            row_pointer -= 1

            if row_pointer < 1:  # reset row pointer
                row_pointer = numRows-1

        res = ""
        for row in zigzag_grid:
            for val in row:
                if val:
                    res += val

        return res






if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print("")