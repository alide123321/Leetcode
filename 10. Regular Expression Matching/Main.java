class Solution {
    public boolean isMatch(String s, String p) {
        StringBuilder regexPat = new StringBuilder();
        int pLength = p.length();
        for (int i = 0; i < pLength; ++i) {
            char c = p.charAt(i);
            if (i + 1 < pLength && p.charAt(i + 1) == '*') {
                if (c == '.') {
                    regexPat.append(".*");
                } else {
                    regexPat.append(c).append('*');
                }
                ++i; // skip '*'
            } else {
                regexPat.append(c);
            }
        }
        String regex = "^" + regexPat.toString() + "$";
        return s.matches(regex);
    }
}
