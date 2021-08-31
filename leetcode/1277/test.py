class Solution:
    def minWindow(self, s, t):
        count_t = Counter(t)
        count_s = Counter({ s[0]: 1 })
        n = len(s)
        i, j = 0, 0
        result, min_size = "", float('inf')
        while j < n:
            if self.check(count_s, count_t):
                if min_size > j - i + 1:
                    min_size = j - i + 1
                    result = s[i:j+1]
                count_s[s[i]] -= 1
                i += 1
            else:
                j += 1
                if j < n: count_s[s[j]] += 1

        return result

    def check(self, count_s, count_t):
        for k in count_t.keys():
            if count_t[k] > count_s[k]:
                return False
        return True
