class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ht;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            if (ht.contains(target-nums[i])) {
                res.push_back(ht[target-nums[i]]);
                res.push_back(i);
            }
            ht[nums[i]] = i;
        }

        return res;
    }
};
