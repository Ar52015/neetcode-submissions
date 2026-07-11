class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, int> hm;
        vector<vector<string>> res;

        for (const string& s : strs) {

            int charmap[26] = {};
            for (char c : s)
                charmap[c - 'a']++;

            string key;
            for (int i = 0; i < 26; i++) {
                key += '#';
                key += to_string(charmap[i]);
            }

            auto it = hm.find(key);
            if (it != hm.end()) {
                res[it->second].push_back(s);
            } else {
                hm[key] = res.size();
                res.push_back({s});
            }

        }

        return res;

    }
};
