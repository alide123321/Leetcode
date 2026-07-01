#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string xS = to_string(x);
        int i = 0, j = xS.length() - 1;

        while(i < j) if(xS[i++] != xS[j--]) return false;

        return true;
    }
};