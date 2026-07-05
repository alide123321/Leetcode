from collections import deque
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        queue = deque(words)
        output = [""]
        currLine = 0

        while len(queue) > 0:

            currLength =  0
            wordsToAdd = deque()

            if currLine != 0:
                output.append("")

            while True:
                currLength += len(queue[0])
                wordsToAdd.append(queue.popleft())

                if len(queue) <= 0 or currLength + len(wordsToAdd) + len(queue[0]) > maxWidth:
                    break

            numOfExtraSpaces = maxWidth - currLength 
            gaps = len(wordsToAdd) - 1
            base = numOfExtraSpaces // gaps if gaps > 0 else 1
            extra = numOfExtraSpaces % gaps if gaps > 0 else numOfExtraSpaces


            if len(queue) == 0:

                while len(wordsToAdd) > 1:
                    output[currLine] += wordsToAdd.popleft() + " "

                output[currLine] += wordsToAdd.popleft()
                
                while len(output[currLine]) < maxWidth:
                    output[currLine] += " "

                break

            while len(wordsToAdd) > 1:
                output[currLine] += wordsToAdd.popleft()

                for i in range(base):
                    output[currLine] += " "

                if extra > 0:
                    output[currLine] += " "

                extra -= 1


            output[currLine] += wordsToAdd.popleft()

            while len(output[currLine]) < maxWidth:
                output[currLine] += " "

            currLine += 1


        return output