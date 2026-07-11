class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
        
        int chr[26];

        for (char sc : s)
            chr[sc - 'a']++;

        for (char tc : t)
            chr[tc - 'a']--;
        
        for (int i : chr) {
            if (i != 0)
                return false;
        }

        return true;

    }
};
