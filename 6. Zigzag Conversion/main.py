class Solution:
    def convert(self, s: str, numRows: int) -> str:
        

        if numRows == 1 or numRows >= len(s):
            return s

        strRows = []
        output = ""

        for i in range(numRows):
            strRows.append("")
        
        rowNum = 0
        flipDir = False

        for i in range(len(s)):
            strRows[rowNum] += s[i]

            if flipDir:
                rowNum -= 1
            else:
                rowNum += 1
            
            if rowNum == 0 or rowNum == (numRows - 1):
                flipDir = not flipDir

        for i in range(numRows):
            output += strRows[i]

        return output