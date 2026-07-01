#include <string>
#include <regex>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        string regexPat = "";
        int pLength = p.length();
        for(int i = 0; i < pLength; ++i){
            if(i+1 < pLength && p[i + 1] == '*'){
                regexPat += p[i] == '.' ? ".*" : "(" + string(1, p[i]) + ")*";
                ++i;
            } else {
                regexPat += p[i];
            }
        }
        return regex_match(s, regex("^" + regexPat + "$"));
    }
};