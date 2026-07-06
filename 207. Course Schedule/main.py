from ast import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dq = deque()

        for IDs in prerequisites:
            if IDs[0] == IDs[1]:
                return False

            if IDs[0] in dq:
                if IDs[1] in dq:
                    if dq.index(IDs[0]) < dq.index(IDs[1]):
                        return False
                else:
                    dq.insert(dq.index(IDs[0]), IDs[1])
            
            elif IDs[1] in dq:
                dq.insert(dq.index(IDs[1]) + 1, IDs[0])

            else:
                dq.appendleft(IDs[0])
                dq.appendleft(IDs[1])

        print(dq)
        return True

        

if __name__ == "__main__":

    numCourses = 20
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    #[4,17,1,15,13,14,11,6,5,18,3,10,0]

    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(result)
    