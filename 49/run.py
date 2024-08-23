class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mpp = {}
        ans = []
        ind = 0

        for s in strs:

            sorted_s = ''.join(sorted(s))

            if sorted_s in mpp:
                ans[mpp[sorted_s]].append(s)
            else:
                mpp[sorted_s] = len(ans)
                ans.append([s])

        return ans

# we first store len of ans, then append the string because list has 0 based indexing

# TC - [N*k*logk] - N is list size (traversal), k is longest string (sort func), log k is appending to dictionary
# SC - [N*k] - N is list size (store sorted strings), k is longest string (space of mpp value)