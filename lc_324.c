// https://leetcode.com/problems/wiggle-sort-ii/discuss/77688/O(n)%2BO(1)-after-median-without-Virtual-Indexing-%3A-)
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return;
    
        // Find a median.
        auto midptr = nums.begin() + n / 2;
        nth_element(nums.begin(), midptr, nums.end());
        int mid = *midptr;
        
        int i = (n - 1) / 2 * 2, j = i, k = 1;
        for (int c = 0; c < n; ++c) {
            if (nums[j] < mid) {
                swap(nums[i], nums[j]);
                i -= 2;
                j -= 2;
                if (j < 0) j = n / 2 * 2 - 1;
            } else if (nums[j] > mid) {
                swap(nums[j], nums[k]);
                k += 2;
            } else {
                j -= 2;
                if (j < 0) j = n / 2 * 2 - 1;
            }
        }
    }
};